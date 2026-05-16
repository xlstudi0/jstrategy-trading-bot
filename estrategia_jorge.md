# 📊 ANÁLISIS COMPLETO — ESTRATEGIA DE TRADING "JORGE MENTOR"

> **Curso completo de trading de criptomonedas por análisis técnico multicapa**
> 
> 842 archivos · 52 carpetas · Julio 2023 – Febrero 2024

---

## 🗂️ ESTRUCTURA DEL MATERIAL

| # | Módulo | Archivos | Contenido |
|---|--------|----------|-----------|
| 1 | `2. S Y R` | 0 | ❌ **Vacío** — Soportes y Resistencias no documentados |
| 2 | `3. EMAS✅` | 92 | EMA10/55/200, compresión, teoría 12 velas, debilitamiento EMA55 |
| 3 | `3. VOLUMEN✅✅` | 4 | Subidas sin volumen (texto vacío) |
| 4 | `4. ESTRATEGIAS MENTOR` | 64 | Super Estrategia + Excel AUT LONG/SHORT con recompras |
| 5 | `5. COBERTURA` | 48 | Cobertura por rangos |
| 6 | `6. TIPS✅` | 112 | Tips de entrada, retrocesos, mercados tradicionales, ETF |
| 7 | `7. OPERACIONES JORGE✅` | 69 | Operaciones reales, quiebres, tomas de ganancia |
| 8 | `8. JUGADAS INSTITUCIONAL` | 60 | Jugadas institucionales (Feb 2024) |
| 9 | `9. Análisis Fundamental✅` | 7 | Impacto de noticias en soportes |
| 10 | `ANALISIS JORGE` | 192 | **Análisis completo de Jorge (17+ horas de redacción)** |
| 11 | `BOT/` | 13 | Configuración de bot de trading |
| 12 | `BullRun✅/` | 69 | Jugadas en bull run, EMA tips, patrones de entrada |
| 13 | `EXCEL ESTRATEGIA JORGE/` | 2 | Templates Excel de estrategia |
| 14 | `GAP/` | 3 | Gaps (archivos de texto vacíos) |
| 15 | `GESTION DINERO✅` | 2 | Gestión de capital |
| 16 | `Indicadores/` | 15 | Squeeze Momentum + ADX PRO (guía completa) |
| 17 | `OTC/` | 2 | Trading OTC |
| 18 | `OTROS/` | 19 | Exchange, VPN, trucos |
| 19 | `Psicología/` | 66 | Ballenas, masa, Market Maker |
| 20 | `Recompras.xlsx` | 1 | Buybacks (incompleto) |
| 21 | `RUNE✅/` | 1 | Análisis RUNE |
| 22 | `ARGUMENTOS.txt` | 1 | **Checklist maestro de la estrategia** |

---

## 🧬 ARQUITECTURA DE LA ESTRATEGIA — 7 PILARES

---

### PILAR 1: EMAS — EL CORAZÓN DEL SISTEMA

**EMAs utilizadas:** `EMA10` · `EMA55` · `EMA200` (exponenciales, cierre)

> *"Observa las EMAS, aprende de ellas. Los movimientos, las curvaturas, todo tiene un porqué. Ellas se adelantan al movimiento."* — Jorge

#### Señales de las EMAs

| Señal | Interpretación | Acción |
|-------|---------------|--------|
| EMAs con **pendiente pronunciada** | Tendencia fuerte | Seguir dirección |
| EMAs **aplanándose** | Se avecina rango o cambio estructural | Prepararse |
| EMAs **comprimiéndose** (se juntan sin tocarse) | Explosión inminente | 🔥 **Señal más poderosa** |
| EMA10 se **cruza** con EMA55 | Cambio estructural de tendencia | Iniciar conteo de 12 velas |
| EMA10 y EMA55 forman **"montañita"** | Compresión lista para disparar | Preparar entrada |
| **Cruces durante volatilidad** | Se identifica nivel de fuerza | Medir fuerza del movimiento |
| EMA55 **tocada 3+ veces** como resistencia/soporte | La estructura se está rompiendo | **NO operar en contra** |
| Precio muy alejado de EMA10 (% alto) | Debe corregir o ranguear hacia EMA10 | Esperar corrección |
| **TF altos (4H, 1D, 1W)** | Rangos más fiables y duraderos | Operar rangos macro |
| **TF bajos (15m-1H)** | Rangos menos probables pero operables | Operar con cautela |
| **4H** | La temporalidad más respetable para rangos | TF de referencia |

#### Escenarios con EMA10

1. **Soporte/Resistencia para continuar la tendencia** — El precio se apoya y sigue
2. **Rango** — El precio consolida alrededor de la EMA10
3. **Apoyarse para romperla** — Toque + rechazo → ruptura
4. **Romperla directamente** — Ruptura limpia sin apoyo previo

> ⚠️ *"Ten en cuenta los tipos de velas que se forman alrededor de la EMA y los patrones, para que no te engañen con los próximos movimientos."*

#### Regla de oro

> *"Para una operación más confiable, opera los rangos a nivel macro (4H, 1D, 1W), porque tienen más durabilidad y mayor porcentaje a operar."*

---

### PILAR 2: TEORÍA DE LAS 12 VELAS — EL TIMING

**Regla universal:** Después de una señal de cambio estructural, se cuentan **12 velas**. La entrada se hace en la **vela #7**. El resultado se ve en la **vela #12**. Funciona en **cualquier temporalidad** (5m, 15m, 1H, 4H, 1D, 1W).

