"""
ADAPTIVE LAYER — capa 3 de la estrategia Jorge

Lee `jorge_trade_journal.csv` y devuelve:
- block_reason(side, type, killzone, dow, regime) → str | None
- sizing_multiplier(side, type, killzone, dow, regime) → float (0.0..1.5)
- bucket_metrics() → dict con WR/expectancy por combinación
- summarize() → texto humano para Telegram /adaptive

NO REEMPLAZA reglas duras del bot. Solo modula sizing y bloquea setups que han mostrado
underperformance reciente. Diseñado para ser conservador: con poca data devuelve
multiplicador 1.0 (neutral) — no aplica decisiones hasta tener al menos
`min_trades_per_bucket` cierres en esa combinación.
"""

from __future__ import annotations
import csv
import os
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional

# ─── CONFIG DE LA CAPA ADAPTATIVA ─────────────────────────────────────────────

ADAPTIVE_CONFIG = {
    # Tamaño mínimo de bucket para que las decisiones sean fiables.
    # Con menos trades, el bucket es "neutral" → multiplicador 1.0, sin bloqueo.
    "min_trades_per_bucket": 8,

    # Win rate mínimo aceptable. Por debajo → setup bloqueado.
    "block_below_wr": 0.40,

    # Profit factor mínimo (gross_win / gross_loss). Por debajo → bloqueado.
    "block_below_pf": 0.9,

    # Bloquear si hay N pérdidas consecutivas en este bucket
    "block_after_n_losses": 5,

    # Duración del bloqueo (días) tras detectarlo
    "block_duration_days": 7,

    # Ventana de análisis (días) — usa solo trades recientes para decisiones
    "lookback_days": 30,

    # Sizing: cómo escalar el multiplicador según WR del bucket
    "sizing_neutral_wr": 0.5,        # WR de referencia = sizing 1.0
    "sizing_max_mult":   1.5,        # tope superior (no sobrear-apostar)
    "sizing_min_mult":   0.4,        # tope inferior (mejor reducir, no eliminar)

    # Drawdown actual sobre balance — penaliza sizing si en racha negativa
    "drawdown_window_days": 7,
    "drawdown_penalty_per_pct": 0.05,  # 1% drawdown → -5% sizing
    "drawdown_max_penalty": 0.50,      # tope de penalización

    "trade_journal_file": "jorge_trade_journal.csv",
    "backtest_journal_file": "jorge_backtest_journal.csv",
}


# ─── DATA STRUCTURES ──────────────────────────────────────────────────────────

@dataclass
class BucketStats:
    side: str
    entry_type: str
    killzone: str
    dow: str
    regime: str
    trades: int = 0
    wins: int = 0
    losses: int = 0
    gross_pnl: float = 0.0
    gross_win: float = 0.0
    gross_loss: float = 0.0
    consecutive_losses: int = 0
    last_trade_ts: Optional[str] = None

    @property
    def win_rate(self) -> float:
        return self.wins / self.trades if self.trades else 0.0

    @property
    def profit_factor(self) -> float:
        return self.gross_win / self.gross_loss if self.gross_loss > 0 else (
            float("inf") if self.gross_win > 0 else 0.0
        )

    @property
    def expectancy_usdt(self) -> float:
        return self.gross_pnl / self.trades if self.trades else 0.0


# ─── PARSEO DEL JOURNAL ───────────────────────────────────────────────────────

# Eventos que CIERRAN una posición (parcial o total). Sus pnl_usdt cuentan para WR.
CLOSING_EVENTS = {
    "tp1", "tp2", "tp3",
    "tp1_short", "tp2_short", "tp3_short",
    "hard_stop", "hard_stop_short",
    "trailing_stop", "short_trail_close",
    "force_close", "force_close_short",
    "hedge_partial", "hedge_close", "hedge_force_close",
}

# Eventos que abren — usados para asociar los cierres con su contexto (entry_type, killzone…)
OPENING_EVENTS = {"open_long", "open_short_standalone", "open_hedge"}


def _parse_ts(s: str) -> Optional[datetime]:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return None


