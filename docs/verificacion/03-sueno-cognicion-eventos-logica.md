# Verificacion 03: sueño, cognición, eventos, perfiles y lógica derivada

Auditoría independiente del dataset demo. Todo lo recalculado se hizo desde los archivos crudos de `nlsp-raw/downloads/x/` con código Python propio (`python3 -I`). Los scripts de trabajo están en `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif/` (fuera del proyecto). No se modificó ningún archivo existente.

## Resumen ejecutivo

- **Eventos:** `demo_eventos.csv` solo contiene la campaña CFT70 (132 filas). Faltan 921 eventos de `CRF_Campaign_3_Symptom_Complaint` (cobertura 12,5 %). La causa es el glob `CRF_*SYMPTOM*`, sensible a mayúsculas.
- **Sueño de C1G0003:** el archivo de consulta se lee antes que el archivo principal y gana el primer registro. Se sobrescriben 29 noches que sí están en el archivo A, y 11 noches son copias exactas de C1G0001. Las cifras de PRE (n=4) son en realidad 2 noches de un solo sujeto.
- **Vitales de C3:** `tidy_utmb.py` no reconoce cabeceras `SysBP`, `DiaBP`, `Body Temp`, `Weight` y `Respiration rate`. Faltan 582 días de PAS/PAD/temperatura, 809 de respiración y 801 de peso. Con datos completos el semáforo es 79,1 / 14,8 / 6,1 % (no 81 / 13 / 6 %), y 60 estados cambian.
- **Cognición:** hay 302 sesiones únicas, no 332. Las 30 de C1 aparecen duplicadas en `utmb_cognicion_winscat.csv`. Las medias de CPT RT cambian (523,6 / 492,8 / 475,5 ms frente a 531,5 / 496,8 / 477,3). La mejora entre fases coincide con aprendizaje (todas las primeras sesiones son Nasa1p, con instrucciones).
- **Anclaje:** hay 8 filas con BR_Day inconsistente con la fecha, no 4 (3985: 1; 7984: 7). En las 8 el error está en BR_Day; la fecha encaja con sus vecinos. `dia_mision` (calculado desde la fecha) es correcto.
- **Alineación sueño-vitales de C1:** no se confirma la sospecha. Fecha, BR_Day y fase coinciden en todos los días compartidos. Sí hay una fila de vitales con año 2001 (2001-10-29) que el script descarta en lugar de corregir.
- **Reproducibilidad:** `build_demo.py` reproduce los 6 archivos de `demo/` byte a byte; `tidy_utmb.py` reproduce los 5 `utmb/*.csv`.

---

## Tabla de verificación

Estado: **OK** = coincide; **DISCREPANCIA** = no coincide o hay error; **NO VERIFICABLE** = no hay forma de comprobarlo con los datos disponibles.

