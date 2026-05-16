# GUÍA DE USO RÁPIDO — SISTEMA JORGE

> Nota V2: la versión operable recomendada está resumida en `08_ESTRATEGIA_V2_CONSERVADORA.md`.
> El bot ya no debe llevar credenciales hardcodeadas. Usa variables de entorno siguiendo `09_BOT_ENV.example`.

## SETUP DE TRADINGVIEW (10 minutos)

### 1. Agregar los indicadores
1. Abre TradingView → par BTCUSDT en Binance o Bybit
2. Clic en **Pine Script Editor** (pestaña inferior)
3. Borra el código de ejemplo, pega el contenido de `05_TRADINGVIEW_PINE_SCRIPT.pine` → clic **Guardar** → **Agregar al gráfico**
4. Repite para `06_TRADINGVIEW_SQUEEZE_MOMENTUM.pine` → esto crea un panel separado debajo

### 2. Configurar alertas (paso a paso)

**Para CADA alerta que quieras activar:**

1. Clic en el ícono del **reloj** (alertas) en la barra lateral derecha, o presiona `Alt+A`
2. Clic en **"+ Crear alerta"**
3. En el campo **"Condición"** → selecciona el indicador:
   - `"Estrategia Jorge - EMA + 12 Velas + Squeeze"` → para alertas del script principal
   - `"Squeeze Momentum — Jorge"` → para alertas del panel de squeeze
4. En el **segundo desplegable** aparecen todas las condiciones nombradas — elige una:

**Alertas del script principal (05):**
| Condición en el desplegable | Cuándo suena |
|---|---|
| `🟢 LONG FUERTE — Vela 7 + Compresión + Squeeze + ADX` | Entrada máxima convicción (todos los argumentos) |
| `🟡 LONG ALT — Cruce EMA + Squeeze + Volumen + ADX` | Cruce fresco con confirmaciones |
| `🔁 LONG 4TO TOQUE — EMA55 ya es soporte` | 4to toque = entrada directa |
| `🔴 SHORT / COBERTURA — Compresión Fallida + ADX` | Compresión fallida, cubrir |
| `🔀 Cambio Estructural ALCISTA — EMA10 cruza EMA55` | Nuevo ciclo alcista |
| `🔀 Cambio Estructural BAJISTA — EMA10 cruza EMA55` | Nuevo ciclo bajista |
| `⚡ Compresión de EMAs Iniciada` | EMAs se están comprimiendo |
| `⏰ Vela 7 Alcanzada — Zona de Entrada` | Momento de revisar entrada |
| `📍 Precio en EMA55 — Zona de Rebote` | Precio tocando soporte dinámico |
| `⚠️ Precio Sobreextendido de EMA10 — No Entrar` | No entrar, esperar corrección |
| `🌀 Squeeze Momentum ALCISTA` | Momentum acelerando al alza |
| `🌀 Squeeze Momentum BAJISTA` | Momentum acelerando a la baja |
| `🚀 Squeeze DISPARADO ALCISTA` | Disparo urgente — entrada LONG |
| `💣 Squeeze DISPARADO BAJISTA` | Disparo urgente — cubrir |
| `🟡 Valle Squeeze toca cero — Señal Compra` | Valle verde tocó 0 y rebotó |
| `💜 Rebote EMA55 con Absorción` | Rebote en EMA55 + volumen |
| `🔲 Precio en Order Block Alcista` | Precio en zona OB institucional |
| `✳️ Estructura Alcista Confirmada — EMA15 > EMA30` | Estructura menor confirma alza |

**Alertas del Squeeze Momentum (06):**
| Condición en el desplegable | Cuándo suena |
|---|---|
| `⚡🟢 Squeeze Liberado ALCISTA` | Disparo alcista — entrada urgente |
| `⚡🔴 Squeeze Liberado BAJISTA` | Disparo bajista — cubrir urgente |
| `🔒 Squeeze ACTIVADO — Acumulando energía` | Empieza acumulación, prepararse |
| `🔓 Squeeze LIBERADO — Confirmar dirección` | Energía liberada, ver histograma |
| `↑ Momentum cruza CERO al alza` | Cambio de sesgo a alcista |
| `↓ Momentum cruza CERO a la baja` | Cambio de sesgo a bajista |
| `🟡 PRE-SEÑAL LONG — Squeeze ON + Momentum positivo` | Alerta temprana alcista |
| `🟠 PRE-SEÑAL SHORT — Squeeze ON + Momentum negativo` | Alerta temprana bajista |