#### Tabla de equivalencias temporales (del Excel `Teoria 12 Velas solo por EMAS.xlsx`)

| Temporalidad | 8 velas | 12 velas | 18 velas |
|-------------|---------|----------|----------|
| **15m** | 2 horas | 3 horas | — |
| **1H** | 8 horas | 12 horas | 18 horas (1-2 días) |
| **4H** | — | 48 horas (2-3 días) | 72 horas (3-7 días) |
| **1D** | — | 10-12 días | 18-30 días |
| **1W** | — | 12 semanas | — |

#### Escenario 1: Tendencia bien definida

```
Contexto: Macro alcista, precio en rango. Rompe resistencia con cuerpo, hace nuevo máximo. 
Señal de fortaleza.

Proceso:
  1. Rompe resistencia → se transforma en soporte
  2. Precio debe ranguear (acumular stock)
  3. Cuenta desde vela roja que muestra debilidad (toca el soporte)
  4. Entra en vela #7
  5. Vela #8 o posterior → pump

Ejemplo: BTC 4H, resistencia $38,450. 
Rompe → apoya → 7 velas de rango → vela #8 pump.
```

#### Escenario 2: Cambio estructural por EMAs

```
Contexto: Cruce de EMA10/55 confirma cambio de tendencia + estructura Wyckoff.

Proceso:
  1. Confirmar tendencia por cruce de EMAs + velas
  2. Contar desde el cruce de EMAs
  3. Vela #7 suele tocar la EMA55
  4. Comprar desde vela #7 (o antes si monitoreas en tiempo real)
  5. Vela #12 debe estar cerca del máximo anterior

Nota: El mismo patrón se repite en todas las temporalidades cuando hay tendencia.
```

#### Escenario 3: Anticipar cambio de tendencia (el más avanzado)

```
Contexto: Macro alcista en TF altos. TF bajo (1H) solo es retroceso. 
La operación es LONG.

Proceso:
  1. Vela envolvente rompe mini-rango anterior
  2. Inicia conteo desde esa vela grande
  3. Entra en vela #7

Sub-estrategia A — SCALPING:
  - Sales en la EMA
  - Cobras una parte y dejas correr
  - Si el precio vuelve a tu entrada, recargas LONG

Sub-estrategia B — CAMBIO ESTRUCTURAL:
  - NO sales cuando toque la EMA
  - Esperas el cambio estructural completo
  - Si el precio vuelve a tu entrada, no importa — casi nunca pasa
  - Y si pasa, es para coger SL de los que entraron con SL debajo del mínimo
```

##### 🔥 El insight más brutal de todo el curso:

> *"El precio no fluctúa en ondas. El precio fluctúa según dónde están los Stop Loss de la gente. Lo que hace el precio realmente es perseguir a los sobreapalancados con SL."*

> *"Por este motivo se producen los dobles suelos. Hay unos que ponen el SL un poquito más arriba o más abajo, dos bandos. Donde haya más dinero de esos dos bloques, el precio va. El precio fluctúa según dónde haya más dinero para comer (SL)."*

#### Escenario 4: Con Squeeze Momentum

Misma teoría de 12 velas pero confirmada con el indicador Squeeze + ADX. Los cuadrantes de impulso confirman la dirección esperada.

#### Escenario 5: Compresión fallida + entrada en TF alto

```
Cuando las EMAs comprimen demasiado sin resolver al alza en TF alto.
Si no sube en el tiempo esperado, caerá. 
Señal de debilidad → prepararse para el movimiento real (que puede ser bajista).
```

#### Variante "sin valle rojo" (Técnica enseñada el 19 dic 2023)

```
Contexto: Tendencia bajista, cualquier temporalidad (probado desde 5m funciona bien).

Proceso:
  1. Mercado decide irse alcista
  2. Marca un mini ATH después del cruce de EMA10 con EMA55
  3. Cuenta 12 velas desde la vela que marca el máximo o la alcista 
     que cierra por encima del punto medio de la anterior
  4. Vela #7: precio suele tocar EMA55 → COMPRAR
  5. Vela #12: precio debe estar muy cerca del mini ATH nuevamente
```

---

### PILAR 3: COMPRESIÓN DE EMAS — LA SEÑAL MÁS PODEROSA

> *"Después de un cambio estructural, el precio DEBE ranguear — acumulando stock — mientras se comprimen las EMAs, para luego continuar. Si no lo hace, caerá."*

#### Fases de la compresión

```
Fase 1. Cambio estructural (patrones de velas + EMAs)
Fase 2. Impulso busca siguiente nivel (resistencia)
Fase 3. Primer toque → rebote (normal, especialmente si es resistencia importante)
Fase 4. Inicia conteo de 12 velas
Fase 5. EMAs comienzan a comprimirse (montañita entre EMA10 y EMA55)
Fase 6. Vela #7: entrada
Fase 7. Vela #11: EMA10 debe aplanarse y precio por encima de ambas EMAs
Fase 8. Vela #12: impulso
```

#### ⚠️ La compresión tiene tiempo límite

Si la EMA10 no se aplana y el precio no se recupera por encima de ambas EMAs para la vela #11, la compresión **fallará** y el precio caerá.

#### Ejemplos documentados

**Ejemplo 1 — BTC Weekly (compresión exitosa):**
- Cambio estructural → rango → compresión → entrada vela #7
- Market Maker bombeó en vela #9 (antes de lo esperado por teoría)
- Segundo ciclo similar → entrada vela #7 → pump