| # | Afirmación | Declarado | Recalculado | Estado | Nota |
|---|---|---|---|---|---|
| A1 | Sujetos de sueño | 3 | 3 (C1G0001-C1G0003) | OK | |
| A2 | Noches de sueño | 200 | 200 filas en el derivado; 190 con fuente única (archivo A) | DISCREPANCIA | 10 noches de C1G0003 se rellenan con el archivo de consulta (ambiguo); 11 noches de C1G0003 son copias exactas de C1G0001 (ver D-1) |
| A3 | Duración PRE (h) | 7,78 | 7,78 con n = 2 noches únicas | DISCREPANCIA | El derivado cuenta 4 filas porque las 2 de C1G0003 son copias de las de C1G0001. Con n = 2 la cifra no es interpretable |
| A4 | DE duración PRE | 0,06 | 0,07 (n = 2) | DISCREPANCIA | El 0,06 sale de la duplicación |
| A5 | Duración IN (h) | 7,22 ± 0,51 | 7,20 ± 0,53 (n = 167, solo archivo A) | DISCREPANCIA | Menor. Incluye 8 noches tomadas del archivo de consulta y 29 sobrescritas |
| A6 | Duración POST (h) | 7,47 | 7,40 (n = 21, solo archivo A) | DISCREPANCIA | Menor. Afectada por las sobrescrituras de C1G0003 |
| A7 | Eficiencia PRE (%) | 93,95 | 93,95 (n = 2) | OK (valor) | El valor coincide pero n = 2 no es interpretable |
| A8 | DE eficiencia PRE | 2,14 | 2,62 (n = 2) | DISCREPANCIA | El 2,14 proviene de cuatro filas con duplicados |
| A9 | Eficiencia IN (%) | 81,49 ± 8,73 | 81,65 ± 8,47 (n = 167) | DISCREPANCIA | Menor |
| A10 | Eficiencia POST (%) | 84,77 | 83,26 (n = 21) | DISCREPANCIA | 1,5 puntos de diferencia por las sobrescrituras de C1G0003 |
| A11 | Latencia PRE / IN / POST (min) | 10 / 41 / 33 | 10 / 43 / 32 (solo archivo A) | OK (± 2 min) | Las latencias escritas como `0` (3 noches) quedan vacías en el derivado (ver A15) |
| A12 | Parseo H:MM, `7:44:00` a 7,73 h | 7,733 | 7,733 | OK | Los formatos H:MM, H:MM:SS y decimal se parsean bien en el derivado |
| A13 | Los dos archivos de actigrafía son duplicados | Implícito (se deduplican) | No son duplicados. A tiene 207 filas (una por noche). B tiene 191 filas: 6 de C1G0002 idénticas a A; 185 de C1G0003, con 2 o 3 registros por noche en 66 de sus 69 noches | DISCREPANCIA | El deduplicado de `tidy_utmb.py` ("primero gana") depende del orden del glob, que no está ordenado. En este sistema B se lee antes que A |
| A14 | Deduplicado correcto | Correcto | Incorrecto para C1G0003: en 29 noches con valor en A se usa un registro de B | DISCREPANCIA | Ver D-1 y el código corto |
| A15 | Latencia `0` (sin dos puntos) | Válida | 3 noches (C1G0001 11/9, C1G0002 9/15, C1G0003 11/8) quedan vacías | DISCREPANCIA | Menor. `hhmm()` exige `H:MM` |
| A16 | Formato decimal en B (`6.56`) | Formato H:MM | Hay 1 registro decimal (C1G0003 10/9, registro 4052), no usado | NO VERIFICABLE | No altera la salida actual, pero el parser debería rechazarlo o avisar |
| A17 | Reproducible `utmb_sueno_actigrafia.csv` | Regenerable | Idéntico al regenerar con `tidy_utmb.py` | OK | Con la advertencia del orden del glob |
| B1 | Sujetos de cognición | 29 | 29 | OK | |
| B2 | Sesiones de cognición | 332 | 302 únicas (30 duplicadas de C1 en el derivado) | DISCREPANCIA | C1 aparece en el archivo "All" y en los 3 archivos por sujeto; el derivado conserva ambos |
| B3 | CPT RT PRE (ms) | 531,5 (n = 173) | 523,6 (n = 161) | DISCREPANCIA | La cifra incluye 12 sesiones duplicadas |
| B4 | CPT RT IN (ms) | 496,8 (n = 112) | 492,8 (n = 100) por etiqueta cruda; 488,3 si las 6 sesiones C1 del 7-8/9 se asignan a PRE | DISCREPANCIA | Ver B8 |
| B5 | CPT RT POST (ms) | 477,3 (n = 47) | 475,5 (n = 41) | DISCREPANCIA | Menor |
| B6 | Regla cuando hay varios runs en un día | "Se conserva el último run del día" (comentario del script) | Ningún sujeto-día tiene más de una sesión en el crudo: la regla no se activa. El código sobrescribe con la última fila leída | NO VERIFICABLE | No está documentada en LEEME. Si apareciera un día con dos sesiones, "última" sesgaría hacia la fase de práctica |
| B7 | Mapeo de columnas WinSCAT | CPT = atención continua; "búsqueda en memoria" = MTS | ReadMe del crudo: CPT = "Running Memory"; MTS = "Match to Sample (Blocks)" | DISCREPANCIA | Etiqueta en LEEME no coincide con el ReadMe. Los valores sí se mapean bien (CPTRT, MTHRT, MTSRT, CDDRT) |
| B8 | La mejora de RT entre fases es fisiológica | Implícito | Confundida con aprendizaje. Las 29 primeras sesiones son Nasa1p (con instrucciones). El RT baja con el número de sesión en 28 de 28 sujetos (mediana -10,7 ms por sesión). La mezcla de variantes cambia por fase (IN: 84 % Nasa1; PRE: 49 %) | NO VERIFICABLE | Interpretar como efecto de práctica, no como cambio fisiológico |
| B9 | Sesiones de C1 el 7 y 8 de septiembre | Fase IN | Las etiquetas WinSCAT dicen IN, pero vitales y sueño dicen PRE (6 sesiones: 3 sujetos x 2 días) | DISCREPANCIA | Afecta a la media IN (B4) |
| C1 | Eventos totales | 132 | 132 en CFT70. El crudo tiene 1.053 (132 + 921 de C3) | DISCREPANCIA | El glob `CRF_*SYMPTOM*` no incluye `CRF_Campaign_3_Symptom_Complaint` |
| C2 | Top síntomas | Pain 42, Other 41, Sleeping Difficulty 23, Dry Skin 19, Headache 6, Dizziness 1 | Idéntico para CFT70 | OK | Solo sobre el subconjunto incluido (ver C1) |
| C3 | Texto de acción, intervención y resultado | Se preserva | 132 de 132 coinciden (comparación por multiconjunto de textos) | OK | Se comprobaron las 132 filas, no 30 |
| C4 | Fecha de los eventos | Completa | Una fila (8936, `02/19/20131`) queda sin fecha ni `dia_mision` sin aviso | DISCREPANCIA | Probable 19/02/2013 por contexto (entre 18/02 y 24/02) |
| C5 | Eventos C3 en perfiles | Campo `eventos` | 0 para los 23 sujetos de C3 que tienen eventos en el crudo | DISCREPANCIA | Consecuencia de C1 |
| D1 | Astronautas totales | 44 (40 UTMB + 4 I4) | 44 (40 + 4) | OK | I4-C001 a I4-C004 |
| D2 | UTMB con vitales | 29 | 29 | OK | |
| D3 | UTMB sin vitales | 11 con "solo cognición o laboratorio" | 11, todos con cognición; 4 de ellos además con laboratorio | OK | Matiz: "solo cognición" es correcto para los 11 sin vitales, con laboratorio en 4 |
| D4 | Días y banderas por perfil | Correctos | 0 diferencias en días totales, días de misión, vitales, sueño y cognición | OK | |
| D5 | Bandera de laboratorio | 10 | 10 con valores numéricos en el crudo | OK | |
| D6 | Bandera de tilt | 25 sujetos con tilt | Crudo: 29 sujetos. Faltan C1G0001, C1G0002, C1G0003 y 6607 | DISCREPANCIA | Además, ningún script de `scripts/` genera `utmb_tilt_ortostatico.csv` (origen no documentado) |
| E1 | Anclaje: mediana de (fecha - BR_Day) en misión | Robusto a errores de captura | Reproducido. 39 sujetos con filas de misión (9947 solo tiene PRE) | OK | |
| E2 | Filas IN con `dia_mision` distinto de `BR_Day` | 4 ("errores de captura") | 8 de 2.209 (3985: 1; 7984: 7) | DISCREPANCIA | Recuento incorrecto. Ver E3 y E4 |
| E3 | 3985, 2007-04-08 | ¿Fecha o BR_Day mal? | Es BR_Day: vale 34 (ya usado el 3/8); debía ser 65 según 4/7 (BR 64) y 4/9 (BR 66). La fecha es correcta | OK (resuelto) | Ver detalle |
| E4 | 7984, "tres filas" | 3 | 7 filas, todas con BR_Day erróneo y fecha correcta | DISCREPANCIA | Ver detalle |
| E5 | Sueño y vitales de C1G0001-3 alineados | Sospecha de desalineación | Fecha, BR_Day y fase coinciden en el 100 % de los días compartidos | OK (sospecha no confirmada) | Hay problemas reales: 10/29/2004 sin vitales en C1G0001 y C1G0002, y los duplicados de C1G0003 (D-1) |
| E6 | Fila de vitales con año 2001 | Descartada por "fecha imposible" | La fila 2001-10-29 (BR 51) es en realidad 2004-10-29. Se descarta y el día 10/29/2004 queda sin vitales en C1G0001 y C1G0002 | DISCREPANCIA | Pérdida evitable: habría que corregir el año |
| E7 | 5788, 2007-02-27 (C3, PRE) | Un registro | Dos registros con BR 12 y BR 11. La demo conserva BR 12 | DISCREPANCIA | Menor. Fuera de misión |
| E8 | Duplicados en `utmb_vitales_diarios.csv` | Sin duplicados | 253 claves (sujeto, fecha) duplicadas: 252 de C1 (archivos por sujeto) y 1 de E7 | DISCREPANCIA | La demo deduplica (primero gana), el derivado no |
| F1 | Fórmula z y estado | z = (valor - media) / max(DE, suelo); verde < 2, amarillo 2-3, rojo >= 3 | Implementado correctamente; z de pulso, PAS, PAD, temperatura, peso y estado coinciden con el recálculo cuando hay datos | OK | Suelos de LEEME: pulso 6, PAS 8, PAD 6, temp 0,3, peso 1,0. El script usa además resp 1,5 y HRV 6, no documentados en LEEME |
| F2 | Línea base: PRE o primeros 7 días de misión si hay < 3 valores de pulso | Regla | Implementada. Hay 5 sujetos sin línea base de PAS/PAD/temp y 7 sin peso/resp | DISCREPANCIA | Consecuencia de las cabeceras no reconocidas (D-2) |
| F3 | Distribución del semáforo | 81 / 13 / 6 % | Con el derivado: 81,1 / 13,1 / 5,8 %. Con datos completos: 79,1 / 14,8 / 6,1 % | DISCREPANCIA | Las cifras reproducen el derivado, pero el derivado omite datos. 2.936 días con estado |
| F4 | No verde por fase | Pre 10 %, misión 18 %, regreso 33 % | Derivado: 10,1 / 18,1 / 32,9 %. Datos completos: 11,1 / 20,1 / 36,2 % | DISCREPANCIA | La dirección (aumento hacia el regreso) se mantiene |
| F5 | Estados que cambian al completar datos | — | 60 filas en 5 sujetos (3985, 7961, 7984, 8615, 8779) | DISCREPANCIA | Todas explicadas por datos faltantes; ninguna por la fórmula |
| F6 | Redondeo de z de temperatura | — | Diferencia máxima 0,05 z por redondeo de media y DE a 2 decimales | OK | Dentro de tolerancia |
| G1 | Columnas simuladas identificadas | `*_sim` | Cinco columnas `_sim` en `demo_diario`. Ninguna entra en z ni en estado | OK | La línea base contiene `hrv_rmssd_ms_sim_media/de`, también con sufijo `_sim` |
| G2 | Ánimo base 6,5-8 y caída hacia 75 % de misión | Regla | Base por sujeto entre 6,3 y 8,1 (ruido de muestra). Caída de -0,07 (inicio) a -1,21 (decil 7) | OK | Coherente con la regla |
| G3 | HRV inversa al pulso real | Regla | r intrasujeto mediana -0,89; 29 de 29 sujetos negativos | OK | Acoplamiento deliberado por diseño |
| G4 | SpO2 97,6 ± 0,7, recorte 93-100 | Regla | 97,59 ± 0,69; mínimo 95,2; máximo 100,0 | OK | |
| G5 | Radiación 0,4 mSv/día solo en misión | Regla | 0,4 en las 2.209 filas de misión; 0 en el resto | OK | |
| G6 | Radiación acumulada "correcta" | Acumulado de la misión | Suma solo filas observadas. En 10 sujetos hay menos filas de misión que días de misión (p. ej. UTMB-02: 2 filas frente a 29 días = 0,8 frente a 11,6 mSv) | DISCREPANCIA | Cumple su definición, no la del escenario |
| G7 | Sin fuga de simulados a columnas reales | No hay fuga | Recalculo de todas las columnas reales sin simulados coincide con el derivado, salvo las diferencias por D-2 y D-1 | OK | |
| G8 | Límite de carrera 600 mSv | Citado | Citado en FUENTES.md como verificado contra `radiation_cancer_2026.pdf` p. 43 | NO VERIFICABLE | El PDF no se abrió en esta auditoría |
| H1 | `build_demo.py` reproducible | Regenerable | 6 archivos de `demo/` byte a byte idénticos en copia | OK | |
| H2 | `tidy_utmb.py` reproducible | Regenerable | 5 `utmb/*.csv` idénticos en este sistema | OK | Depende del orden del glob (no ordenado) |
| H3 | Conteos de LEEME | 3.032 / 40 / 3.100 / 132 / 44 | 3.032 / 40 / 3.100 / 132 / 44 | OK | Los conteos coinciden; la calidad de contenido no (ver C1, D-1) |
| H4 | Resumen por fase: n de vitales | Sin especificar | Inflado por 253 duplicados (p. ej. HR PRE 426 frente a 395 únicos) | DISCREPANCIA | Ver I1 |
| H5 | Resumen por fase: p95 | Sin especificar | Usa `statistics.quantiles` con método exclusivo. Extrapola fuera del rango: hemoglobina POST p95 = 182,34 con máximo 131 | DISCREPANCIA | Ver I2 |
| H6 | Valores no fisiológicos en el derivado | Anulados ("fuera de rango") | `utmb_vitales_diarios.csv` conserva pulso 16 lpm y peso 0 kg (2 filas). La demo los anula; el resumen no. Los valores crudos de respiración 116 y 56 rpm no llegan al derivado por la cabecera (D-2) | DISCREPANCIA | Menor |

