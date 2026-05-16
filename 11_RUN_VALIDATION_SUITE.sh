#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [[ -f ".env.local" ]]; then
  set -a
  # shellcheck disable=SC1091
  source ".env.local"
  set +a
fi

RUN_TS="$(date +%Y%m%d_%H%M%S)"
OUT_DIR="${JORGE_BOT_VALIDATION_DIR:-$ROOT_DIR/validation_runs/$RUN_TS}"
mkdir -p "$OUT_DIR"

SYMBOLS_RAW="${JORGE_BOT_VALIDATION_SYMBOLS:-BTC/USDT:USDT,ETH/USDT:USDT,SOL/USDT:USDT}"
IFS=',' read -r -a SYMBOLS <<< "$SYMBOLS_RAW"

export JORGE_BOT_PAPER="${JORGE_BOT_PAPER:-true}"
export JORGE_BOT_TESTNET="${JORGE_BOT_TESTNET:-true}"
export JORGE_BOT_BACKTEST_ENTRY_CANDLES="${JORGE_BOT_BACKTEST_ENTRY_CANDLES:-5000}"
export JORGE_BOT_BACKTEST_MID_CANDLES="${JORGE_BOT_BACKTEST_MID_CANDLES:-3600}"
export JORGE_BOT_BACKTEST_MACRO_CANDLES="${JORGE_BOT_BACKTEST_MACRO_CANDLES:-1200}"

echo "Validation suite: $OUT_DIR"
echo "Símbolos: ${SYMBOLS[*]}"
echo "Ventanas: entry=$JORGE_BOT_BACKTEST_ENTRY_CANDLES mid=$JORGE_BOT_BACKTEST_MID_CANDLES macro=$JORGE_BOT_BACKTEST_MACRO_CANDLES"

for symbol in "${SYMBOLS[@]}"; do
  safe_name="${symbol//\//_}"
  safe_name="${safe_name//:/_}"
  echo ""
  echo "==> Backtest $symbol"
  export JORGE_BOT_SYMBOL="$symbol"
  python3 04_SCRIPT_BOT_PYTHON.py backtest
  cp jorge_backtest_result.json "$OUT_DIR/${safe_name}_result.json"
  cp jorge_backtest_trades.csv "$OUT_DIR/${safe_name}_trades.csv"
done

python3 12_SUMMARIZE_BACKTESTS.py "$OUT_DIR"

echo ""
echo "Resumen consolidado:"
echo "  $OUT_DIR/summary.json"
echo "  $OUT_DIR/summary.csv"
echo "  $OUT_DIR/summary.md"