**Ejemplo 2 — XRP Weekly (compresión en tendencia alcista):**
- Vela verde agresiva 55% + absorción en mecha 19%
- Alejado de EMA10 un 60% → debe ranguear
- No pudo ranguear → buscó EMA55 → absorción del 22% → nuevo soporte
- Compresión "fea" → entrada vela #7 sin miedo
- Subida del 47% hasta vela #11
- Segundo ciclo: rango de distribución → quiebre → nueva compresión → nuevo conteo

**Ejemplo 3 — BTC 1D/4H (compresión FALLIDA):**
- EMAs comprimidas en diario muy estrechas → avisa movimiento fuerte
- 4H: compresión bajista para cambio alcista
- 3 toques a EMA55 (debilitando resistencia) → 4to toque debería ser LONG
- Vela roja rompe mini-rango entre EMAs → compresión falla
- Precio cae → busca liquidez → rebota para testear resistencia anterior
- **Jugada del Market Maker**

**Ejemplo 4 — BTC 4H (compresión en zona de peligro):**
- EMAs comprimiendo en zona de peligro (soporte del rango 4H)
- 1H: cada toque a EMA10 es para caer (tendencia bajista EMAs)
- Parece que no tiene fuerza para subir, pero ES NORMAL
- Una vez que EMAs comprimieron suficiente en TF mayor
- 1H: precio rango alto + EMAS comprimen → señal de operar cambio estructural

---

### PILAR 4: SQUEEZE MOMENTUM + ADX PRO — CONFIRMACIÓN

> Sistema original de John Carter ("Mastering the Trade", cap. 11) + LazyBear (TradingView) + TradingLatino. Documento completo de **DIGITAL CAPITALS TRADING**.

#### Definición

El Squeeze Momentum Indicator + ADX PRO es un **oscilador de impulso** que indica la **explosividad y dirección** con que el precio se moverá.

#### Los 4 cuadrantes de poder

| Cuadrante | Condición | Potencia | Color |
|-----------|-----------|----------|-------|
| 🔥 **Impulso Alcista** | Oscilador pendiente **POSITIVA** y está **DEBAJO** de línea 0 | **Doble potencia** | 🟢 Verde |
| 💪 **Fuerza Alcista** | Oscilador pendiente **POSITIVA** y está **ENCIMA** de línea 0 | Potencia normal | 🟡 Amarillo |
| 🔥 **Impulso Bajista** | Oscilador pendiente **NEGATIVA** y está **ENCIMA** de línea 0 | **Doble potencia** | 🔴 Rojo |
| 💪 **Fuerza Bajista** | Oscilador pendiente **NEGATIVA** y está **DEBAJO** de línea 0 | Potencia normal | 🟠 Naranja |

> **Regla:** Los cuadrantes de **impulso** poseen el **doble de potencia** que los de fuerza. Su misión es cambiar la dirección del oscilador para generar las ondas. Los de fuerza representan la **pérdida de fuerza** del movimiento.

#### Squeeze ON/OFF

- **Cruces negras en línea media** = mercado acaba de entrar en consolidación (baja volatilidad) → se prepara movimiento explosivo
- **Cruces grises** = "Squeeze" activo
- **Estrategia de Carter:** Esperar hasta el primer gris después de una cruz negra → tomar posición en dirección del oscilador

#### Señales automatizadas

| Señal | Condición | Significado |
|-------|-----------|-------------|
| **B (Buy)** | Termina ADX bajista + oscilador dirección alcista (Impulso alcista) | Comprar |
| **S (Sell)** | Termina ADX alcista + oscilador dirección bajista (Impulso bajista) | Vender |

#### Filtro de tendencia

- **EMA10 > EMA55** = Tendencia alcista → **solo alertas de compra activas**
- **EMA10 < EMA55** = Tendencia bajista → **solo alertas de venta activas**
- El trader puede activar/desactivar este filtro

#### Alertas disponibles

- Buy y Sell
- Activación del Squeeze ON
- Cambios de cuadrante (Impulso Alcista, Fuerza Alcista, Impulso Bajista, Fuerza Bajista)

#### Componentes del panel automatizado

- Panel numérico con valor del ADX y direccionalidad en tiempo real
- Flecha indicadora de direccionalidad del oscilador
- Panel EMA10/55 con tendencia (alcista/bajista)
- Señalador de Squeeze ON/OFF
- Cambio de color automático de paneles según cuadrante

---

### PILAR 5: GESTIÓN DE CAPITAL — LA "SUPER ESTRATEGIA"

Los archivos Excel contienen **calculadoras automáticas de posición con sistema de recompras (DCA)**.

#### 📊 Parámetros de los 4 templates

| Archivo | Tipo | Capital | Apalancamiento | Precio Entrada | Take Profit | Última Bala |
|---------|------|---------|----------------|----------------|-------------|-------------|
| `AUT LONG (TARDE-TECHOS)` | LONG | **$80** | 35x | $96.71 | $150 | $49.18 |
| `AUT SHORT (AL PUNTO-TECHOS)` | SHORT | **$33** | 100x | $51,300 | $44,000 | $57,166 |
| `AUT SHORT (TARDE-SUELOS)` | SHORT | **$100** | 100x | $31,000 | $27,000 | $74,978 |
| `long.xlsx` | LONG | **$89** | 50x | $20.17 | $22 | $14.35 |

#### Sistema de recompras escalonadas (ejemplo AUT SHORT TARDE-SUELOS)