---

## Detalles

### D-1. Sueño de C1G0003 (archivo A frente a archivo de consulta B)

- El archivo A (`BRSMACT_Campagin_1_Actigraphy`, 207 filas) tiene una fila por noche y 3 sujetos. 17 filas son `No Data` (7 de C1G0002 y 10 de C1G0003).
- El archivo B (`..._Query_Result`, 191 filas) incluye C1G0002 (6 noches idénticas a A) y C1G0003 (185 filas). En C1G0003 hay 66 de sus 69 noches con 2 o 3 registros y numeración `Record Number` distinta.
- **Serie de registros 4019-4089 en B:** 68 de 69 noches coinciden exactamente (latencia, duración y eficiencia) con las de C1G0001 en la misma fecha. Es muy improbable por azar, así que sugiere una mezcla de sujetos en la extracción de la consulta. Conviene consultar al responsable de los datos.
- **Serie 4208-4324 en B:** coincide con A en todas las noches de C1G0003 con valor (9/17 a 11/14).
- **Resultado en el derivado:** `tidy_utmb.py` recorre primero el archivo B (el glob no está ordenado), así que para C1G0003 el registro retenido es el primero de B, no el de A.
  - 29 noches con valor en A quedan reemplazadas por un registro de B.
  - 10 noches `No Data` se rellenan con el primer registro de B.
  - 11 noches del derivado son copias exactas de C1G0001 en la misma fecha: 9/7, 9/8, 9/9, 9/11, 9/13, 9/15, 10/4, 10/6, 11/9, 11/11 y 11/13.