5. **Configurar notificación:**
   - ✅ **Notificación en la app** (recomendado — activa en móvil)
   - ✅ **Email** (para no perderse nada)
   - 🔔 **Webhook** → pega tu URL de bot de Telegram si tienes uno
6. En **"Opciones de activación"** → elegir `"Al cierre de la vela"` (más fiable, menos ruido)
7. Clic **"Crear"**

### 3. Alertas mínimas recomendadas (las 7 esenciales)
Configura ESTAS en todos los timeframes que operes (1D, 4H, 1H):

1. `🟢 LONG FUERTE` — señal de entrada principal (máxima convicción)
2. `🔁 LONG 4TO TOQUE` — entrada directa por regla del 4to toque EMA55
3. `🔀 Cambio Estructural ALCISTA` — inicio de nuevo ciclo
4. `⚡ Compresión de EMAs Iniciada` — prepararse para entrada
5. `🚀 Squeeze DISPARADO ALCISTA` — disparo final urgente
6. `🟡 Valle Squeeze toca cero` — señal de compra de Jorge
7. `🔴 SHORT / COBERTURA` — protección de posición

### 4. Configuración de layout recomendada
```
┌─────────────────────────────────────────────────────┐
│  GRÁFICO PRINCIPAL (EMA10 + EMA55 + señales)        │
│  Timeframe: 4H (análisis) o 1H (entrada)            │
├─────────────────────────────────────────────────────┤
│  SQUEEZE MOMENTUM (panel inferior)                   │
│  Colores: verde brillante=subiendo, verde oscuro=perdiendo fuerza │
│           rojo brillante=bajando, rojo oscuro=perdiendo fuerza   │
│  Puntos: negro=squeeze ON, gris=OFF, azul=sin squeeze│
└─────────────────────────────────────────────────────┘
```

### 5. Multi-timeframe recomendado
- Ventana izquierda: **1D** (macro)
- Ventana central: **4H** (análisis principal)
- Ventana derecha: **1H** (afinación entrada)

---

## SETUP DEL BOT (primeros pasos)

### Requisitos
```bash
pip install ccxt pandas numpy ta requests
```

### Configurar API
Usa variables de entorno, no edites secretos dentro del script.

```bash
cp 09_BOT_ENV.example .env.local
```

Exporta las variables antes de correr el bot:

```bash
export JORGE_BOT_PAPER=true
export JORGE_BOT_TESTNET=true
export JORGE_BOT_API_KEY=tu_api_key
export JORGE_BOT_API_SECRET=tu_api_secret
export JORGE_BOT_TELEGRAM_TOKEN=tu_token
export JORGE_BOT_TELEGRAM_CHAT_ID=tu_chat_id
```

### Runner automático recomendado
```bash
chmod +x 10_RUN_PAPER_TESTNET.sh
./10_RUN_PAPER_TESTNET.sh
```

### Suite automática de validación antes de prod
Esto corre backtests por lote en varios activos y deja un resumen consolidado.

```bash
chmod +x 11_RUN_VALIDATION_SUITE.sh
./11_RUN_VALIDATION_SUITE.sh
```

Por defecto barre:
- `BTC/USDT:USDT`
- `ETH/USDT:USDT`
- `SOL/USDT:USDT`

Y usa una ventana más amplia:
- `5000` velas de entrada
- `3600` velas intermedias
- `1200` velas macro

Si quieres cambiar símbolos:

```bash
export JORGE_BOT_VALIDATION_SYMBOLS="BTC/USDT:USDT,ETH/USDT:USDT,BNB/USDT:USDT"
./11_RUN_VALIDATION_SUITE.sh
```

Archivos generados automáticamente:

- `jorge_trade_journal.csv` → eventos y cierres del bot
- `jorge_trade_metrics.json` → métricas resumidas
- `jorge_backtest_result.json` → último backtest
- `jorge_backtest_trades.csv` → operaciones del backtest
- `validation_runs/<timestamp>/summary.json` → resumen consolidado del barrido
- `validation_runs/<timestamp>/summary.csv` → tabla rápida para comparar activos
- `validation_runs/<timestamp>/summary.md` → lectura humana

### Obtener API keys
**Bybit Testnet**: https://testnet.bybit.com → Cuenta → API Management
**Binance Testnet**: https://testnet.binancefuture.com

### Ejecutar en testnet
```bash
# Modo trading normal
python 04_SCRIPT_BOT_PYTHON.py

# Modo backtest (análisis histórico)
python 04_SCRIPT_BOT_PYTHON.py backtest
```