| Recompra | % Margen | Margen Requerido | Precio Recompra | Precio Medio | Tamaño Posición |
|----------|----------|-----------------|-----------------|-------------|-----------------|
| R0 | 0.20% | $0.20 | $31,000 | $31,000 | $20.00 |
| R1 | 0.20% | $0.199 | $31,496 | $31,247 | $39.89 |
| R2 | 0.20% | $0.198 | $31,999 | $31,497 | $59.68 |
| R3 | 0.20% | $0.197 | $32,512 | $31,749 | $79.36 |
| R4 | 0.20% | $0.196 | $33,032 | $32,003 | $98.93 |
| R5 | 0.20% | $0.195 | $33,561 | $32,259 | $118.41 |
| R6 | 0.20% | $0.194 | $34,098 | $32,518 | $137.81 |
| R7 | 0.20% | $0.193 | $34,643 | $32,779 | $157.15 |
| **TOTAL** | **1.57%** | — | — | — | **$157.15** |

#### Sistema de recompras AUT LONG (TARDE-TECHOS)

| Recompra | % Margen | Precio Recompra | Precio Medio | Tamaño Posición |
|----------|----------|-----------------|-------------|-----------------|
| R0 | 6.70% | $96.71 | $96.71 | $187.60 |
| R1 | 0.20% | $95.26 | $96.67 | $192.62 |
| R2 | 0.20% | $93.83 | $96.60 | $197.61 |
| R3 | 0.20% | $92.42 | $96.50 | $202.60 |
| R4 | 0.20% | $91.04 | $96.37 | $207.57 |
| R5 | 0.20% | $89.67 | $96.21 | $212.52 |
| R6 | 0.20% | $88.33 | $96.03 | $217.46 |
| R7 | 5.00% | $87.00 | $92.77 | $340.50 |
| **TOTAL** | **12.16%** | — | — | **$340.50** |

#### 📊 Excel de recompras con cobertura (`Recompras (No terminado).xlsx`)

Contiene un sistema de cobertura LONG + SHORT simultáneos:

| Concepto | LONG | SHORT |
|----------|------|-------|
| Capital | $72 | — |
| % Cobertura | 21.5% | 33% |
| Monto | $15.48 | $23.76 |
| R1 | $43,516 | 0 |
| R2 | $43,020 | 0 |
| R3-R6 | 0 | 0 |

---

### PILAR 6: REGLAS DE ENTRADA — EL CHECKLIST MAESTRO

> Fuente: `ARGUMENTOS.txt` — El documento más importante de toda la carpeta.

#### Checklist completo ANTES de abrir una operación

```
☐ 1. TODOS los gráficos SINCRONIZADOS
     (15m, 1H, 4H, 1D, 1W deben contar la misma historia)

☐ 2. SOPORTES y RESISTENCIAS FUERTES
     o líneas de tendencia bien definidas

☐ 3. ORDER BLOCK (OB) VIRGEN o ZONA DE REACCIÓN
     Los OB FUERTES son desde 4H hacia arriba — "ahí entran los cracks"

☐ 4. LIQUIDEZ identificada
     ¿Dónde están los stops de la masa?

☐ 5. TEORÍA DE 12 VELAS activa
     Conteo iniciado, preferiblemente velas #5-#7

☐ 6. RUPTURAS e IMBALANCES confirmados

☐ 7. REGLA DE LOS 3 TOQUES
     Si una resistencia fue tocada 3 veces → NO short → posible LONG al 4to
     (TIP: no siempre se cumple, pero debe tenerse en consideración)

☐ 8. DATOS DE TRADING
     Entender por qué el precio sube sin volumen

☐ 9. EMAS chequeadas:
     • R y S
     • Cruces entre ellas, inclinación o aplanamiento
     • Pauta de compresión y sincronización
     • Picos pequeños
     • EMA10, 55, 200 / MA200
     • Precio alejado de EMA10 → posible rango o corrección

☐ 10. CONFIRMACIÓN DE ENTRADA
     OB virgen en 1D → refinar en 4H → contar velas → entrada calculada
```

#### Proceso de confirmación completo

```
1. Buscar OB VIRGEN o FUERTE desde 4H hacia arriba
2. Bajar a temporalidad inferior para refinar la entrada
3. Contar las velas para tener una entrada calculada
4. Ejemplo: OB virgen en 1D → refinar en 4H → entrada precisa
5. Confirmación final: gráficos sincronizados + OB fuerte
```

---

### PILAR 7: TIPS OPERATIVOS CLAVE

#### Tips de Entrada (`6. TIPS✅/TIP para entradas.txt`)

| # | Tip |
|---|-----|
| 1 | **Mejor estrategia:** Ver caer el mercado y cazar **LONG** en tendencia alcista de EMAs en semanal y mensual |
| 2 | En tendencia bajista a nivel EMAs semanal y pendiente negativa mensual → jugar **SHORT** |
| 3 | Los **soportes** son más seguros — el precio **rebotará** en algún momento |
| 4 | Las **resistencias** no tienen límite — llegado el punto **no tienen techo** |

#### Retrocesos y Correcciones (`6. TIPS✅/Retroceso o Corrección.txt`)

> *"Los retrocesos o corrección, la mayoría de las veces, son del **50%** del impulso de la vela anterior, tanto al alza como a la baja."*

#### Consideraciones del Mercado (`6. TIPS✅/Consideración.txt`)

