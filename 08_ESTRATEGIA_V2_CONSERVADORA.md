# ESTRATEGIA V2 CONSERVADORA — OBJETIVO $10 A $20 POR DÍA

## Propósito

Esta versión no intenta capturar todos los movimientos ni replicar la filosofía agresiva del material original. Está diseñada para:

- priorizar supervivencia de la cuenta,
- reducir entradas mediocres,
- buscar consistencia antes que grandes porcentajes,
- usar el bot como ejecutor disciplinado, no como “rescatador” de malas entradas.

## Regla principal

El objetivo diario no se fuerza. Se usa como techo operativo.

- Si ya hiciste entre `$10` y `$20`, dejas de abrir nuevas posiciones.
- Si el mercado no da setup de calidad, no se opera.
- Si el día viene malo, se corta rápido.

## Perfil operativo V2

- Mercado principal: `BTCUSDT`
- Sesgo: `long-only` por defecto
- Temporalidades:
  - `1D`: sesgo macro
  - `4H`: estructura y conteo
  - `1H`: ejecución
- Máximo de posiciones simultáneas: `1`
- Apalancamiento base: `3x`
- Capital activo por idea: `10%` de la cuenta

## Qué setups sí se operan

### Setup A — Máxima convicción

Condiciones:

- `1D` y `4H` alcistas por EMA10 > EMA55
- Compresión real EMA10/EMA55 en `4H`
- Conteo en zona `vela 6-8`
- Squeeze liberado o impulso alcista claro
- ADX con tendencia
- Precio en soporte útil: EMA55 o OB

Acción:

- abrir primera parte,
- permitir DCA solo si sigue en estructura,
- tomar parciales rápido.

### Setup B — Convicción alta

Condiciones:

- cruce alcista reciente,
- squeeze alcista ya disparado,
- confirmación 2H/3H/4H,
- volumen aceptable,
- no sobreextensión frente a EMA10.

Acción:

- entrada estándar,
- tamaño normal,
- sin persecución si ya corrió mucho.

### Setup C — Aceptable pero filtrado

Se puede operar solo si:

- score total `>= 8`,
- ADX confirma tendencia,
- no es fin de semana,
- no hay sobreextensión,
- no hay alerta de distribución,
- la sesión está dentro del horario líquido.

No es un trade premium como A/B, pero sí es operable si el resto de filtros está limpio.

## Qué setups NO se operan en V2

- Entradas contra tendencia
- Fines de semana
- ALTs por defecto
- Cobertura automática como plan primario
- Martingale agresivo
- “Aguantar hasta que vuelva” sin invalidación dura

## Gestión de posición V2

### Toma de ganancias

- `TP1`: `+1.0%` de precio
  - cerrar `20%`
- `TP2`: `+2.0%`
  - cerrar `20%`
- `TP3`: `+3.5%`
  - cerrar `30%`
- resto:
  - dejar solo `10%` corriendo si la estructura sigue limpia

### DCA moderado

Niveles:

- `-1.5%`
- `-3.0%`
- `-4.5%`
- `-6.0%`

Reglas:

- solo si `4H` sigue alcista,
- solo si el precio cae en soporte estructural,
- tamaños moderados, no doblantes agresivos.

### Invalidación dura

Si el trade llega a `-6%` desde el promedio, se sale.

La cobertura queda desactivada por defecto. Primero se demuestra que el edge simple existe; luego se evalúa si el hedge suma o solo complica.

## Riesgo diario V2

- objetivo diario: `+$15`
- límite diario: `-$15`

Eso obliga a una relación operativa mucho más sana que buscar `+$10` dejando correr `-$25`.

## Qué significa realmente “$10 a $20 por día”

Con cuenta de `5000 USDT`, eso equivale aproximadamente a:

- `0.2%` a `0.4%` diario sobre el equity.

No es un objetivo absurdo, pero sí exige:

- pocas entradas,
- buena disciplina,
- cero FOMO,
- cortar cuando el mercado no acompaña.

## Validación mínima antes de usar dinero real

No subir de etapa hasta cumplir esto:

1. `100` trades cerrados en paper o testnet.
2. Profit factor > `1.3`.
3. Win rate suficiente para tu estilo, pero más importante:
   - promedio de ganancia mayor que promedio de pérdida.
4. Drawdown controlado.
5. Ningún error de ejecución, sizing o estado del bot.

Para automatizar esta validación:

- usa `./11_RUN_VALIDATION_SUITE.sh`,
- revisa `validation_runs/<timestamp>/summary.md`,
- descarta cualquier activo con muestra insuficiente.

## Siguiente escalón

Solo después de validar BTC:

- añadir `ETHUSDT`,
- luego 1 o 2 ALTs líderes,
- nunca pasar a cesta multi-par amplia sin métricas reales.