- **Impacto:** PRE tiene 2 noches únicas (ambas de C1G0001), no 4. Las medias de IN y POST cambian ligeramente (ver A5, A6, A9, A10).

### D-2. Vitales de C3: cabeceras no reconocidas

Los archivos afectados son C3A_0224 y C3A_0446 (peso y respiración), y C3D_3985, 7961, 7984, 8615 y 8779 (PAS, PAD, temperatura, peso y respiración). `tidy_utmb.py` solo busca `Blood Pressure, diastolic` / `DiaBP (mmHg)`, `Resp Rate (rpm)` / `Respiration rate (rpm)`, `Weight (Kg)` / `Weight (kg)` y `Body Temp (Celsius)` / `Temperature, body (Celsius)`. Las variantes `SysBP`, `DiaBP`, `Body Temp`, `Weight` y `Respiration rate` (sin unidad) no se leen.

| Variable | Días con valor en el crudo y vacío en el derivado |
|---|---|
| PAS / PAD | 582 (5 archivos C3D) |
| Temperatura | 582 (5 archivos C3D) |
| Respiración | 809 (2 archivos C3A + 5 C3D) |
| Peso | 801 (2 archivos C3A + 5 C3D) |

### E-1. Anclaje de misión y BR_Day

- Anclaje: mediana sobre las filas de misión de (fecha - BR_Day). Se reproduce con los mismos resultados. Cada sujeto tiene un desfase modal constante, salvo las filas erróneas.
- Las 8 filas IN con `dia_mision != BR_Day` son todas errores en BR_Day. En cada caso, la fecha es coherente con sus vecinos (sin huecos ni duplicados de fecha), y el BR_Day no lo es:

| Sujeto | Fecha | BR_Day en crudo | BR_Day esperado (vecinos) | Observación |
|---|---|---|---|---|
| 3985 | 2007-04-08 | 34 | 65 | 34 ya existe el 2007-03-08; 4/7 es BR 64 y 4/9 es BR 66 |
| 7984 | 2007-02-24 | 1 | 13 | 2/23 es BR 12 y 2/25 es BR 14 |
| 7984 | 2007-03-09 | 5 | 26 | 3/8 es BR 25 y 3/10 es BR 27 |
| 7984 | 2007-03-16 | 34 | 33 | 3/15 es BR 32; 3/17 es BR 34 |
| 7984 | 2007-03-20 | 36 | 37 | 3/19 es BR 36 (repetido) |
| 7984 | 2007-03-21 | 37 | 38 | Desfase de un día hasta 3/23 |
| 7984 | 2007-03-22 | 38 | 39 | Idem |
| 7984 | 2007-04-21 | 59 | 69 | 4/20 es BR 68 y 4/22 es BR 70; BR 59 ya existe el 4/11 |

- `dia_mision` se calcula desde la fecha, así que es correcto en estos casos. Lo que está mal es la columna `br_day` del derivado; LEEME ya recomienda usar `dia_mision`, pero debería decirse explícitamente que `br_day` no es fiable en esas 8 filas.

