#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path


def load_trade_stats(csv_path: Path) -> dict:
    wins = 0
    losses = 0
    gross_profit = 0.0
    gross_loss = 0.0
    has_mark_to_market = False

    if not csv_path.exists():
        return {
            "closed_trades_from_csv": 0,
            "profit_factor": 0.0,
            "has_mark_to_market": False,
        }

    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            row_type = (row.get("type") or "").strip()
            if row_type == "win":
                wins += 1
                gross_profit += float(row.get("profit") or 0)
            elif row_type == "loss":
                losses += 1
                loss_value = float(row.get("loss") or row.get("profit") or 0)
                gross_loss += abs(loss_value)
            elif row_type == "open_mark_to_market":
                has_mark_to_market = True

    closed = wins + losses
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else (float("inf") if gross_profit > 0 else 0.0)
    return {
        "closed_trades_from_csv": closed,
        "profit_factor": round(profit_factor, 2) if profit_factor != float("inf") else "inf",
        "has_mark_to_market": has_mark_to_market,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python3 12_SUMMARIZE_BACKTESTS.py <validation_dir>")
        return 1

    base_dir = Path(sys.argv[1]).resolve()
    result_files = sorted(base_dir.glob("*_result.json"))
    if not result_files:
        print(f"No se encontraron archivos *_result.json en {base_dir}")
        return 1

    rows = []
    for result_file in result_files:
        with result_file.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)

        stem = result_file.name.removesuffix("_result.json")
        trade_stats = load_trade_stats(base_dir / f"{stem}_trades.csv")
        total_trades = int(payload.get("total_trades") or 0)

        rows.append({
            "symbol": payload.get("symbol", stem),
            "final_capital": payload.get("final_capital", 0),
            "return_pct": payload.get("total_return_pct", 0),
            "total_trades": total_trades,
            "wins": payload.get("wins", 0),
            "losses": payload.get("losses", 0),
            "winrate_pct": payload.get("winrate_pct", 0),
            "avg_win_pct": payload.get("avg_win_pct", 0),
            "avg_loss_pct": payload.get("avg_loss_pct", 0),
            "profit_factor": trade_stats["profit_factor"],
            "has_mark_to_market": trade_stats["has_mark_to_market"],
            "sample_quality": "insuficiente" if total_trades < 15 else "media" if total_trades < 40 else "mejor",
            "evidence_status": (
                "sin_cierres"
                if total_trades == 0 and trade_stats["has_mark_to_market"]
                else "sin_muestra"
                if total_trades == 0
                else "valido"
            ),
        })

    rows.sort(key=lambda item: (item["return_pct"], item["winrate_pct"]), reverse=True)

    valid_rows = [row for row in rows if row["total_trades"] > 0]
    best_row = max(valid_rows, key=lambda item: (item["return_pct"], item["winrate_pct"])) if valid_rows else rows[0]

    summary = {
        "validation_dir": str(base_dir),
        "runs": rows,
        "best_symbol_by_return": best_row["symbol"],
        "profitable_runs": sum(1 for row in rows if row["return_pct"] > 0 and row["total_trades"] > 0),
        "insufficient_sample_runs": sum(1 for row in rows if row["sample_quality"] == "insuficiente"),
    }

    with (base_dir / "summary.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2)

    csv_fields = [
        "symbol",
        "final_capital",
        "return_pct",
        "total_trades",
        "wins",
        "losses",
        "winrate_pct",
        "avg_win_pct",
        "avg_loss_pct",
        "profit_factor",
        "has_mark_to_market",
        "sample_quality",
        "evidence_status",
    ]
    with (base_dir / "summary.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Resumen de validacion",
        "",
        f"- Directorio: `{base_dir}`",
        f"- Corridas rentables: `{summary['profitable_runs']}/{len(rows)}`",
        f"- Muestras insuficientes: `{summary['insufficient_sample_runs']}/{len(rows)}`",
        f"- Mejor retorno: `{summary['best_symbol_by_return']}`",
        "",
        "| Symbol | Return % | Trades | Winrate % | Profit Factor | Calidad muestra | Evidencia |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['symbol']} | {row['return_pct']} | {row['total_trades']} | "
            f"{row['winrate_pct']} | {row['profit_factor']} | {row['sample_quality']} | {row['evidence_status']} |"
        )

    with (base_dir / "summary.md").open("w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
