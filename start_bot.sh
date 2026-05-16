#!/bin/bash
# Arranque persistente del bot Jorge con credenciales cargadas desde .env
cd "$(dirname "$0")"
set -a
source .env
set +a
# Mata instancias previas
pkill -f "04_SCRIPT_BOT_PYTHON.py" 2>/dev/null
sleep 2
# Lanza con nohup
nohup python3 04_SCRIPT_BOT_PYTHON.py > bot_stdout.log 2>&1 &
echo "Bot lanzado PID=$!"
sleep 6
ps aux | grep "04_SCRIPT_BOT_PYTHON.py" | grep -v grep | awk '{print "RUNNING PID", $2}'
echo ""
echo "=== Tail jorge_bot.log ==="
tail -8 jorge_bot.log