| Situación | Comportamiento |
|-----------|---------------|
| Mercado alcista, precio en resistencia **volátil** | Rebote de ~$1,500 |
| Mercado alcista, precio en resistencia **no volátil** | Rechazo de $400-$800 |
| **BTC volátil** | = **ALTs volátiles** |
| Gráficos **perpetuos** | Análisis de 4H hacia abajo |
| Gráficos **spot** | Análisis de 1D hacia arriba |

#### Análisis Fundamental (`9. Análisis Fundamental✅/TIP.txt`)

> *"Cuando hay noticia mala, no hay soporte que valga... hasta que se encuentra una pared (soporte bueno)."*

#### Debilitando EMA55 (`3. EMAS✅/Debilitando EMA55✅/Explicacion 19 dic - 2023.txt`)

```
• Si EMA55 en 1H actúa como resistencia y es tocada más de una vez,
  especialmente después del 3er toque sin rechazar el precio → NO entres en SHORT
• Esto confirma que la estructura bajista se ROMPIÓ
• Para que sea más efectiva, debe situarse en zona de S/R importante en TF mayores
• Operar en fuego cruzado del rango = más riesgoso (50/50)
• Requiere análisis más exhaustivo y correcta gestión del riesgo
```

#### Cobertura (`5. COBERTURA/Cobertura.txt`)

> *"La cobertura es como si trabajaras en una caja. Siempre tienes un rango que se mueve con el precio. Encuentra un rango y este con el tiempo se va ampliando."*

---

### PILAR 8: PSICOLOGÍA DE TRADING

> Fuente: `Psicología(ballena, masa y personal)/TIP.txt`

#### Principio fundamental

> *"Cuando muchos (las masas) ven lo mismo (patrón) para su beneficio, generalmente el Market Maker hace lo contrario para liquidarlos (comer)."*

#### Cómo atrapa el Market Maker a la masa

- **Chartismo clásico** — patrones que todos conocen → el MM hace lo contrario
- **Patrones técnicos** — los agarra en confianza/FOMO
- **Soportes obvios** — la masa pone stops ahí → el precio va a comerlos
- **Dobles suelos** — no son estructura, son cacería de stops de dos bandos de sobreapalancados
- **Noticias** — el MM las usa para barrer stops antes del movimiento real

#### La verdad sobre el precio

> *"El precio no fluctúa en ondas. El precio persigue a los sobreapalancados con SL. Por eso se producen los dobles suelos: hay dos bandos que ponen el SL un poquito más arriba o más abajo. Donde haya más dinero de esos dos bloques, el precio va."*

---

### PILAR 9: GESTIÓN DE SALIDA

> Fuente: `7. OPERACIONES JORGE✅/Quiebres (Rompimiento Estructuras)/Explicacion.txt`

#### Reglas de salida de Jorge

1. **Entrar con alto porcentaje** en quiebres estructurales (con EMAs)
2. **Tomar ganancia al 30-50% mínimo**
3. **Retirar 90-95% de la posición**
4. **"Salir corriendo"** — ser agresivo en la salida, no esperar más

> *Ejemplo real (19 dic 2023): Jorge tenía una orden que no se activó por $20 USD. Como el mercado ya estaba muy arriba, entró por rompimiento estructural. "Una entrada que él hizo a la fija."*

---

### PILAR 10: EJEMPLO DE OPERACIÓN REAL — CONTRA TENDENCIA

> Fuente: `3. EMAS✅/Operando contra tendencia utilizando EMAS✅/Explicacion.txt`

**Fecha:** 24 julio 2023 — BTC

#### Contexto multi-temporalidad

```
1D: Rompió rango anterior a la baja → sostenido por EMA55 → 
    alejado 3% de EMA10 → DEBE CORREGIR a EMA10
4H: Alejado 2.37% de EMA10 + dos absorciones de 0.8% en parte baja
1H: Dos absorciones de 0.6% + alejado de EMA10 1.4-2%
```

#### Entrada afinada en 15m

```
15m: Finaliza ciclo bajista → corrigiéndose a EMA10 en toda la bajada
     Mecha larga de ABSORCIÓN con VOLUMEN
     → Fin del movimiento bajista
     → Comienzo de cuadrante IMPULSO ALCISTA en Squeeze Momentum
     → Entrada sin miedo en el doble piso o en la misma mecha
     → Entrada: $29,000 - $28,800
```

#### Objetivos

```
TP1: EMA55 en 15m = EMA10 en 4H ✓ (cumplido)
TP2: EMA55 en 1H y 4H mientras comprimen EMAs en diario
     Hay imbalance en 1H y 4H antes de llegar a la EMA
     → El recorrido no tendrá dificultad en irse al alza
```

---

## ⚙️ GUÍA COMPLETA DE IMPLEMENTACIÓN

---

### Fase 1: Configuración de TradingView

#### Indicadores a instalar

```
┌─ MEDIAS MÓVILES ─────────────────────────────┐
│ EMA 10  (exponencial, close, color azul)      │
│ EMA 55  (exponencial, close, color amarillo)  │
│ EMA 200 (exponencial, close, color rojo)      │
│ MA 200  (simple, close, color gris)            │
└───────────────────────────────────────────────┘

┌─ OSCILADORES ─────────────────────────────────┐
│ Squeeze Momentum Indicator (LazyBear)          │
│ ├─ Panel de cuadrantes de colores              │
│ ├─ Señales B (Buy) / S (Sell)                  │
│ └─ Squeeze ON/OFF                              │
│                                                 │
│ ADX PRO (console / TradingLatino)               │
│ ├─ Panel numérico con valor ADX                │
│ ├─ Flecha de direccionalidad                   │
│ └─ Panel EMA10/55 con tendencia                │
└───────────────────────────────────────────────┘

┌─ HERRAMIENTAS DE DIBUJO ──────────────────────┐
│ Soportes y Resistencias horizontales           │
│ Líneas de tendencia                            │
│ Order Blocks (OB)                              │
│ Canales / Rangos                               │
│ Fibonacci (retrocesos al 50%)                  │
└───────────────────────────────────────────────┘
```

