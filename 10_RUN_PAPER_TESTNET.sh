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

export JORGE_BOT_PAPER="${JORGE_BOT_PAPER:-true}"
export JORGE_BOT_TESTNET="${JORGE_BOT_TESTNET:-true}"

echo "Iniciando bot en modo paper/testnet..."
echo "Journal: ${JORGE_BOT_JOURNAL_FILE:-jorge_trade_journal.csv}"
echo "Metrics: ${JORGE_BOT_METRICS_FILE:-jorge_trade_metrics.json}"

python3 04_SCRIPT_BOT_PYTHON.py
