# REGLAS DE ENTRADA Y SALIDA — SISTEMA JORGE

## CHECKLIST PRE-ENTRADA

Antes de abrir cualquier posición, verificar TODOS estos puntos:

### Análisis Macro (1D / 1S)
- [ ] ¿La tendencia mayor por EMAs es alcista?
- [ ] ¿El precio NO está excesivamente alejado de EMA10? (>3% en 1D = esperar)
- [ ] ¿Hay compresión de EMAs en curso? (señal de inminencia)
- [ ] ¿El precio está sobre la EMA55 en 1D? (si no → modo defensivo)

### Análisis Intermedio (4H / 12H)
- [ ] ¿Las EMAs en 4H confirman la dirección macro?
- [ ] ¿Estamos en vela 5-7 del conteo de 12 velas?
- [ ] ¿Hay zona de soporte/resistencia clave coincidente?
- [ ] ¿El volumen muestra absorción o acumulación?

### Análisis de Entrada (1H / 15m)
- [ ] ¿El Squeeze Momentum está en cuadrante alcista (verde)?
- [ ] ¿El precio tocó la EMA55 en esta temporalidad?
- [ ] ¿Hay mecha de absorción visible con volumen?
- [ ] ¿Todos los timeframes apuntan en la misma dirección?

---

## REGLAS DE ENTRADA — LONG

### Entrada Tipo A (Máxima Convicción)
**Condiciones:**
- Tendencia alcista en 1D/1S
- EMAs comprimidas en 4H
- Precio en soporte (EMA55 en 4H o nivel S/R mayor)
- Vela 7 del conteo de 12 velas
- Squeeze momentum alcista en 1H

**Acción:** Entrar el 20% inicial de la posición planificada

### Entrada Tipo B (Alta Convicción)
**Condiciones:**
- Cambio estructural confirmado por cruce EMA10/EMA55
- Precio en mecha de absorción (long wick bajista con cierre alcista)
- Velas 5-7 del conteo

**Acción:** Entrar el 20% inicial

### Entrada Tipo C (Contra Tendencia — Rebote)
**Condiciones:**
- Tendencia bajista macro pero en zona de soporte mayor (EMA55 1D)
- Absorción evidente con volumen destacado
- Configuración de 12 velas alcista en 15m-1H

**Acción:** Entrar 10% (posición reducida por mayor riesgo)

---

## REGLAS DE SALIDA — TAKE PROFIT

**Regla maestra de Jorge:** "La descargo cuando esté en positivo >100% del margen. Resto con TP 1000%"
Con 5x leverage: 100% retorno/margen = 20% movimiento de precio

### TP1 (+5% precio = 25% retorno/margen) — cerrar 20%
- Lock-in temprano para asegurar que la operación no sea pérdida
- EMA55 en temporalidad de entrada (15m o 1H)
- "Si ves rechazo → cierras" — no esperar niveles fijos si hay señal clara

### TP2 (+12% precio = 60% retorno/margen) — cerrar 20%
- EMA55 en 1H o resistencia horizontal clara
- Cerca del máximo anterior del rango
- "Si se despegaron mucho de la entrada, stop a entrada" → mover SL a break-even aquí

### TP3 (+22% precio = 110% retorno/margen) — cerrar 30% ("descargo en +100%")
- Zona de distribución: precio alejado de EMA10 en temporalidad mayor
- Absorción en la parte alta (wick alcista importante)
- Vela envolvente bajista con volumen en resistencia

### TP Final / Hold — 30% restante corre indefinidamente
- Colocar TP al 1000% del margen y dejar correr
- Solo cerrar si estructura se invalida o hay absorción clara en techo
- "No tiene lógica tener operación -1000% y cerrarla en 100%"

### Regla especial para rupturas estructurales
- Cerrar **90-95% en el primer 30-50% de ganancia**
- Operación de ruptura = salida rápida, no hold

---

## REGLAS DE STOP LOSS

Jorge NO usa SL convencional. Pero los parámetros de invalidación son:

### Invalidación de LONG
- Precio cierra en cuerpo por DEBAJO de la EMA55 en 1D
- Las EMAs hacen cruce bajista (EMA10 cruza abajo la EMA55) en 4H
- La "teoría de 12 velas" falla: 12 velas pasan y el precio NO volvió al máximo previo
- El rango hace mínimos cada vez más bajos + múltiples toques a la EMA10 (debilitándola)

**En ese caso:** Aplicar cobertura (SHORT) en vez de cerrar el LONG

### Invalidación de SHORT
- Precio cierra en cuerpo por ENCIMA de la EMA10 en el timeframe operado
- EMA10 cruza alcista la EMA55
- La absorción bajista es seguida de mayor absorción alcista

---

## NIVELES DE RECOMPRA (DCA)

Para una posición de 100 USDT con 5X de apalancamiento en BTC:

| Entrada | % del capital | Condición |
|---------|---------------|-----------|
| 1ra (inicial) | 20% | Zona clave + vela 7 |
| 2da recompra | 20% | Siguiente soporte (EMA55 1H) |
| 3ra recompra | 20% | Siguiente soporte (EMA55 4H) |
| 4ta recompra | 20% | OB importante en 1D |
| 5ta recompra | 20% | OB mayor o EMA55 en 1S |