#### Layout multi-temporalidad

```
┌──────────────┬──────────────┬──────────────┐
│    1W        │     1D       │     4H       │
│  (contexto   │   (OBs +     │  (refinar    │
│   macro)     │  tendencia)  │   entrada)   │
├──────────────┼──────────────┼──────────────┤
│     1H       │     15m      │   SQUEEZE    │
│  (setup de   │  (entrada    │   + ADX      │
│   entrada)   │   precisa)   │   (panel)    │
└──────────────┴──────────────┴──────────────┘
```

---

### Fase 2: Rutina de Análisis Diario

```
PASO 1 — CONTEXTO MACRO (1W + 1D)
├─ ¿Tendencia alcista o bajista a nivel de EMAs?
├─ ¿Las EMAs están expandidas, aplanándose o comprimiendo?
├─ Soportes y resistencias principales
├─ Order Blocks vírgenes (sin tocar)
└─ ¿Hay compresión activa?

PASO 2 — ZONAS DE INTERÉS (4H)
├─ ¿Hay OB virgen cerca del precio actual?
├─ ¿Hay compresión de EMAs activa?
├─ ¿Hay conteo de 12 velas en curso?
├─ ¿EMA55 está siendo debilitada (3+ toques)?
└─ Zonas de liquidez visibles (mínimos/máximos con stops)

PASO 3 — CONFIRMACIÓN (1H + Squeeze/ADX)
├─ ¿Tendencia de EMAs en 1H?
├─ ¿Cuadrante del Squeeze Momentum?
├─ ¿ADX confirma dirección?
├─ ¿Hay Squeeze ON activo?
└─ ¿Velas alrededor de EMAs muestran intención?

PASO 4 — ENTRADA (15m)
├─ Afinar OB o zona de reacción
├─ Confirmar absorción con volumen
├─ Cuadrante de impulso en Squeeze
├─ Calcular SL (debajo del OB o EMA55)
└─ Definir TP parcial (30-50%) y TP final
```

---

### Fase 3: Protocolo de Entrada

```
┌─────────────────────────────────────────────────┐
│           CHECKLIST DE ENTRADA                   │
├─────────────────────────────────────────────────┤
│                                                  │
│  ☐ Gráficos sincronizados (15m→1W)              │
│  ☐ OB VIRGEN en 1D o 4H                         │
│  ☐ EMAs comprimiendo o recién cruzadas           │
│  ☐ Conteo de 12 velas: #5-#7 preferiblemente    │
│  ☐ Squeeze en cuadrante de IMPULSO              │
│  ☐ ADX confirmando dirección                     │
│  ☐ EMA55 no está siendo tocada 3+ veces          │
│      (a menos que sea LONG tras debilitamiento)  │
│  ☐ Precio alejado de EMA10 → corrección esperada │
│  ☐ SL identificado (OB o EMA55)                  │
│  ☐ TP definido (30-50% mínimo)                   │
│                                                  │
│  SI TODOS → ENTRAR SIN MIEDO                    │
│  SI FALTA ALGUNO → ESPERAR o NO ENTRAR           │
└─────────────────────────────────────────────────┘
```

#### Timing exacto de entrada

| Vela # | Acción |
|--------|--------|
| #0 | Cambio estructural detectado (cruce, quiebre, envolvente) |
| #1-#4 | Monitorear compresión, esperar |
| #5-#6 | Preparar orden, afinar zona |
| **#7** | **ENTRAR** (suele tocar EMA55) |
| #8-#11 | Dejar correr, mover SL a BE |
| #12 | Resultado esperado → tomar ganancia parcial o total |

---

### Fase 4: Gestión de Riesgo

#### Basado en los templates Excel de Jorge

| Parámetro | Configuración |
|-----------|--------------|
| Capital por operación | 10-30% del portfolio (LONG), 5-15% (SHORT) |
| Apalancamiento máximo | 35-50x (LONG), 50-100x (SHORT) |
| Recompra inicial | -1.6% del precio de entrada |
| Paso entre recompras | 0.2% → 0.4% → 0.8% → 1.6% → 3.2% → 6.4% |
| Máximo recompras | 5-7 (según template) |
| Stop Loss | OB virgen o EMA55 (el más alejado) |
| Take Profit parcial | 30-50% de la posición |
| Retiro de capital | 90-95% después del TP parcial |
| Capital máximo en riesgo | Ver "Última Bala" en el Excel |

#### Cálculo de tamaño (fórmula de Jorge)

```
Margen Inicial = Capital × % de Margen (5-10%)
Monto Apalancado = Margen × Apalancamiento
Precio Medio = Precio de Entrada (inicialmente)
Nuevo Precio Medio = Σ(Monto × Precio) / Σ(Monto)

Liquidación LONG  = Precio Medio × (1 - 1/Apalancamiento)
Liquidación SHORT = Precio Medio × (1 + 1/Apalancamiento)

Take Profit LONG  = Precio Medio × (1 + %TP)
Take Profit SHORT = Precio Medio × (1 - %TP)
```

