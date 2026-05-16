# ESTRATEGIA DEFINITIVA — JORGE (DigitalCapitalsTrading)
> Compilación exhaustiva de todo el material: texto, imágenes, Excel, chat de Telegram.
> Última actualización: Mayo 2026

---

## TABLA DE CONTENIDO

1. [Filosofía Central](#filosofia)
2. [Los 10 ARGUMENTOS — Checklist Maestro](#argumentos)
3. [EMAs — Estructura y Señales Exactas](#emas)
4. [Teoría de las 12 Velas — Timing de Entrada](#12velas)
5. [Squeeze Momentum + ADX PRO](#squeeze)
6. [VRVP — Perfil de Volumen](#vrvp)
7. [Indicador de Liquidez](#liquidez)
8. [Order Blocks (OB)](#ob)
9. [Rupturas Estructurales](#rupturas)
10. [Gestión de Capital y DCA](#capital)
11. [Cobertura (Hedge) Activa](#hedge)
12. [Proceso de Análisis Top-Down](#topdown)
13. [Tabla de Señales Exactas](#senales)
14. [Gestión de Riesgo — Reglas Absolutas](#riesgo)
15. [Psicología y Mindset](#psicologia)
16. [Configuración TradingView](#tradingview)

---

## 1. FILOSOFÍA CENTRAL {#filosofia}

> "Cuando estás tradeando algo seguro no un meme, no importa el número en negativo"

> "La forma de operar te va a ser rentable en el tiempo y vas a poder decir el día de mañana coño llevo 6 meses operando y no tengo 1 sola posición en negativo"

> "Solo me va a tomar más tiempo de lo normal. Pero yo tengo paciencia."

> "El precio fluctúa según donde estén los Stop Loss de la gente"

El sistema de Jorge es **anti-SL convencional**: no existe stop loss fijo. El riesgo se maneja con **cobertura activa** y **DCA en 5 partes**. La paciencia es la ventaja competitiva.

**Principios fundamentales:**
- Operar siempre **a favor de la tendencia macro** (1D/1S)
- Nunca entrar por **FOMO** — siempre esperar la señal
- Las **EMAs no mienten** en temporalidades altas (4H, 1D)
- El mercado siempre busca la liquidez antes de moverse
- Los institucionales (creadores de mercado) aplican las mismas herramientas: EMAs, OB, liquidez
- "El creador de mercado actúa con cautela para no mostrar sus posiciones. Toma liquidez del soporte antes de subir."

---

## 2. LOS 10 ARGUMENTOS — CHECKLIST MAESTRO {#argumentos}

*Extraído directamente del archivo ARGUMENTOS.txt del mentor*

Antes de entrar a cualquier operación, verificar TODOS estos argumentos:

| # | Argumento | Qué buscar |
|---|-----------|------------|
| 1 | **Todos los gráficos sincronizados** | 4H, 1H, 15m apuntando en la misma dirección |
| 2 | **S y R fuertes** | Soporte/resistencia claro, o líneas de tendencia activas |
| 3 | **OB virgen o zonas de reacción** | Order block no tocado desde 4H hacia arriba |
| 4 | **Liquidez** | Niveles de liquidez visibles en el indicador; precio yendo a buscarla |
| 5 | **Teoría de las 12 Velas** | En qué vela estamos del conteo; ideal: vela 7 |
| 6 | **Rupturas e imbalance** | ¿Hay un gap/imbalance que el precio deba cerrar? |
| 7 | **Regla del 3er/4to toque** | En resistencia: 3 toques la debilitan → 4to toque = LONG |
| 8 | **Datos de volumen** | Subida sin volumen = trampa; bajada con volumen en mecha = suelo |
| 9 | **EMAs** | R/S, cruce, inclinación/aplanamiento, compresión, sincronización, picos pequeños |
| 10 | **Confirmación multi-temporal** | OB virgen en 1D, refinar entrada en 4H, contar velas para entrada calculada |

**Regla de puntuación:** Los mejores trades tienen 8+ argumentos a favor. Con 5-6 se puede entrar con tamaño reducido (20% del capital planificado). Con menos de 5, no entrar.

---

## 3. EMAs — ESTRUCTURA Y SEÑALES EXACTAS {#emas}

### EMAs utilizadas

| EMA | Timeframe de referencia | Función |
|-----|------------------------|---------|
| **EMA 10** | 1D (macro), 4H (intermedio) | Soporte/resistencia dinámica principal; guía la tendencia |
| **EMA 55** | 4H (zona de decisión) | Zona institucional; rebotes desde aquí en tendencia alcista |
| **EMA 200 / MA200** | 1S/1M | Referencia macro; soporte/resistencia de largo plazo |
| **EMA 15** | 1H/15m | Confirmar rango vs. cambio de estructura |
| **EMA 30** | 1H/15m | Par con EMA15 para identificar rango y cambio de estructura |

> "Los traders que contratan los institucionales usan las EMAs por defecto de Binance"
> "Los retrocesos son a las pequeñas zonas de acumulación que casualmente coinciden con la EMA de 55"

### Señales de las EMAs

#### 3.1 Cruce Alcista EMA10/EMA55
- **Qué es:** EMA10 cruza SOBRE la EMA55
- **Significado:** Inicio de nuevo ciclo alcista — cambio estructural confirmado
- **Acción:** Comenzar conteo de 12 velas; preparar primera entrada
- **Timeframe:** Válido en 4H y 1D principalmente

#### 3.2 Cruce Bajista EMA10/EMA55
- **Qué es:** EMA10 cruza BAJO la EMA55
- **Significado:** Fin del ciclo alcista; estructura bajista confirmada
- **Acción:** Cerrar LONGs o tomar cobertura SHORT; NO abrir nuevos longs

#### 3.3 Compresión de EMAs
- **Qué es:** EMA10 y EMA55 se acercan entre sí, precio entre ambas
- **Significado:** Acumulación de energía — movimiento explosivo próximo
- **Acción:** Preparar entrada; monitorear de cerca el Squeeze Momentum
- **Duración típica:** 7-12 velas antes del breakout
- **Nota:** "Casualmente hoy se tocó la EMA10 en el diario y casualmente primer toque en la EMA55 en 4H → Compresión de EMAs → Posterior un rango"

#### 3.4 Compresión Fallida
- **Qué es:** EMAs comprimen pero precio NO supera resistencia en 12 velas
- **Significado:** La energía se agota; movimiento bajista confirmado
- **Acción:** SHORT o cobertura activa

#### 3.5 Distancia EMA10
- **1D:** Si precio se aleja >3% de EMA10 → esperar corrección; NO entrar
- **1S:** Si precio se aleja >20% de EMA10 → zona de techo
- **Escenarios posibles al acercarse a EMA10:** rebote para continuar tendencia, rango alrededor de EMA10, o ruptura directa
- "Mayor probabilidad de rango cuando es en gráficos mayores (1D o 1S) ya que se respeta más la EMA10"

#### 3.6 Regla del 3er/4to Toque de EMA55
- Cada toque de la EMA55 como resistencia la **debilita**
- **3er toque:** No funciona igual de fuerte como rechazo
- **4to toque = LONG** — la estructura ya está rota; la resistencia se convierte en soporte
- Contar los toques en el mismo timeframe de análisis

#### 3.7 EMA15/EMA30 para Estructura Menor
- Usar en 1H/15m para confirmar si el precio está en rango o cambiando estructura
- "Siguiendo las EMAs en 15 y 30 ves el rango y el cambio de estructura"
- El indicador Squeeze/ADX por sí solo no dice si es rango o caída — confirmar con EMA15/EMA30

#### 3.8 Timeframe Operativo de Entrada (NUEVO — confirmado por imágenes)
- **EMA10 en 1H o 30M = timeframe operativo real** para timing de entrada (no 1D)
- Jorge: "En la puta ema. En la ema entro. Ema de 10" → cuando le preguntaron si era 1D: "No esa está muy lejos. 1H por lo menos o 30M"
- **2H = timeframe institucional oculto**: "Vieron el retroceso a la EMA de 10 en 2H porque nadie ve ese"
- Los institucionales explotan el 2H porque el retail solo monitorea 1H, 4H y 1D
- Timeframe **mínimo para EMAs: 15M** — no usar EMA10/55 en velas menores a 15M

#### 3.9 Equivalencia Fractal de EMAs
- **EMA200 en 1H ≈ EMA55 en 4H** (mismo nivel de precio, distinto TF)
- **EMA55 en 1M ≈ EMA10 en 5M** — equivalencia fractal en cualquier par de TF
- Jorge confirmó: "Yo dejé de ver la EMA de 200" — EMA55 en TF superior lo sustituye
- Esto significa que cuando EMA55 en 4H actúa como soporte, es equivalente a EMA200 en 1H

#### 3.10 Regla de Separación EMA10 (CORRECCIONES)
- En tendencia alcista: **las correcciones van a la EMA10, NO a la EMA55**
- "Las correcciones en tendencia alcista es hasta la EMA de 10"
- Solo en tendencias muy sobreextendidas o cambio estructural el precio llega a la EMA55
- Ejemplos reales: BTC 42K→28K (EMA10 semanal), BTC 58K→43K (EMA10 semanal)
- La **EMA10 semanal predijo caídas de 14.000$ a 18.000$** — el que la ignora pierde fortuna

#### 3.11 Rango Detectado Antes de su Formación
- Con solo las EMAs Jorge predice rangos 10 días antes de que se formen
- "Dije no va a seguir subiendo, solo fue a la EMA. Vamos a tener un rango en el diario"
- "Rango de 3000$? 5000$? Y dije sí" — exacto antes de que ocurriera
- Cómo: observando la curvatura de las EMAs (aplanamiento de EMA10 después de extensión)

---

## 4. TEORÍA DE LAS 12 VELAS — TIMING DE ENTRADA {#12velas}

### Concepto Central
Después de un cambio estructural o movimiento impulsivo, el precio **rangea/acumula** por ~12 velas. La **vela 7** es el punto óptimo de entrada. La **vela 12** debe estar cerca de superar la resistencia.

### Cómo iniciar el conteo
| Escenario | Punto de inicio del conteo |
|-----------|---------------------------|
| Cruce alcista EMA10/EMA55 | Vela del cruce |
| Cambio estructural (vela envolvente) | Vela que rompe el mini-rango bajista |
| Squeeze Momentum cambia de bajista a alcista | Vela del cambio de cuadrante |
| Tendencia bajista con señales de agotamiento | Vela de rechazo en soporte clave |

### Reglas de la Vela 7
- **Entrada principal:** Vela N°7 del conteo
- Si en vela 7 el precio toca la EMA55 → **entrada sin miedo** (doble confirmación)
- Si los argumentos están a favor pero vela 7 no es perfecta → entrar igual, tamaño inicial
- Si llegamos a vela 11 con EMA10 aplanándose y precio sobre ambas EMAs → entrada óptima tardía

### Señales adicionales de entrada (con 12 velas)
- Absorción en mecha (wick) en zona de soporte en cualquier vela
- Squeeze Momentum pasando de cuadrante bajista a alcista
- Sincronización de 4H + 1H + 15m en misma dirección

### Duración de las 12 velas por timeframe (confirmado por Jorge)
| Timeframe | Duración del ciclo de 12 velas | Horizonte de holding |
|-----------|-------------------------------|---------------------|
| 15M | ~3 horas | 3 horas |
| 1H | 8–12 horas | 8–12 horas mínimo |
| 4H | 72 horas (3 días) | 3 días |
| 1D | ~12 días | 12 días |
| Regla | En tendencia bajista el timing es exacto; en alcista puede extenderse | — |

> "El problema es que 15M es para 3H" — Jorge
> "1H mínimo 8 horas, 4H 72 horas" — Jorge
> Si EMAs alcistas el resultado llega más rápido; si bajistas, es más lento

### Timeout de compresión
- Si la compresión en 4H no produce un breakout en **~8 horas** → setup se invalida
- "No hay compresión suficiente y el tiempo se le agota. 8 horas más"

### Señal de la valla/valley indicator (confirmado)
- **Valle verde toca el punto 0 pero NO cae** = señal de compra de libro
- "Si el valle verde toca el punto 0 y no cae es compra"
- "Casi llegó al punto 0 y allí marcaba compra de libro"
- "Triple valle rojo = máxima compresión antes de movimiento"

### Señal de falla de la teoría (SHORT)
- Precio hace máximos más bajos dentro del rango + toca EMA10 múltiples veces → distribución → SHORT
- Precio no supera resistencia en 12 velas → compresión fallida → cobertura

---

## 5. SQUEEZE MOMENTUM + ADX PRO {#squeeze}

### El Indicador Combinado
Jorge usa **SQZMOM & ADX** — muestra simultáneamente:
1. **Dirección** (alcista/bajista)
2. **Fuerza ADX** (con/sin tendencia; umbral ≈21 = sin tendencia)
3. **Estado del Squeeze** (ON/OFF)

> Nombre visible en sus gráficos: `SQZMOM & ADX Pd 0.55 20 2 20 1.5 14 14 23`

### Los 4 Cuadrantes del Squeeze Momentum

| Cuadrante | Histograma | Señal |
|-----------|------------|-------|
| **Impulso Alcista** | Verde oscuro → verde claro, bajo cero y subiendo | MÁS PODEROSO: preparar LONG |
| **Fuerza Alcista** | Verde, sobre cero y subiendo | Tendencia alcista activa; mantener LONG |
| **Impulso Bajista** | Rojo oscuro → rojo claro, sobre cero y bajando | MÁS PODEROSO: preparar SHORT |
| **Fuerza Bajista** | Rojo, bajo cero y bajando | Tendencia bajista activa; mantener SHORT |

### Señal de Compra Clave
> "Si el valle verde del MACD/Squeeze toca el punto 0 y no cae → es señal de compra"
- Histograma verde que se acerca a cero pero **rebota sin cruzarlo** = acumulación completa
- Actuar en esa vela o en la siguiente

### Interpretación del ADX
- ADX <21 = "Sin Tendencia" → no operar breakouts
- ADX ≥21 = Tendencia presente → operar en dirección del histograma
- Cuando ADX está en fuerza bajista e histograma en rojo → "Tiene fuerza bajista, interpreta" (NO entrar LONG)
- Cuando ADX cambia de dirección + histograma confirma → señal de entrada

### Regla de Confirmación con EMAs
- **Una sola señal del indicador NO basta** para determinar si es rango o caída
- Siempre confirmar con **EMA15 y EMA30** en 1H para ver el cambio de estructura

### Squeeze ON vs. Squeeze OFF
| Estado | Puntos | Qué hacer |
|--------|--------|-----------|
| **Squeeze ON** | Puntos negros | Acumulación activa; preparar órdenes, NO entrar aún |
| **Squeeze OFF** | Puntos grises | Energía liberada; verificar dirección del histograma y entrar |
| **Sin squeeze** | Puntos azules | Condición normal; seguir otras señales |

### Disparo Final (entrada urgente)
- Squeeze OFF + histograma positivo y subiendo = **🚀 LONG inmediato**
- Squeeze OFF + histograma negativo y bajando = **💣 SHORT inmediato**

---

## 5b. VOLUMEN DE PARADA — SEÑAL DE SUELO {#vol_parada}

> "El volumen de parada lo ven en la primera vela, paso seguido comienza a hacer rango, agarrando armonía de nuevo"

### Definición
El **volumen de parada** (stop candle) es la primera vela que aparece con volumen elevado después de una caída. Esta vela señala que los institucionales están absorbiendo la venta — es el preludio del suelo.

### Secuencia de confirmación
1. **Caída sostenida** — precio cae con velas rojas
2. **Vela de parada** — primera vela con volumen alto (>1.5x promedio), puede ser doji o wick largo bajista
3. **Rango de armonía** — el precio comienza a lateralizar ~2-4 velas después de la vela de parada
4. **Confirmación** — el precio no hace nuevos mínimos durante el rango → es el suelo

### Cómo usarlo para DCA
- Cuando aparece la vela de parada en zona de soporte (EMA55, OB) → **recomprar con 1-2% de la cuenta**
- "Simplemente voy comprando y donde vea la absorción importante entro"
- "No puedes quedarte con el 0.3 o 0.6% de la cuenta en esa sola entrada"
- La vela de parada en un OB virgen = entrada de máxima convicción

### Diferencia con absorción normal
| Señal | Qué buscar | Cuándo aparece |
|-------|-----------|----------------|
| **Absorción** | Wick largo + alto volumen en 1 vela | En cualquier momento |
| **Volumen de parada** | Primera vela con volumen elevado DESPUÉS de caída | Suelo de movimiento bajista |

---

## 6. VRVP — PERFIL DE VOLUMEN {#vrvp}

### Indicadores a usar (los DOS)
1. **"Perfil de volumen de la sesión"** — muestra el perfil de la sesión activa
2. **"Perfil de volumen de rango visible"** — muestra el perfil del rango visible en pantalla

> "Los dos" — Jorge los usa simultáneamente

### Configuración Exacta (confirmada de las imágenes)

**Pestaña Entradas de datos:**
| Parámetro | Valor |
|-----------|-------|
| Diseño de las filas | Número de filas |
| Tamaño de la fila | **180** (o 1000 — ambos usados) |
| Volumen | **Máximo** |
| Volumen del área de valor | **70** |

**Pestaña Estilo:**
| Parámetro | Valor |
|-----------|-------|
| Ancho (% del recuadro) | **16%** |
| Colocación | **Derecha** |
| VAH (Value Area High) | **Desactivado** visualmente |
| VAL (Value Area Low) | **Desactivado** visualmente |
| POC (Point of Control) | **Desactivado** visualmente |
| Developing POC | **Desactivado** visualmente |

> "4H no falla" — Jorge sobre el VRVP en temporalidad 4H

### Cómo usar el VRVP para entradas
- **POC (aunque desactivado visualmente):** La zona de mayor volumen = soporte/resistencia clave
- **Zona VAH:** Si el precio supera el VAH con volumen → continuación alcista
- **Zona VAL:** Si el precio cae al VAL con rechazo → soporte de compra
- **Vacíos de volumen:** Áreas donde el precio se mueve rápido (poca resistencia)
- Los retrocesos en tendencia alcista suelen coincidir con **zonas de alto volumen en el VRVP**

---

## 7. INDICADOR DE LIQUIDEZ {#liquidez}

### Configuración

| Activo | Threshold (Límite) |
|--------|-------------------|
| BTC | **10** (millones USD) |
| ETH | **10** (millones USD) |
| SOL | **1** |
| Altcoins pequeñas | **0.1** (con punto, NO coma) |
| Si mucha liquidez con 0.1 | Subir a **0.2** o **0.3** |

> "Solo cambiando ese numerito ya se arregla" — Jorge

### Uso en el análisis
- El precio **siempre va a buscar la liquidez** antes de moverse
- Zonas de liquidez alta = imanes para el precio
- Cuando el precio toca una zona de liquidez y rechaza → señal de entrada (ya absorbió)
- "El creador de mercado viola el soporte, toma la liquidez de los shorts y luego sube"
- Usar en combinación con OB y VRVP para confirmar zonas de entrada

---

## 8. ORDER BLOCKS (OB) {#ob}

### Definición
Zona donde los institucionales (smart money) han dejado órdenes sin ejecutar. El precio regresa a estas zonas para activarlas.

### Reglas de los OB según Jorge
- **OB FUERTES:** Solo desde **4H hacia arriba** (donde entran los "cracks")
- **OB en 1D:** La referencia principal; refinar la entrada en 4H
- **OB virgen:** OB que nunca ha sido tocado después de su creación = más poderoso
- **Proceso:** Buscar OB virgen en 1D → refinar la entrada en 4H → contar velas para entrada calculada

### Cómo identificar un OB
- La última vela bajista (o alcista) antes de un movimiento impulsivo fuerte
- Zona donde el precio hizo un quiebre de estructura
- Nivel que el precio ha respetado múltiples veces (zona de reacción)

### Estrategia de entrada con OB
1. Marcar OB virgen en 1D (o 4H)
2. Bajar a 4H (o 1H) para ver cómo se acerca el precio al OB
3. Contar velas desde el cruce EMA/inicio de rango
4. Si el precio llega al OB en la vela 7 del conteo → **entrada máxima convicción**
5. Entrar primer 20% en la zona del OB; siguiente 20% si el precio retrocede dentro del OB

---

## 9. RUPTURAS ESTRUCTURALES {#rupturas}

> Extraído de: `7. OPERACIONES JORGE/Quiebres (Rompimiento Estructuras)/Explicacion.txt`

### Cómo opera Jorge las rupturas
- Entrar con **porcentaje alto** de capital disponible
- **Salir rápido:** tomar ganancias en 30-50% mínimo, sacando el **90-95% de la posición**
- "Esas son operaciones de rupturas estructurales" — diferente al DCA normal

### Cuándo entrar por ruptura
- Cuando el precio intenta romper una resistencia importante con volumen
- Cuando hay una estructura que se rompe con vela envolvente alcista
- Ejemplo (19 dic 2023): Jorge entró por rompimiento de estructura cuando una orden no se activó y el mercado ya estaba arriba

### Imbalances (Gaps de Liquidez)
- Zonas donde el precio se movió rápido y no "llenó" (dejó gap)
- El precio tiende a volver a cerrar imbalances
- "Para que un gap se llene, el precio debe mantenerse por encima de los niveles clave"
- Si el precio viola el soporte, toma la liquidez y sube → **imbalance activo**

---

## 10. GESTIÓN DE CAPITAL Y DCA {#capital}

### División del Capital
```
CAPITAL TOTAL
├── 50% Capital Activo    → Posiciones abiertas
└── 50% Capital Reserva   → Para DCA y emergencias
```

### Sistema de 5 Partes (DCA)
> "20% 20% 20% 20% 20% — con mi regla de 5 partes y chao"

| Parte | % del capital activo | Cuándo entrar |
|-------|---------------------|---------------|
| 1ª | 20% | Primera señal (vela 7 o OB virgen) |
| 2ª | 20% | Si cae -3% desde entrada |
| 3ª | 20% | Si cae -7% desde entrada |
| 4ª | 20% | Si cae -12% desde entrada |
| 5ª | 20% | Si cae -20% desde entrada |

### Take Profit (TP)

**Regla real de Jorge:** "La descargo cuando esté en positivo >100% del margen. Resto con TP 1000%."
Con 5x apalancamiento: 100% retorno/margen = 20% movimiento de precio.

| TP | % precio | Retorno/margen (5x) | Porcentaje a cerrar |
|----|----------|---------------------|---------------------|
| TP1 | +5%  | 25% del margen  | 20% de la posición (lock-in temprano) |
| TP2 | +12% | 60% del margen  | 20% de la posición |
| TP3 | +22% | 110% del margen | 30% de la posición ("descargo en +100%") |
| TP_HOLD | indefinido | — | 30% restante — dejar correr hasta OB/resistencia mayor |

> "La descargo cuando esté en positivo >100% de margen, resto con TP 1000%"
> "No importa que suban más, pero vas asegurando"
> "Si se despegaron mucho de la entrada, stop a entrada" (mover SL a break-even cuando gana +12%)
> "Como se te ocurre cerrar a entrada" — NUNCA cerrar en negativo si el macro sigue alcista
> "No necesariamente tienes que esperar al 300%. Sí ves rechazo → cierras"

**Para rupturas estructurales (tipo B rápido):** cerrar 90-95% al primer 30-50%, no dejar correr.

### Apalancamiento
| Tipo de operación | Leverage |
|-------------------|----------|
| Swing (4H/1D) | 3x-5x |
| Scalping (15m-1H) | 5x-10x |
| DCA bajo convicción | 5x |

---

## 11. COBERTURA (HEDGE) ACTIVA {#hedge}

### Principio
No hay stop loss. Cuando el precio va en contra, se **abre una cobertura SHORT de 2x el LONG** para neutralizar pérdidas mientras se espera recuperación. Jorge es **98% LONG** — el short solo existe como protección.

> "Soy 98% long. Cuando hago short es en cobertura. Prefiero mil veces quedarme atrapado en un long que en un short."
> "En modo cobertura nunca vas a tener pérdida aunque se vaya 1000% en contra"

### Tamaño de la cobertura
**COBERTURA = 2x EL TAMAÑO DEL LONG**

> "Si tu long es de 100 USD, la cobertura debe ser de 200"
> Esto protege el long Y genera ganancia adicional con el movimiento bajista

### Cuándo abrir cobertura
**Ideal (manual):** Abrir en el TECHO — cuando el precio llega a una resistencia importante, breakout bajista, o zona de quiebre estructural.

**Automático (bot):** Precio cae -20% desde entrada + estructura 4H bajista confirmada.

> "El 3er error más grave es no abrir las coberturas en los quiebres"
> "dijo que metía cobertura si le bajaba 20 a 30% en contra la posición"
> "No abrir cobertura a los -7% — eso es demasiado agresivo"

### Proceso de cobertura
```
1. LONG activo → precio sube a resistencia / quiebre bajista
2. Abrir SHORT = 2x el margen del LONG (cobertura protege + genera ganancia)
3. Precio baja → SHORT gana, LONG pierde (se compensan)
4. Cerrar 80% del SHORT cuando gana +10% ("cobra 80% de lo que entre")
5. Dejar 20% corriendo hasta que squeeze vuelva alcista
6. Con SHORT cerrado → continuar DCA en LONG si es necesario
```

### Gestión avanzada de cobertura (para posiciones grandes)
> "Abrir una cobertura con el doble y ir descargando a medida que vaya subiendo 10% del margen donde se vea una resistencia buena, se cierra más el long, se recarga el short y se espera pacientemente"
> "Le va a tomar un par de días o mínimo dos semanas para que te vayan dando salidas — pero ambas en neta ganancias"

### Cuándo cerrar la cobertura
- Cerrar **80%** del SHORT cuando gana +10% ("cobra 80% de lo que entre")
- Cerrar el **20% restante** cuando Squeeze vuelve alcista
- NO cerrar la cobertura si el precio sigue bajando hacia OBs — el SHORT sigue protegiendo

### Cobertura en cascada (caída extrema)
Si el precio sigue cayendo después de la cobertura:
1. Si cae otro 20% → abrir nueva cobertura (mismo tamaño, 2x del LONG)
2. Si sigue cayendo → transferir capital de spot a futuros y repetir
> "Y si sigue cayendo mandas de spot a futuros y dale otra vez"

### Reglas avanzadas de cobertura (NUEVO — de imágenes COBERTURA)

**Límite del "doble trick":**
- La técnica de abrir cobertura con el doble solo funciona hasta **-5% a -10%** de caída
- Más allá de -10% → usar **igual % (1:1)** en lugar del doble
- "El truco de mandar el doble, solo funciona hasta 5-10% max. De ahí en adelante a 10x y coberturas de igual % — no del doble"

**Umbral para escalar hedge a 20x:**
- Las coberturas a 20X se abren **solo cuando el LONG ya lleva +300% de ganancia**
- "Las coberturas a 20X yo las comienzo cuando tengo el long con 300% de ganancias"

**La cobertura ocupa >50% de la cuenta:**
- Al desplegar cobertura completa se usa más del 50% del capital
- "Porque ocupo más del 50% de la cuenta haciendo eso"
- **NO abrir otras posiciones** mientras se está en modo cobertura activo

**Cuando las posiciones convergen (long y short en ganancia):**
- Cerrar ambas con **trailing stop**
- "Cuando ambas posiciones se acercan → cierro ambas con trailing stop"

**Recargar en rango (descarga/carga):**
- Descarga: 80% de la posición al llegar a soporte/resistencia clave
- Recarga: 10-15% en cada rebote; 2:1 o 3:1 en zonas importantes
- "Al llegar a un soporte o resistencias recargo 2a1 / 3a1 dependiendo"

**Pauta continuación alcista (pull al EMA55):**
- Precio cae a la EMA55 en timeframe pequeño → esto es FAKE-OUT antes de continuación alcista
- "Una zona para acumular más y sacar a la gente que viene de abajo haciendo creer que se va a 0"
- En 15M pierde la EMA55 → buscar en 30M, si aguanta → LONG fuerte

### Limitaciones
- **Martingale funciona en LONG, NO en SHORT**: "Es que una martingale en Long funciona. En short no — porque en short no tienes techo"
- No debería necesitar más de 5 recompras (DCAs) en ningún trade

> "Cuando estás tradeando algo seguro no un meme, no importa el número en negativo"

---

---

## 11b. JUGADAS INSTITUCIONALES — PATRONES REALES {#institucional}

### Validación institucional de los indicadores
> "Fidelity ocupa lo mismo que nosotros: EMA10-55, Soporte, resistencia, Smart Money, perfil de volumen"
> "Operan igual que Jorge, la única diferencia es que tienen mucha más plata, recursos ilimitados"

Los indicadores de Jorge NO son retail — son exactamente los que usan los institucionales. Esto confirma que seguir estas señales es estar alineado con el flujo real de dinero.

### Cómo operan los institucionales
- **Venden futuros en resistencia** para hacer caer el precio artificialmente
- **Compran spot en el retesteo** cuando retail entra en pánico
- "Ellos solo vendieron futuros y volvieron a comprar. En el retesteo venden el spot"
- Esto explica por qué las rupturas parecen "falsas" antes de explotar

### Dominancia de BTC como filtro para ALTCOINS (NUEVO — confirmado OCR)
> "Dominancia de BTC Bajista en: 1min, 5min, 15min, 30min → apenas para que las alts empiecen a subir"

**Filtro para operar altcoins:**
- Si BTC dominance está bajando en MÚLTIPLES timeframes pequeños (1m, 5m, 15m, 30m simultáneamente) → favorable para abrir longs en alts
- Si BTC dominance está subiendo → el dinero va de alts a BTC → NO operar alts long

**Ciclo macro completo (tabla "Tenerlo en cuenta siempre"):**
| BTC Precio | ALTS | Dominancia BTC | Fase |
|-----------|------|----------------|------|
| Sube | Sube | Baja | Fase Altseason |
| Sube | Baja | Sube | Fase de Dump de Alts |
| Lateraliza | Sube | Baja | Altseason tardía |
| Lateraliza | Baja | Sube | Fase de Acumulación |
| Baja | Baja mucho | Sube | Fase de Dump total |
| Baja | Lateraliza | Sube | Fase de Acumulación |

**Ciclo secuencial altseason:**
BTC sube → BTC corrige + ETH sube → ETH baja → ALTS explotan
> "ETH baja y las altcoins comienzan a subir y explotar — así ha ocurrido siempre"

### Horario institucional clave
- **Chicago time 4–6 PM = ventana de acumulación institucional**
- Causan caídas de precio en ese horario para comprar barato
- "Cuando terminen de comprar lo van a mandar pa arriba de una sola vela"
- Los lunes institucionales compran BTC (sesgo alcista lunes)

### Timeframe oculto: 2H
- Los institucionales usan **EMA10 en 2H** para sus entradas
- "Nadie ve ese [2H] — solo ven 1H, 4H y 1D"
- Cuando el precio retrocede a EMA10 en 2H → señal de alta calidad (pocas personas la ven)

### Cada máximo se retestea (regla)
- **"Cada vez que marca un máximo lo retestea por ley"**
- Nunca entrar en breakout puro → esperar el retesteo del nuevo máximo
- "Rompe, apoya, sube" — break + retest holds + continuation

### Los stop loss del retail = combustible
- Las órdenes de stop de retail están todas en los mismos niveles obvios
- El precio los "caza" antes del movimiento real
- No colocar SL en niveles redondos ni en mínimos/máximos evidentes
- "Viola el soporte, toma la liquidez de los shorts y luego sube"

### Vacíos de liquidez (liquidity voids)
- Un rally parabólico sin pullbacks deja **vacíos de liquidez hacia abajo**
- "Esta dejando varios de liquidez a la baja. Así que mosca, así como sube así cae"
- El precio volverá a llenar esos vacíos a la misma velocidad que subió
- Subida sana = precio crea soportes en cada escalón (no velas verdes consecutivas)

### ETF y on-chain
- Ventas de Grayscale/ETF son ruido orquestado para acumular barato
- Glassnode (on-chain): monitorear disponibilidad de BTC en OTC
- "Se acabaron los BTC en OTC y reventaron las compras en Coinbase" → precio explota

---

## 11c. MODO SCALPING POR RANGO {#scalping_rango}

> "Detecto un rango y a darle"
> "Pongo unas 20 órdenes en diferentes monedas detectando un rango en ellas"
> "La primera tanda se tardó 50 minutos — de 10 a 50"

Este es el modo de operación más rápido de Jorge — diferente al swing con DCA. Se opera la oscilación dentro de un rango identificado.

### Condiciones para entrar en modo scalping por rango
1. Precio en un rango lateral claro (no en tendencia)
2. Identificar soporte y resistencia del rango en 1H o 4H
3. OB virgen dentro del rango (zona de reacción)
4. No requiere tantos argumentos — el rango mismo es la señal

### Ejecución
- Entrar al **1% de la cuenta** en el soporte del rango
- Seleccionar **3 a 5 recompras** de **-1.6% cada una** (dentro del rango)
- TP: resistencia del rango → cerrar **50-100% de la posición**
- Si el precio rompe el rango a la baja → dejar caer + esperar OB importante abajo
- "Si se sale del rango déjalo caer si vas en long — dependiendo de cuántas recompras tengas"

### Regla del 0.1% vs 1%
| Situación | Tamaño de entrada |
|-----------|------------------|
| No hay soporte/rango claro | 0.1% de la cuenta |
| Soporte identificado pero no OB virgen | 1% de la cuenta |
| OB virgen + absorción importante | 1-2% de la cuenta |
| Zona virgen de altísima convicción | hasta 5% |

> "Con el 1% es si identificas el rango. Si no hay soporte o rango entonces 0.2%"

### Modo multi-par (Jorge avanzado)
Jorge opera varias monedas simultáneamente en modo rango:
- Detectar rango en 5-20 monedas diferentes
- Colocar órdenes límite en cada soporte de rango con TP automático
- Las operaciones se abren y cierran solas (sin monitorear activamente)

---

## 12. PROCESO DE ANÁLISIS TOP-DOWN {#topdown}

### Layout de TradingView (3 ventanas)
```
IZQUIERDA: 1D (análisis macro)
CENTRO:    4H (análisis principal)
DERECHA:   1H (afinación entrada)
```

### Jerarquía completa de temporalidades para intradia
> "Solo debes de darle seguimiento a todos los gráficos desde 15M a 4H"
> "Hablo de 15, 30, 1, 2 y 3H"
> "No te fijes solo en 1H, sino en 2 y 3H — con eso sacas la definición del de 4H"
> "1H es pa entrar y salir sin sentimientos"

| Timeframe | Rol en intradia |
|-----------|----------------|
| 4H | Marco de referencia institucional — estructura macro del día |
| 2H + 3H | Definen la tendencia del 4H sin tener que esperar el cierre de 4H |
| 1H | Entrada y salida — confirmación directa de la operación |
| 30M | Ver el cambio de estructura en detalle |
| 15M | Ver el timing exacto — horizonte 3 horas |

**Flujo de intradia:**
1. Revisar 4H: ¿estructura alcista? ¿en qué vela del conteo?
2. Revisar 2H y 3H: confirman o contradicen el 4H
3. Entrar en 1H: señal de entrada con EMA10/55 + squeeze + absorción
4. Afinar en 15M-30M: para timing más exacto de la vela

### Secuencia diaria de análisis (15 minutos)

#### Mañana — Análisis Macro (1D)
1. ¿EMA10 > EMA55? → sesgo alcista
2. ¿Precio alejado >3% de EMA10? → esperar, no entrar
3. ¿EMAs comprimidas? → preparar; movimiento próximo
4. ¿VRVP muestra zonas de soporte/resistencia clave?
5. Anotar nivel de EMA55 en 1D (soporte/resistencia principal del día)

#### Durante el día — Análisis Intermedio (4H)
1. ¿En qué vela del conteo estamos?
2. ¿El Squeeze Momentum está en verde y subiendo?
3. ¿Hay absorción en volumen (mecha + alto volumen)?
4. ¿Precio cerca de OB virgen?
5. ¿ADX muestra tendencia (≥21) o rango (<21)?
6. Si vela 5-8 + compresión + squeeze verde + ADX tendencia → **preparar entrada**

#### Entrada (1H + confirmación 15m)
1. Verificar los 10 ARGUMENTOS
2. Precio cerca de EMA55 en 1H = zona de rebote ideal
3. EMA15/EMA30 en 1H muestran cambio de estructura alcista
4. Squeeze OFF con histograma positivo
5. Entrar primer 20% del capital planificado
6. Colocar TP1, TP2, TP3

---

## 13. TABLA DE SEÑALES EXACTAS {#senales}

### Señales de ENTRADA LONG

| Señal | Condiciones requeridas | Timeframe | Tipo |
|-------|----------------------|-----------|------|
| **LONG MÁXIMA CONVICCIÓN** | EMA10>EMA55 + vela 7 + EMAs comprimidas + Squeeze OFF alcista + OB virgen + volumen | 4H + 1H | A |
| **LONG ESTÁNDAR** | EMA10>EMA55 + cruce alcista + Squeeze positivo + volumen sobre promedio + no sobreextendido | 4H | B |
| **LONG REBOTE EMA55** | Precio toca EMA55 (4H) + mecha larga bajista + absorción en volumen + Squeeze no bajista | 4H | C |
| **LONG 4TO TOQUE** | Precio llega al nivel que fue resistencia 3 veces → 4to toque = entrada directa | 4H/1H | C |
| **LONG RUPTURA** | Precio rompe resistencia con volumen alto + EMA10>EMA55 + Squeeze OFF alcista | 4H | B (salida rápida) |
| **LONG IMPULSO SQUEEZE** | Histograma verde oscuro bajo cero acercándose a 0 sin cruzar | 4H | B |

### Señales de SALIDA / SHORT

| Señal | Condiciones requeridas | Timeframe | Tipo |
|-------|----------------------|-----------|------|
| **SHORT / COBERTURA** | 12 velas sin superar resistencia + Squeeze bajista + EMA10 aplanándose | 4H | Cobertura |
| **SALIR LONG** | EMA10 cruza bajo EMA55 | 4H/1D | Salida total |
| **ALERTA PELIGRO** | Precio >3% sobre EMA10 en 1D (sin volumen) | 1D | No entrar |
| **DISTRIBUCIÓN** | Máximos más bajos dentro del rango + Squeeze rojo + ADX bajo | 4H | Abrir cobertura |

### Señales de ALERTA (preparar)

| Señal | Qué hace |
|-------|----------|
| Compresión iniciada (EMA10/55 acercándose) | Preparar órdenes; movimiento próximo |
| Squeeze ON (puntos negros) | Acumulación activa; NO entrar aún |
| Vela 7 alcanzada en conteo | Revisar todos los argumentos; entrada inminente |
| Momentum cruza cero al alza | Cambio de sesgo a alcista; confirmar con EMAs |
| Momentum cruza cero a la baja | Proteger posiciones largas |

---

## 14. GESTIÓN DE RIESGO — REGLAS ABSOLUTAS {#riesgo}

### Lo que NUNCA hacer
❌ Entrar cuando precio alejado >3% de EMA10 en 1D
❌ Ignorar análisis macro y operar solo en 15m
❌ Poner SL fijo (usa cobertura en su lugar)
❌ Cerrar posición con pérdida sin verificar macro
❌ Operar ALTs cuando BTC está en rango sin dirección
❌ Entrar por FOMO cuando ya subió y no hay señal
❌ Ignorar el volumen (subida sin volumen = trampa)
❌ Operar rupturas sin volumen de confirmación
❌ Abrir posición completa en la primera entrada
❌ Entrar contra tendencia macro (1D/1S)
❌ Abrir short directional sin weekly + monthly EMA ambos bajistas
❌ Usar EMAs en timeframes menores a 15M
❌ Ignorar vacíos de liquidez debajo del precio (rally sin pullbacks = peligro)
❌ Entrar en breakout sin esperar el retesteo ("rompe apoya sube")
❌ Abrir otras posiciones mientras cobertura activa usa >50% de la cuenta
❌ Usar "doble trick" en coberturas cuando caída supera -10% (usar 1:1 en su lugar)

### Gestión de posición activa
```
Posición abierta → revisión diaria:
1. ¿Análisis macro sigue válido? (EMA10 > EMA55 en 1D)
2. ¿Squeeze sigue positivo en 4H?
3. ¿Precio respetando EMA55 en 4H?

→ SÍ a las 3: mantener posición, aplicar DCA si hay niveles de rebote
→ NO a alguna: evaluar cobertura o reestructurar
```

---

## 15. PSICOLOGÍA Y MINDSET {#psicologia}

### Principios de Jorge

> "No compitas con nadie. No mires relojes ajenos. Cada quien va a su ritmo o como pueda."

> "Acá lo importante no es si ganas o no empezando. Acuérdate que estás probando algo que es nuevo para ti. No te dejes llevar por el FOMO."

> "Aplicando al 100% la estrategia vas a lograr el objetivo cual es ser rentable con el tiempo."

> "No es que te vas a ganar mañana lo de un carro ni nada por el estilo."

> "Solo me va a tomar más tiempo de lo normal. Pero yo tengo paciencia."

### Reglas mentales de operación
1. Un trade perdedor no invalida la estrategia — verificar si se siguieron los 10 argumentos
2. Si estás dudando, el análisis macro no está claro → no entrar
3. La operación con cobertura se puede mantener indefinidamente mientras el proyecto sea sólido
4. No operar en fines de semana (bajo volumen, movimientos no confiables)
5. Los lunes institucionales compran BTC → sesgo ligeramente alcista al inicio de semana
6. **"Yo dejo órdenes y me acuesto a dormir"** — colocar límites en zonas calculadas, no babysitear
7. **"El miedo no factura"** — el capital tiene que trabajar aunque tú duermas
8. **"No debes tener apuro en ganar. Si tienes apuro lo perderás todo"** — paciencia es la ventaja
9. **FOMO**: "Aveces me domina el fomo. Con 1 operación que haga se me pasa" — un buen trade borra el fomo
10. **"Todo el mundo metiendo short donde no se mete short"** = señal contrarian; no seguir la multitud

### Errores más graves (según Jorge)
1. No salir de altcoins o proteger la entrada cuando hay ganancias abiertas
2. Usar **demasiado % por operación** (oversize)
3. **No abrir coberturas en los quiebres** — el 3er error más grave
4. Entrar en la 2da señal cuando ya se perdió la 1ra, por FOMO

---

## 16. CONFIGURACIÓN TRADINGVIEW {#tradingview}

### Indicadores a instalar
1. **`05_TRADINGVIEW_PINE_SCRIPT.pine`** — EMA10/55/200 + señales + tabla (overlay)
2. **`06_TRADINGVIEW_SQUEEZE_MOMENTUM.pine`** — Panel Squeeze Momentum (panel inferior)
3. **SQZMOM & ADX** — Buscar en TradingView Community Scripts
4. **Volume Profile (VRVP)** — "Perfil de volumen de rango visible" (nativo TradingView)
5. **Volume Profile Session** — "Perfil de volumen de la sesión" (nativo TradingView)
6. **Indicador de Liquidez / VSRA** — Buscar en Community Scripts

### Config rápida del VRVP
```
Entradas: Filas=180, Volumen=Máximo, Área valor=70
Estilo: Ancho=16%, Colocación=Derecha, VAH/VAL/POC/DevPOC=OFF visualmente
```

### Config del Indicador de Liquidez
```
BTC/ETH: Threshold = 10
SOL: Threshold = 1
Altcoins pequeñas: Threshold = 0.1 (punto, no coma)
```

### Alertas mínimas recomendadas (configurar en 1D, 4H y 1H)
1. `🟢 LONG FUERTE` — señal de entrada principal
2. `🔀 Cambio Estructural ALCISTA` — inicio de nuevo ciclo
3. `⚡ Compresión de EMAs Iniciada` — prepararse para entrada
4. `⚡🟢 Squeeze Liberado ALCISTA` — disparo final de confirmación
5. `🔴 SHORT / COBERTURA` — protección de posición

---

## RESUMEN EJECUTIVO — FLUJO DE DECISIÓN

```
¿EMA10 > EMA55 en 1D?
    └── NO → No abrir longs nuevos; evaluar cobertura si posición activa
    └── SÍ → Continuar análisis ↓

¿Precio alejado >3% de EMA10 en 1D?
    └── SÍ → Esperar corrección; no entrar
    └── NO → Continuar análisis ↓

¿Squeeze Momentum positivo en 4H?
    └── NO → Esperar; monitorear
    └── SÍ → Continuar análisis ↓

¿En qué vela del conteo estamos?
    └── <5: Esperar
    └── 5-8: Zona de entrada (evaluar argumentos)
    └── >12: Compresión fallida si no superó resistencia → SHORT

¿Cuántos de los 10 ARGUMENTOS están a favor?
    └── <5: No entrar
    └── 5-7: Entrar con 20% del capital planificado
    └── 8-10: LONG FUERTE — entrar con 40-60% inicial

ENTRADA → Primer 20% → TP1 (+5%) → TP2 (+12%) → TP3 (+22%, descargo en +100%/margen) → 30% corre indefinidamente
```

---

## RESUMEN DE INSIGHTS CLAVE — IMÁGENES TELEGRAM (Mayo 2026)

### Capital y sizing
- Futuros = **20% del capital total**; dividido en **5 partes iguales de 20%**
- Con 0.1% por entrada: "no importa que caiga -17% en un día" — tamaño pequeño = aguantar sin estrés
- Cuando ves absorción importante: **recomprar con 1-2% de la cuenta** ("no puedes quedarte con 0.3-0.6%")
- "Se supone que aguantamos más de 1 semana tragándonos una caída y recomprando"

### TPs y gestión activa
- TP real: **100% retorno sobre margen** = descarga principal (con 5x leverage = +20% precio)
- "La descargo cuando esté en positivo >100%, resto con TP 1000%"
- "Si se despegaron mucho de la entrada, stop a entrada" (mover SL a break-even)
- "Como se te ocurre cerrar a entrada" — Jorge no acepta cerrar en empate cuando el macro es alcista
- "Ve cerrando algunas, No importa que suban más, Pero vas asegurando"
- Para rupturas: cerrar **30-50% mínimo** (operaciones de ruptura = salir corriendo)

### Cobertura (actualizado)
- **Cobertura = 2x el LONG** ("Si long es 100 USD → SHORT debe ser 200")
- Abrir en TECHO/quiebre, NO a los -7% de pérdida
- "Cobra 80% de lo que entre" → cerrar 80% primero, dejar 20% corriendo
- Martingale funciona en LONG, **NO funciona en SHORT** (sin techo)
- Jorge: "Soy 98% long. Cuando hago short es en cobertura. Prefiero mil veces quedarme atrapado en long"

### Errores más comunes que Jorge señala
1. No salir de altcoins o proteger la entrada cuando hay ganancias
2. Usar demasiado % por operación (position sizing excesivo)
3. **No abrir coberturas en los quiebres** (3er error más grave)
4. Entrar en la 2da señal en lugar de la 1ra o esperar la 3ra

### Análisis multi-temporalidad
- "Análisis en gráficos perpetuo es de 4H hacia abajo, y gráfico 1D hacia arriba sirve el de Spot"
- Jorge usa 4H a 12H (incluyendo 6H) para sus análisis
- "1H es pa entrar y salir sin sentimientos"
- "No te fijes solo en 1H, sino en 2 y 3H — con eso sacas la definición del de 4H"

---

## 17. MODO BULLRUN — ESPECULACIÓN PURA {#bullrun}

> "De aquí para adelante es mera especulación todo. No hay análisis técnico ni fundamental que valgan. Ni macro ni nada."
> — Jorge, cuando BTC entra en territorio de precio nunca visto

### Características del modo BullRun
- Cuando BTC supera ATH y entra en precio desconocido, el TA tradicional pierde relevancia
- El precio puede separarse masivamente de la EMA10 semanal — **esto no es señal de venta**
- El análisis técnico no puede proyectar objetivos: no hay zona de resistencia histórica
- Operadores de YouTube que dan precios objetivo en BullRun son especuladores, no analistas
- La estrategia de EMA10/55 sigue válida para entradas y DCA, pero los TPs se expanden

### Comportamiento en BullRun
- Entrar en correcciones a EMA10 (no esperar EMA55 — la corrección no llega tan lejos)
- TPs: mover radicalmente hacia arriba — el TP 1000% del margen cobra sentido total
- No cerrar posición completa: "Acuérdate nunca cerrar completo"
- Las coberturas en BullRun se hacen con % mínimo (5-10%) solo en resistencias clave
- Los eventos mediáticos causan **sell the news**: el precio baja cuando la noticia llega

### Regla Sell The News — Eventos Anuales
> "Desde que tengo razón en el mundo cripto — en todos los eventos anuales que hacen, se desploma esa verga"
> — Jorge sobre Bitcoin Conference, ETF approvals, halvings

**Regla operativa:** En eventos mediáticos grandes (conferencias BTC, aprobaciones ETF, halvings):
1. El precio sube anticipando el evento (comprar el rumor)
2. El día del evento: **el precio se desploma** (vender la noticia)
3. Acción: reducir exposición (no salir completo) antes del evento o abrir cobertura corta

---

## 18. MECÁNICA DEL MARKET MAKER {#market-maker}

> "El exchange no lo tumba de golpe. Solo lo mantiene para que le puedan comprar. Crean una escalera en el precio y van vendiendo poco a poco. Es la única forma de convencer a los demás."
> — Jorge sobre distribución institucional

### Escalera de Distribución
Cuando un market maker (institución, exchange) quiere salir de posición masiva:
1. **Sube el precio gradualmente** — creando una "escalera" (niveles de resistencia sucesivos)
2. **Vende en cada escalón** — a medida que el retail compra cada subida
3. **El retail interpreta** la escalera como "sigue subiendo, compro más"
4. **Cuando el MM tiene vendida su posición** → deja caer el precio sin soporte
5. El retail queda atrapado en la parte alta

### Cómo identificar la escalera de distribución
- Múltiples toques a la EMA10 desde abajo (debilitamiento progresivo)
- Subidas sin volumen genuino (el MM vende mientras el precio sube)
- Cada nuevo máximo es apenas un poco mayor que el anterior
- Argumento A8 del sistema: **alerta de distribución** = penaliza el score

### Dos tipos de caída de precio
1. **Caída por creador externo**: caída de golpe, panic sell, recupera rápido
2. **Caída por creador del exchange**: escalera controlada, lenta, metódica — más peligrosa

### Aplicación práctica
- Ver escalera de distribución → **no entrar**; esperar que termine la distribución y el precio llegue al soporte
- Si ya estás en posición → cobertura parcial (10-20% SHORT)
- La señal de fin de distribución: Squeeze se libera alcista + volumen de absorción genuino

---

## 19. REGLAS OPERATIVAS FINALES {#reglas-finales}

### "Nunca cerrar completo"
> "Acuérdate nunca cerrar completo" — Jorge tras ver un LONG de SOL +998%

La regla aplica siempre, independientemente del PnL:
- TP1 → cerrar 20%
- TP2 → cerrar 20%
- TP3 (100%+ retorno/margen) → cerrar 30%
- **El 30% restante se deja correr con TP en 1000% del margen**
- Aunque el precio siga subiendo 5x más, el 30% está trabajando
- "No tiene lógica tener una operación en +1000% y haberla cerrado en +100%"

### Modo Cobertura — Ganancia Garantizada
> "En modo cobertura nunca vas a tener pérdida porque así se te vaya en contra 1000%, siempre tu posición ganadora va más cargada. Prácticamente con lo ganado se cubre la pérdida más un % a tu favor."
> — Jorge

Mecánica:
1. LONG cae → abrir SHORT (2x el LONG)
2. SHORT gana → crece más rápido que lo que pierde el LONG
3. Cerrar 80% del SHORT cuando SHORT = +10% → capturar ganancia
4. Con esa ganancia del SHORT: **recargar el LONG** (comprar más abajo)
5. El 20% del SHORT restante: **protegerlo a breakeven**
6. Resultado: LONG promediado más abajo + SHORT protegido = siempre hay un lado ganador

> "Recompras y ganas en ambas" — al cerrar SHORT con ganancia y recargar LONG

### Scalping en Rango — Modo Avanzado (Long+Short simultáneo)
Para operar rangos con alta convicción de los límites:
1. Identificar rango confirmado (soporte y resistencia claros)
2. Abrir **LONG en soporte** + **SHORT en resistencia** simultáneamente
3. Con TP pre-colocado en cada uno:
   - Si sube → LONG cierra con TP, SHORT queda flotando
   - Si baja → SHORT cierra con TP, LONG queda con recompras
4. Alternativa: **Trailing stop 1.2%** en ambas posiciones
5. Jorge operaba 20 pares simultáneos en este modo ("10 a 50, 50 operaciones ganando así sea 1$")

### Retrocesos en Tendencia Alcista — Target DCA
> "Los retrocesos en tendencia alcista es hasta la EMA10"

En tendencia alcista fuerte (BullRun o impulso estructural):
- Los retrocesos normales no llegan a EMA55 — solo tocan EMA10
- DCA target principal: **EMA10** del timeframe operado
- Si el precio pasa la EMA10 y va hacia EMA55 → tendencia más débil, recargar en EMA55
- Si pasa EMA55 → revisar argumentos de entrada (posible invalidación)

### Ruptura Estructural — Operación de Alta Convicción
> "Rompimiento quiebre de estructura bajista a alcista: long a 80% de la cuenta, 100% seguro. 51.54% fuera el 95% del margen"
> — Jorge tras operar quiebre estructural en BTC

Condiciones para ruptura de alta convicción:
1. Quiebre confirmado (no breakout falso) de estructura bajista en 4H/1D
2. OB en la zona de ruptura que da soporte
3. Volumen de confirmación

Acción: **entrar con 80% del capital de futuros** (no el 20% normal)
- Cerrar **90-95% del margen** en el primer movimiento (30-50% de ganancia)
- Operación rápida, no hold

---

*Sistema compilado de todos los materiales del mentor Jorge (DigitalCapitalsTrading) — imágenes, textos, Excel y conversaciones — Mayo 2026*