**Máximo de recompras por posición:** Hasta que el precio llegue al siguiente OB estructural mayor.

---

## GESTIÓN DE POSICIÓN ACTIVA

### Si el precio va a tu favor (>30% en ganancias)
1. Cobrar parciales en TPs pre-definidos
2. Mover SL psicológico a breakeven
3. Dejar correr el resto con TP lejano

### Si el precio va en contra (-100% a -300%)
1. Esperar sin cerrar
2. Revisar si los argumentos de entrada siguen válidos
3. Si hay zona de recompra válida → añadir posición

### Si el precio va muy en contra (-600% a -1000%)
1. Esperar hasta el OB importante
2. Aplicar cobertura (SHORT) para neutralizar
3. La descarga del SHORT financia el resto del LONG
4. Solo cuando el SHORT esté en >100% positivo → descargarlo y esperar que el LONG recupere

---

---

## REGLAS INTRADIA — TEMPORALIDADES Y TIMING

### Jerarquía temporal para intradia
1. Revisar **4H** — estructura macro del día (¿alcista? ¿vela del conteo?)
2. Revisar **2H y 3H** — definen la tendencia del 4H sin esperar cierre completo
3. Entrar en **1H** — señal directa de entrada
4. Afinar en **15-30M** — timing exacto (horizonte 3 horas)

> "1H es pa entrar y salir sin sentimientos"
> "No te fijes solo en 1H, sino en 2 y 3H — con eso sacas la definición del de 4H"

### Horizonte de holding por timeframe
- **15M** → esperar resultado en ~3 horas
- **1H** → esperar resultado en 8-12 horas
- **4H** → esperar resultado en ~72 horas (3 días)
- NO cerrar antes del horizonte si el análisis sigue válido

### Señal de Volumen de Parada (suelo potencial)
1. Caída de 3+ velas consecutivas bajistas
2. Aparece primera vela con **volumen alto** (>1.5x promedio)
3. El precio no hace nuevo mínimo en las 2-3 velas siguientes
4. → **Recomprar con 1-2% de la cuenta** (no quedarse con 0.1%)

### Tamaño de entrada según contexto
| Situación | Tamaño |
|-----------|--------|
| No hay rango/soporte claro | 0.1-0.2% |
| Soporte identificado | 1% |
| OB virgen + absorción | 1-2% |
| Volumen de parada en OB virgen | 2% (entrar fuerte) |

### Filtro de dominancia BTC para altcoins
Antes de entrar en una altcoin:
- Verificar si BTC dominance está bajando en 1m, 5m, 15m, 30m simultáneamente
- Si dominancia bajando → verde para alts
- Si dominancia subiendo → esperar, el dinero va a BTC

---

*Las reglas de entrada sin convicción (dudando, FOMO) = no entrar.*

---

## REGLAS DE CIERRE — NUNCA CERRAR COMPLETO

> "Acuérdate nunca cerrar completo" — Jorge

**Regla universal:** Siempre dejar al menos el 30% corriendo:
| Nivel | Cierre |
|-------|--------|
| TP1 (+5%) | 20% de la posición |
| TP2 (+12%) | 20% |
| TP3 (+22%, 100%+ retorno/margen) | 30% |
| Resto | Dejar con TP 1000% del margen |

Esta regla aplica incluso si "parece que ya no va a subir más". El 30% restante es el seguro de no perderse el movimiento explosivo.

---

## RUPTURA ESTRUCTURAL — OPERACIÓN ESPECIAL

**Cuándo:** Quiebre confirmado de estructura bajista → alcista en 4H o 1D

**Condiciones:**
1. Cierre de vela **por encima** del máximo previo (no solo mecha)
2. Volumen alto en la vela de ruptura
3. OB o soporte en la zona de quiebre que valida el nivel
4. EMA10 > EMA55 en el timeframe inmediato superior

**Acción:** Entrar con **80% del capital de futuros** (excepcional vs. el 20% normal)
- TP: cerrar el **90-95% en el primer +30-50% de ganancia**
- Operación rápida — no hold extendido
- Cobertura: NO necesaria (la ruptura se vende si sale mal, no se cubre)

---

## REGLA SELL THE NEWS — EVENTOS ANUALES

> "Desde que tengo razón en el mundo cripto — en todos los eventos anuales que hacen, se desploma esa verga" — Jorge

**Filtro de eventos macro:**
- Bitcoin Conferences, aprobaciones de ETF, halvings, anuncios regulatorios
- El precio sube **anticipando** el evento ("comprar el rumor")
- El día del evento: **vender la noticia** = reducir exposición

**Acción operativa:**
- 48-72h antes del evento grande: tomar parciales o abrir cobertura SHORT (10-20%)
- El día del evento: no aumentar posición
- Después del dump: oportunidad de DCA en soporte clave

---

## RETROCESOS EN TENDENCIA ALCISTA FUERTE

> "Los retrocesos en tendencia alcista es hasta la EMA10" — material OCR

En impulso alcista fuerte (BullRun o ruptura reciente):
- Los retrocesos normales **no llegan a EMA55** — solo tocan EMA10
- DCA target primario: **EMA10** del timeframe operado
- Si pasa EMA10 y llega a EMA55 → tendencia más débil, DCA en EMA55
- Si precio cierra por debajo de EMA55 → revisar argumentos (posible invalidación)