---

### Fase 5: Cuándo NO operar

```
❌ GRÁFICOS NO SINCRONIZADOS
   Diferentes temporalidades cuentan historias contradictorias

❌ SIN OB VIRGEN EN TF ALTO
   Sin zona de reacción clara, la entrada es ciega

❌ EMA55 TOCADA 3+ VECES COMO RESISTENCIA
   NO shortear — la estructura se está rompiendo

❌ COMPRESIÓN SIN SQUEEZE CONFIRMANDO
   La compresión puede fallar si no hay confirmación

❌ RANGO EN FUEGO CRUZADO (50/50)
   El precio puede ir a cualquier lado sin análisis exhaustivo

❌ NOTICIAS FUNDAMENTALES NEGATIVAS FUERTES
   "Cuando hay mala noticia, ningún soporte aguanta"

❌ FOMO — VELA #7 YA PASÓ
   Si el tren ya salió, esperar el siguiente setup

❌ EMAS MUY EXTENDIDAS SIN CORRECCIÓN
   El precio eventualmente volverá a la EMA10

❌ SIN LIQUIDEZ CLARA IDENTIFICADA
   No sabes hacia dónde irá el precio a buscar stops

❌ MERCADO SIN VOLATILIDAD (SQUEEZE ON DEMASIADO TIEMPO)
   La explosión puede tardar más de lo esperado
```

---

### Fase 6: Monitoreo y Salida

```
DURANTE LA OPERACIÓN:

1. Mover SL a Break Even cuando el precio avance un 15-20%
2. Tomar 30-50% de ganancia en TP1
3. Retirar 90-95% del capital inicial
4. Dejar el resto correr con SL ajustado al siguiente nivel
5. Salir completamente si:
   ├─ Squeeze cambia a cuadrante de fuerza opuesto
   ├─ ADX pierde direccionalidad
   ├─ Vela #12 ya pasó sin resultado
   └─ Precio rompe EMA55 en contra

DESPUÉS DE LA OPERACIÓN:

1. Registrar: entrada, salida, argumentos, resultado
2. Revisar qué funcionó y qué no
3. Esperar siguiente setup — no sobre-operar
```

---

### Fase 7: Configuración de Alertas (TradingView)

```
ALERTA 1 — Squeeze ON
  Condición: Squeeze Momentum Indicator → Squeeze ON

ALERTA 2 — Cambio de cuadrante
  Condición: Squeeze → cambia a Impulso Alcista o Impulso Bajista

ALERTA 3 — Señal B/S
  Condición: B (Buy) o S (Sell)

ALERTA 4 — Cruce de EMAs
  Condición: EMA10 cruza EMA55 (arriba o abajo)

ALERTA 5 — Precio toca EMA55
  Condición: close cruza EMA55 (para entradas de 12 velas)
```

---

## 📋 RESUMEN DE TODOS LOS ARCHIVOS DE TEXTO

| Archivo | Contenido | Líneas |
|---------|-----------|--------|
| `ARGUMENTOS.txt` | Checklist maestro de la estrategia | 21 |
| `Estudiar de las EMAS.txt` | Cómo las EMAs avisan el movimiento | 9 |
| `Explicacion - Resumen.txt` | Teoría de las 12 velas (4 escenarios) | 46 |
| `explicación de ejemplos.txt` | 4 ejemplos de compresión | 18 |
| `Explicacion 19 dic - 2023.txt` | Debilitamiento EMA55 | 6 |
| `Explicación jesus 19 dic - 2023 (12 velas).txt` | Técnica sin valle rojo | 8 |
| `Explicacion.txt` (contra tendencia) | Operación real BTC 24 julio 2023 | 10 |
| `Explicacion.txt` (quiebres) | Gestión de salida en rupturas | 9 |
| `TIP para entradas.txt` | Tips de entrada (LONG/SHORT/soportes) | 7 |
| `Retroceso o Corrección.txt` | Retrocesos son 50% | 1 |
| `Consideración.txt` | Volatilidad, sincronización, perp vs spot | 10 |
| `Cobertura.txt` | Concepto de cobertura por rangos | 2 |
| `TIP.txt` (análisis fundamental) | Noticias malas y soportes | 1 |
| `TIP.txt` (psicología) | Market Maker vs las masas | 3 |
| `NO TODOS LOS GAP SE LLENAN.txt` | Vacío | 0 |
| `ESTUDIAR.txt` (GAP) | Vacío | 0 |
| `sube sin volumen.txt` | Vacío | 0 |

---

## 📊 RESUMEN DE LOS ARCHIVOS EXCEL

| Archivo | Tipo | Descripción |
|---------|------|-------------|
| `Teoria 12 Velas solo por EMAS.xlsx` | Calculadora | Tabla de equivalencias temporales 15m→1W |
| `AUT LONG (TARDE-TECHOS).xlsx` | Estrategia | LONG automático con 7 recompras, 35x |
| `AUT SHORT (AL PUNTO-TECHOS).xlsx` | Estrategia | SHORT automático con 4 recompras, 100x |
| `AUT SHORT (TARDE-SUELOS).xlsx` | Estrategia | SHORT automático con 7 recompras, 100x |
| `long.xlsx` | Estrategia | LONG con 5 recompras, 50x |
| `Recompras (No terminado).xlsx` | Cobertura | Sistema LONG/SHORT simultáneo con cobertura |

---

## 🎯 EL MÉTODO JORGE EN 10 PASOS