def load_buckets(cfg: dict = ADAPTIVE_CONFIG) -> dict[tuple, BucketStats]:
    """Lee el journal y agrupa cierres por (side, entry_type, killzone, dow, regime).

    Asocia cada evento de cierre con el contexto del último open_* del mismo side.
    Los buckets son la unidad de decisión de la capa adaptativa.
    """
    path = cfg.get("trade_journal_file", "jorge_trade_journal.csv")
    if not os.path.exists(path):
        return {}

    cutoff = datetime.utcnow() - timedelta(days=cfg.get("lookback_days", 30))
    last_open: dict[str, dict] = {}   # side → último open
    buckets: dict[tuple, BucketStats] = {}

    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = _parse_ts(row.get("timestamp", ""))
            if not ts or ts < cutoff:
                continue
            event = row.get("event", "")
            side  = row.get("side", "")

            if event in OPENING_EVENTS:
                last_open[side] = {
                    "entry_type": row.get("entry_type", "?"),
                    "killzone":   row.get("killzone", "n/a"),
                    "dow":        row.get("dow", ""),
                    "regime":     row.get("regime", "unknown"),
                }

            elif event in CLOSING_EVENTS:
                ctx = last_open.get(side, {
                    "entry_type": "?", "killzone": "n/a",
                    "dow": "", "regime": "unknown",
                })
                key = (
                    side,
                    ctx["entry_type"],
                    ctx["killzone"],
                    str(ctx.get("dow", "")),
                    ctx["regime"],
                )
                bucket = buckets.get(key)
                if bucket is None:
                    bucket = BucketStats(
                        side=key[0], entry_type=key[1], killzone=key[2],
                        dow=key[3], regime=key[4],
                    )
                    buckets[key] = bucket

                pnl_str = row.get("pnl_usdt", "0") or "0"
                try:
                    pnl = float(pnl_str)
                except ValueError:
                    pnl = 0.0
                bucket.trades += 1
                bucket.gross_pnl += pnl
                bucket.last_trade_ts = row.get("timestamp", "")
                if pnl > 0:
                    bucket.wins += 1
                    bucket.gross_win += pnl
                    bucket.consecutive_losses = 0
                elif pnl < 0:
                    bucket.losses += 1
                    bucket.gross_loss += -pnl
                    bucket.consecutive_losses += 1

    return buckets


# ─── DECISIONES ───────────────────────────────────────────────────────────────

def _bucket_key(side: str, entry_type: str, killzone: str, dow: int, regime: str) -> tuple:
    return (side, entry_type, killzone, str(dow), regime)


def _find_bucket(side: str, entry_type: str, killzone: str, dow: int, regime: str,
                 cfg: dict) -> Optional[BucketStats]:
    """Busca el bucket: primero live; si no existe, fallback a backtest journal."""
    key = _bucket_key(side, entry_type, killzone, dow, regime)
    buckets = load_buckets(cfg)
    bucket = buckets.get(key)
    if bucket:
        return bucket
    # Fallback a backtest cold-start
    bt_path = cfg.get("backtest_journal_file", "jorge_backtest_journal.csv")
    if os.path.exists(bt_path):
        bt_cfg = {**cfg, "trade_journal_file": bt_path, "lookback_days": 99999}
        bt_buckets = load_buckets(bt_cfg)
        return bt_buckets.get(key)
    return None


def block_reason(side: str, entry_type: str, killzone: str, dow: int, regime: str,
                 cfg: dict = ADAPTIVE_CONFIG) -> Optional[str]:
    """Devuelve la razón del bloqueo o None si el setup puede operarse.

    Bloquea si:
    - WR < block_below_wr y trades >= min_trades_per_bucket
    - PF < block_below_pf y trades >= min_trades_per_bucket
    - consecutive_losses >= block_after_n_losses
    """
    bucket = _find_bucket(side, entry_type, killzone, dow, regime, cfg)
    if not bucket:
        return None

    min_trades = cfg.get("min_trades_per_bucket", 8)

    if bucket.consecutive_losses >= cfg.get("block_after_n_losses", 5):
        return f"{bucket.consecutive_losses} pérdidas consecutivas"

    if bucket.trades >= min_trades:
        if bucket.win_rate < cfg.get("block_below_wr", 0.4):
            return f"WR {bucket.win_rate:.0%} < umbral"
        if bucket.profit_factor < cfg.get("block_below_pf", 0.9):
            return f"PF {bucket.profit_factor:.2f} < umbral"

    return None