### E-2. Alineación de C1G0001-3

- En los días compartidos, la fecha, el BR_Day y la fase de sueño coinciden con los vitales (0 diferencias en los 3 sujetos): 69 de 69 noches en C1G0003 y 68 de 69 en C1G0001 y C1G0002.
- Días sin vitales que sí tienen sueño: 10/29/2004 en C1G0001 y C1G0002. En vitales, esa fecha figura como `2001-10-29` (BR 51), año erróneo. El script descarta la fila porque cae fuera de rango, con lo que pierde el 10/29 de vitales en dos sujetos. C1G0003 sí tiene 10/29/2004 en vitales.
- Vitales antes de la misión (8/30 a 9/6) y después (11/15 a 11/16) no tienen sueño, que es lo esperable.
- Etiquetas WinSCAT: las sesiones de C1 del 9/7 y 9/8 (BR 2 y 1) aparecen como `IN_TEST`, pero en vitales y sueño son `PRE_TEST`. Son 6 sesiones y afectan a la media IN de cognición (B4).

### B-1. Cognición

- Sesiones únicas: 302 (C1 All: 30; C3: 272). Los 3 archivos de C1 por sujeto son subconjuntos idénticos del archivo All.
- Tabla por fase con datos únicos y sus claims:

| Variable | Fase | Claim (n) | Recalculado (n) |
|---|---|---|---|
| CPT RT (ms) | PRE | 531,5 (173) | 523,6 (161) |
| CPT RT (ms) | IN | 496,8 (112) | 492,8 (100) |
| CPT RT (ms) | POST | 477,3 (47) | 475,5 (41) |

- Efecto de práctica: todas las primeras sesiones son Nasa1p (29 de 29 sujetos). La mediana de la pendiente intrasujeto es -10,7 ms por sesión (28 sujetos con 6 o más sesiones, 100 % negativos). La diferencia IN menos PRE dentro de cada sujeto tiene mediana -25,8 ms (82 % negativa).
- Por tanto, la caída de RT entre fases no puede atribuirse a fisiología sin controlar práctica y variante de test.

### I-1 e I-2. Resumen por fase (`utmb_resumen_por_fase.csv`)

- **Duplicados:** la columna n de HR incluye 253 filas duplicadas (PRE 426 frente a 395; IN 2.356 frente a 2.176; POST 401 frente a 359). Las medias están sesgadas por el mismo motivo.
- **Cabeceras:** PAS, PAD, temperatura, respiración y peso tienen n menor por los archivos no leídos (D-2).
- **Percentiles:** `st.quantiles(vals, n=20)` usa el método exclusivo por defecto. Con n pequeño devuelve valores fuera del rango observado (hemoglobina POST: p95 = 182,34 con máximo 131; con método inclusivo sería 79,66). El método no está documentado.

### C-1. Eventos (`demo_eventos.csv`)

- `build_demo.py` busca `CRF_*SYMPTOM*` (mayúsculas). La carpeta `CRF_Campaign_3_Symptom_Complaint` no coincide, así que sus 23 archivos (921 filas, 23 sujetos) no entran.
- Las columnas de C3 difieren de CFT70 (`Symptom/Complaint` frente a `Symptom`, `Action_Taken` frente a `Action`, `Resolution` frente a `Outcome`, y algunos archivos sin `Test_Phase` ni `Comments`). Habrá que mapearlas antes de incluirlas.
- Fecha ilegible: `02/19/20131` en 8936 (registro 86137). Queda sin fecha y sin `dia_mision`.