```
1. MIRA LAS EMAS
   └─ ¿Están expandidas, aplanándose o comprimiéndose?
   └─ La curvatura y la inclinación te dicen lo que viene

2. IDENTIFICA EL CONTEXTO MACRO
   └─ 1W/1D: tendencia, S/R, OBs vírgenes

3. BUSCA COMPRESIÓN
   └─ EMA10 y EMA55 juntándose = explosión inminente
   └─ Si no hay compresión, espera

4. ENCUENTRA UN OB VIRGEN
   └─ En 4H, 1D o 1W — sin haber sido tocado

5. INICIA CONTEO DE 12 VELAS
   └─ Desde el cambio estructural (cruce, quiebre, envolvente)

6. CONFIRMA CON SQUEEZE + ADX
   └─ Cuadrante de IMPULSO (doble potencia)
   └─ ADX en dirección correcta

7. ENTRA EN LA VELA #7
   └─ Sin miedo si todos los argumentos están alineados
   └─ SL debajo del OB o EMA55

8. COBRA RÁPIDO
   └─ TP1: 30-50% de ganancia
   └─ Retira 90-95% de la posición

9. DEJA CORRER EL RESTO
   └─ SL a BE o trailing
   └─ Objetivo: vela #12 o siguiente S/R

10. NO SOBRE-OPERES
    └─ Si no hay setup claro, no entres
    └─ El mercado siempre da otra oportunidad
```

---

## 🧠 FRASES CLAVE DE JORGE

> *"Observa las EMAS, aprende de ellas. Los movimientos, las curvaturas, todo tiene un porqué. Ellas se adelantan al movimiento."*

> *"Según las curvaturas, se pueden identificar movimientos fuertes y/o rangos antes de que sucedan."*

> *"El precio no fluctúa en ondas. El precio persigue a los sobreapalancados con Stop Loss."*

> *"Cuando las masas ven lo mismo para su beneficio, el Market Maker hace lo contrario para liquidarlos."*

> *"Cuando hay noticia mala, no hay soporte que valga... hasta que se encuentra una pared."*

> *"Los soportes son más seguros — el precio rebotará. Las resistencias no tienen techo."*

> *"Es mejor ver caer el mercado y cazar LONG en tendencia alcista de EMAs en semanal y mensual."*

> *"Salir corriendo — tomas ganancia al 30-50% mínimo y retiras el 90-95% de la operación."*

> *"La cobertura es como trabajar en una caja: siempre tienes un rango que se mueve con el precio."*

> *"Operar rangos a nivel macro (4H, 1D, 1W) es más confiable — más durabilidad y mayor porcentaje."*

---

## ⚠️ LIMITACIONES DE ESTE ANÁLISIS

1. **Las 815 imágenes NO pudieron ser visualizadas** — el modelo actual no tiene capacidad de visión. Para extraer el contenido visual (anotaciones, precios exactos, patrones dibujados en los gráficos) se necesitaría una herramienta con OCR o un modelo multimodal (GPT-4o, Claude, Gemini).

2. **Carpeta `2. S Y R` completamente vacía** — El módulo de Soportes y Resistencias no está documentado en esta copia.

3. **Archivos de texto vacíos** — Los módulos de GAP y Volumen no tienen contenido escrito.

4. **`Recompras (No terminado).xlsx`** — Incompleto, solo tiene la estructura base.

5. **El Excel `Recompras (No terminado).xlsx` tiene una pestaña "Sheet2"** con columnas para registrar operaciones (Exchange, Fecha, Hora, Activo, Estrategia, Apalancamiento, %, Entrada, Argumento Entrada, Salida, Argumento Salida) — pero está vacía (sin datos de operaciones registradas).

---

## 📐 PLANTILLA DE OPERACIÓN (PARA COPIAR Y USAR)

```
═══════════════════════════════════════════════════
 FECHA: ____/____/____
 ACTIVO: __________
 TEMPORALIDAD ENTRADA: ____
═══════════════════════════════════════════════════

 CONTEXTO MACRO:
 1W: _________________________________
 1D: _________________________________

 ARGUMENTOS DE ENTRADA:
 ☐ Gráficos sincronizados
 ☐ S/R fuerte: __________
 ☐ OB virgen en: ____ (TF: ____)
 ☐ Liquidez identificada en: __________
 ☐ Conteo 12 velas: vela #____
 ☐ EMAs: [ ] Comprimiendo [ ] Cruce reciente [ ] Expandidas
 ☐ EMA10 inclinación: ____  EMA55 inclinación: ____
 ☐ Squeeze cuadrante: __________
 ☐ ADX dirección: ____ (valor: ____)

 ENTRADA:
 Precio: __________
 % Capital: ____  Apalancamiento: ____x
 Tamaño posición: __________

 GESTIÓN:
 SL: __________ (argumento: __________)
 TP1 (30-50%): __________  → Retirar ____%
 TP2: __________
 Última bala: __________

 RECOMPRAS:
 R1: __________  R2: __________  R3: __________
 R4: __________  R5: __________  R6: __________

 RESULTADO:
 Salida: __________  P&L: __________
 ¿Se cumplió la teoría? [ ] Sí [ ] No
 Notas: _________________________________
═══════════════════════════════════════════════════
```

---

> **Documento generado a partir del análisis de 842 archivos del curso "Jorge Mentor"**
> 
> Fecha del material original: Julio 2023 – Febrero 2024
> 
> Análisis completado: Mayo 2026