def sizing_multiplier(side: str, entry_type: str, killzone: str, dow: int, regime: str,
                      current_drawdown_pct: float = 0.0,
                      cfg: dict = ADAPTIVE_CONFIG) -> float:
    """Multiplicador adaptativo de sizing.

    1.0 = neutral. >1.0 = bucket histórico fuerte. <1.0 = reducir tamaño.
    Penaliza si hay drawdown reciente independientemente del bucket.
    """
    bucket = _find_bucket(side, entry_type, killzone, dow, regime, cfg)

    base_mult = 1.0
    min_trades = cfg.get("min_trades_per_bucket", 8)
    if bucket and bucket.trades >= min_trades:
        ref_wr = cfg.get("sizing_neutral_wr", 0.5)
        wr     = bucket.win_rate
        ratio  = wr / ref_wr if ref_wr > 0 else 1.0
        base_mult = max(
            cfg.get("sizing_min_mult", 0.4),
            min(cfg.get("sizing_max_mult", 1.5), ratio)
        )

    # Penalización por drawdown reciente
    dd_penalty = min(
        cfg.get("drawdown_max_penalty", 0.5),
        max(0.0, current_drawdown_pct) * cfg.get("drawdown_penalty_per_pct", 0.05)
    )
    return max(0.1, base_mult * (1 - dd_penalty))


def compute_recent_drawdown_pct(cfg: dict = ADAPTIVE_CONFIG) -> float:
    """Drawdown desde el balance pico de la ventana, en porcentaje (0..100)."""
    path = cfg.get("trade_journal_file", "jorge_trade_journal.csv")
    if not os.path.exists(path):
        return 0.0
    cutoff = datetime.utcnow() - timedelta(days=cfg.get("drawdown_window_days", 7))
    peak = 0.0
    last_balance = 0.0
    with open(path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = _parse_ts(row.get("timestamp", ""))
            if not ts or ts < cutoff:
                continue
            try:
                bal = float(row.get("balance") or 0)
            except ValueError:
                continue
            if bal > 0:
                if bal > peak:
                    peak = bal
                last_balance = bal
    if peak <= 0 or last_balance <= 0:
        return 0.0
    return max(0.0, (peak - last_balance) / peak * 100.0)


def summarize(cfg: Optional[dict] = None) -> str:
    """Texto humano para Telegram /adaptive — top 5 buckets buenos y malos.
    Si no se pasa cfg, usa ADAPTIVE_CONFIG. Combina automáticamente live + backtest:
    la live tiene prioridad pero buckets que solo existen en backtest también se incluyen."""
    cfg = cfg or ADAPTIVE_CONFIG

    # Cargar live + backtest si existe
    buckets = load_buckets(cfg)
    bt_path = cfg.get("backtest_journal_file", "jorge_backtest_journal.csv")
    bt_buckets = {}
    if os.path.exists(bt_path):
        bt_cfg = {**cfg, "trade_journal_file": bt_path, "lookback_days": 99999}
        bt_buckets = load_buckets(bt_cfg)
        # Buckets que solo están en backtest (live aún no los tiene)
        for k, v in bt_buckets.items():
            if k not in buckets:
                buckets[k] = v
                v.entry_type = f"{v.entry_type}*"  # marca visual de cold-start

    if not buckets:
        return "📊 Capa adaptativa: aún sin trades cerrados en la ventana."

    rows = sorted(buckets.values(), key=lambda b: b.expectancy_usdt, reverse=True)
    drawdown = compute_recent_drawdown_pct(cfg)
    lines = [
        f"📊 <b>Capa adaptativa</b> ({len(rows)} buckets, ventana {cfg['lookback_days']}d)",
        f"DD reciente: {drawdown:.2f}%  |  * = solo backtest cold-start",
        "",
        "<b>Top performers:</b>",
    ]
    for b in rows[:5]:
        lines.append(
            f"  ✅ {b.side[:1].upper()}/{b.entry_type}/{b.killzone}/{b.regime[:5]}: "
            f"{b.trades}t WR {b.win_rate:.0%} PF {b.profit_factor:.2f} "
            f"exp {b.expectancy_usdt:+.2f} USDT"
        )
    lines.append("")
    lines.append("<b>Worst performers:</b>")
    for b in rows[-5:][::-1]:
        block = block_reason(b.side, b.entry_type.rstrip("*"), b.killzone,
                             int(b.dow) if b.dow.isdigit() else 0, b.regime, cfg)
        flag = "🚫" if block else "⚠️"
        lines.append(
            f"  {flag} {b.side[:1].upper()}/{b.entry_type}/{b.killzone}/{b.regime[:5]}: "
            f"{b.trades}t WR {b.win_rate:.0%} PF {b.profit_factor:.2f} "
            f"exp {b.expectancy_usdt:+.2f} USDT"
        )
    return "\n".join(lines)


# ─── CLI ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    print(summarize())
    if len(sys.argv) > 1 and sys.argv[1] == "verbose":
        print("\n── BUCKETS DETALLE ──")
        for k, v in load_buckets().items():
            print(f"{k}: {v.trades}t WR={v.win_rate:.0%} PF={v.profit_factor:.2f} "
                  f"exp={v.expectancy_usdt:+.2f}")