### F-1. Semáforo

- Sobre el derivado, la fórmula reproduce `estado_vitales` sin errores (0 diferencias con su propia fuente).
- Con datos completos, cambian 60 estados. Los 5 sujetos afectados son los que perdieron PAS/PAD/temperatura en D-2.

### G-1. Simulados

- Cumplen LEEME en ánimo, HRV, SpO2 y radiación (ver tabla G2 a G5).
- Falla la definición del acumulado (G6): cuenta filas observadas en misión, no días de misión. Si el objetivo es una dosis de escenario, conviene calcularlo por `dia_mision` máximo o por días de misión transcurridos.

---

## Código corto (verificación clave)

```python
# H:MM y H:MM:SS -> horas (7:44:00 -> 7,733)
def hm_to_h(s):
    m = re.fullmatch(r'(\d+):(\d{1,2})(?::(\d{1,2}))?', s.strip())
    return int(m[1]) + int(m[2])/60 + int(m[3] or 0)/3600 if m else float(s)

# Deduplicado propuesto: A primero (fuente principal); B solo para noches NA, tras resolver la ambigüedad
sleep = {(r['Subject'], pdate(r['Date'])): r for r in A if r['Sleep Duration (hours)'] != 'NA'}
for r in sorted(B, key=lambda r: int(r['Record Number'])):          # orden explícito, no glob
    sleep.setdefault((r['Subject'], pdate(r['Date'])), r)           # solo si falta

# Glob propuesto para eventos (incluye ambas campañas, sin distinguir mayúsculas)
ev_files = [p for p in glob.glob(f'{RAW}/CRF_*', recursive=True) if 'symptom' in p.lower()]

# Anclaje (LEEME) y señalamiento de BR_Day inconsistente
first_in = {s: date.fromordinal(int(st.median(o)) + 1) for s, o in offs.items()}
bad = [(k, x['br'], x['dia_mision']) for k, x in days.items()
       if x['fase'] == 'mision' and x['dia_mision'] != int(x['br'])]     # -> 8 filas
```

---

## Acciones recomendadas (no aplicadas; no se modificó ningún archivo)

1. **Eventos:** corregir el glob de `build_demo.py` y mapear las columnas de C3 antes de regenerar. Recalcular la tabla de síntomas y los perfiles.
2. **Sueño de C1G0003:** confirmar con la fuente si la serie 4019-4089 pertenece a C1G0001. Usar A como fuente principal y no reemplazarla por B. Eliminar las 11 copias de C1G0001 o marcarlas como no fiables.
3. **Vitales:** añadir las variantes de cabecera a `tidy_utmb.py` (SysBP, DiaBP, Body Temp, Weight, Respiration rate) y regenerar `utmb_vitales_diarios.csv`, `utmb_resumen_por_fase.csv` y `demo/`. Deduplicar antes de resumir.
4. **Cognición:** deduplicar C1 (archivo All únicamente). Documentar la regla de run por día (si hay varios, ahora mismo ninguno) y no interpretar la caída de RT como fisiológica sin controlar práctica y variante.
5. **Fechas:** corregir el año 2001-10-29 a 2004-10-29 (C1G0001 y C1G0002) en lugar de descartarlo; corregir `02/19/20131`; fijar BR_Day de las 8 filas de E-1.
6. **Resumen:** usar percentiles con método inclusivo o documentarlo; no extrapolar fuera del rango.
7. **Tilt:** documentar o generar `utmb_tilt_ortostatico.csv` desde un script del repositorio e incluir C1G0001-3 y 6607.
8. **LEEME:** corregir "4 errores de captura" (son 8 en BR_Day, más 2 fechas), las etiquetas WinSCAT (CPT = Running Memory; MTS = Match to Sample), el recuento de 332 sesiones y el semáforo con datos completos.

## Limitaciones

- No se reconstruyeron los cálculos de tilt ni de laboratorio más allá de las banderas de perfil y el conteo de sujetos.
- Los percentiles de `utmb_resumen_por_fase.csv` se verificaron solo para la hemoglobina POST (método exclusivo confirmado); no se recalcularon todas las celdas.
- No se abrió `radiation_cancer_2026.pdf`.
- La verificación de la reproducibilidad de `tidy_utmb.py` depende del orden de listado del sistema de archivos, que no está garantizado.