---

## PROCESO MANUAL DIARIO (15 minutos)

### Mañana (análisis macro)
1. Abrir BTCUSDT en **1D**
2. ¿EMA10 > EMA55? → sesgo alcista
3. ¿Precio alejado >3% de EMA10? → esperar corrección
4. ¿EMAs comprimidas? → movimiento próximo
5. Anotar nivel de EMA55 en 1D (soporte/resistencia clave)

### Durante el día (afinación)
1. Revisar **4H**: ¿En qué vela del conteo estamos?
2. ¿El Squeeze Momentum está en verde?
3. ¿Hay absorción en volumen?
4. Si estamos en vela 5-8 + compresión + squeeze verde → preparar entrada

### Entrada
1. Bajar a **1H** para confirmar
2. Precio cerca de EMA55 en 1H = zona de rebote ideal
3. Entrar primer 20% del capital planificado
4. Poner TP1, TP2, TP3 según los niveles del archivo 02

---

## SEÑALES CLAVE RESUMIDAS

| Señal | Qué hacer |
|-------|-----------|
| EMAs comprimidas + vela 7 + squeeze verde | LONG — entrada primera parte |
| Cruce alcista EMA10/EMA55 | LONG — empieza conteo de 12 velas |
| Precio toca EMA55 en gráfico mayor | LONG de rebote (más cauteloso) |
| 12 velas sin superar resistencia + squeeze rojo | SHORT o cobertura |
| EMA10 cruza bajista EMA55 | SHORT o cerrar LONG |
| Subida sin volumen + wick alcista grande | Cuidado, posible techo |
| Bajada con wick bajista + alto volumen | Absorción, posible suelo |

---

## ERRORES COMUNES A EVITAR

❌ Entrar cuando el precio está muy alejado de la EMA10 (>3% en 1D)
❌ Ignorar el análisis macro y operar solo en 15m
❌ Operar sin invalidación dura
❌ Cerrar una posición con pérdida sin verificar si el análisis macro sigue válido
❌ Operar ALTs cuando BTC está en rango sin dirección
❌ Entrar por FOMO cuando ya subió y no hay señal
❌ Ignorar el volumen — subida sin volumen = trampa

---

## RECORDATORIOS DE JORGE

> "Cuando estás tradeando algo seguro no un meme, no importa el número en negativo"

> "Solo se deja correr hasta el OB — y se entra no importa que esté al -300%"

> "20% 20% 20% 20% 20% — con mi regla de 5 partes y chao"

> "Veo los gráficos desde 4H a 12H para afinar entradas en el diario"

> "Solo me va a tomar más tiempo de lo normal. Pero yo tengo paciencia."

> "El precio fluctúa según donde estén los Stop Loss de la gente"

---

## ARCHIVOS DEL SISTEMA

| Archivo | Contenido |
|---------|-----------|
| `ESTRATEGIA_DEFINITIVA_JORGE.md` | ⭐ DOCUMENTO MAESTRO — todos los conceptos con señales exactas |
| `01_ESTRATEGIA_COMPLETA.md` | Sistema completo documentado (versión anterior) |
| `02_REGLAS_ENTRADA_SALIDA.md` | Checklist y reglas de trading |
| `03_CONFIGURACION_BOT_BYBIT_BINANCE.json` | Config JSON del bot |
| `04_SCRIPT_BOT_PYTHON.py` | Bot autónomo Python con los 10 ARGUMENTOS + ADX + OB + Telegram |
| `05_TRADINGVIEW_PINE_SCRIPT.pine` | Script principal overlay — EMA+12V+Squeeze+ADX+OB+Toques |
| `06_TRADINGVIEW_SQUEEZE_MOMENTUM.pine` | Panel Squeeze Momentum TradingView |
| `07_GUIA_USO_RAPIDO.md` | Este archivo |
| `08_ESTRATEGIA_V2_CONSERVADORA.md` | Versión conservadora recomendada para consistencia |
| `09_BOT_ENV.example` | Plantilla de variables de entorno del bot |
| `10_RUN_PAPER_TESTNET.sh` | Runner automático paper/testnet |
| `11_RUN_VALIDATION_SUITE.sh` | Barrido automático de backtests multi-activo |
| `12_SUMMARIZE_BACKTESTS.py` | Consolida resultados y calidad de muestra |

---

*Sistema compilado de materiales del mentor Jorge — DigitalCapitalsTrading — Mayo 2026*
