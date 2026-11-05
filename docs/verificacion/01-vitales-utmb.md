# Verificación independiente: vitales diarios y prueba de tilt (UTMB / NLSP)

- Fecha: 2026-11-05
- Alcance: afirmaciones (a) a (f) del informe sobre vitales diarios y tilt, y los archivos derivados `utmb/utmb_vitales_diarios.csv`, `utmb/utmb_resumen_por_fase.csv`, `utmb/utmb_tilt_ortostatico.csv`, `demo/demo_diario.csv` y `demo/LEEME.md`.
- Método: todo se recalculó desde los archivos crudos de `nlsp-raw/downloads/x/` con código propio ejecutado con `python3 -I`. No se usó ningún script de `scripts/`. No se modificó ningún archivo existente.

## 1. Resumen

El derivado de vitales **no es fiel al crudo**. Tres errores de datos afectan a todas las estadísticas declaradas:

1. **Duplicación de Campaña 1.** El derivado tiene 3,192 filas; 252 son copias exactas, porque el archivo `_All` y los `_Subject_1..3` se leyeron los dos. Registros válidos: 2,937.
2. **Columnas no reconocidas.** En 7 sujetos se pierden PAS, PAD, temperatura, peso y frecuencia respiratoria (3,356 celdas con dato crudo quedan vacías). Esto altera las medias por fase y los n.
3. **Limpieza incompleta.** Se conservan 3 valores imposibles (pulso 16, peso 0.0 en 2 filas) y 4 filas con fecha 2001 que el informe dice haber eliminado.

Las cifras del informe son aritméticamente correctas **sobre el CSV derivado**: n, media y DE se reproducen exactamente desde él. El error está aguas arriba, en el CSV. En tilt, las 74 pruebas omiten 4 pruebas válidas y `minutes_tilt` está inflado en 2 pruebas por filas vacías. La demo copia los mismos errores de vitales (3,356 celdas vacías) y de tilt.

Los checksums son correctos: los 116 MD5 de vitales y tilt coinciden, y los ZIP son idénticos a los archivos extraídos.

## 2. Tabla de verificación

"Recalculado" significa: datos crudos únicos, sin fechas de 2001, sin duplicados sujeto-día, valores fuera de rango anulados con los límites del informe y columnas mapeadas por nombre de cabecera. DE = desviación estándar muestral (n−1).

### 2.1 Sujetos y registros

| Afirmación | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Sujetos con vitales diarios | 29 | 29 (3 CFT70 + 3 Campaña 1 + 23 Campaña 3) | OK | Sin IDs repetidos entre campañas |
| Registros de vitales | 3,192 | 2,937 válidos (2,940 únicos crudos − 2 fechas 2001 − 1 duplicado sujeto-día) | DISCREPANCIA | 252 copias exactas de Campaña 1; 4 filas 2001 conservadas; 1 duplicado real conservado (D1, D4, D5) |

### 2.2 Estadística por fase (media ± DE)

| Afirmación | Valor declarado | Valor recalculado (n) | Estado | Nota |
|---|---|---|---|---|
| Pulso PRE | 68.6 ± 12.4 | 69.3 ± 12.2 (394) | DISCREPANCIA | D1, D3 |
| Pulso IN | 70.2 ± 11.7 | 70.6 ± 11.9 (2174) | DISCREPANCIA | D1, D3 |
| Pulso POST | 74.9 ± 14.1 | 76.1 ± 14.3 (359) | DISCREPANCIA | D1 (Campaña 1 duplicada pesa de más) |
| PAS PRE | 115.4 ± 10.2 | 116.0 ± 10.3 (395) | DISCREPANCIA | D2 (n 362 en derivado) |
| PAS IN | 115.9 ± 10.9 | 116.2 ± 10.9 (2182) | DISCREPANCIA | D2 (diferencia de 0.3) |
| PAS POST | 112.9 ± 11.7 | 115.0 ± 12.3 (359) | DISCREPANCIA | D2 (n 334 en derivado) |
| PAD PRE | 68.7 ± 9.9 | 70.1 ± 9.6 (395) | DISCREPANCIA | D2 |
| PAD IN | 70.5 ± 8.8 | 71.4 ± 8.7 (2182) | DISCREPANCIA | D2 |
| PAD POST | 67.7 ± 9.5 | 69.2 ± 9.7 (359) | DISCREPANCIA | D2 |
| Temperatura PRE | 36.50 ± 0.40 | 36.50 ± 0.40 (369) | OK | |
| Temperatura IN | 36.51 ± 0.40 | 36.53 ± 0.37 (2078) | DISCREPANCIA | D2 (DE) |
| Temperatura POST | 36.44 ± 0.45 | 36.49 ± 0.41 (350) | DISCREPANCIA | D2 (DE) |
| Frec. respiratoria PRE | 16.9 ± 1.6 | 16.9 ± 1.5 (394) | DISCREPANCIA | D2 (DE) |
| Frec. respiratoria IN | 16.7 ± 1.6 | 16.9 ± 1.6 (2177) | DISCREPANCIA | D2 |
| Frec. respiratoria POST | 16.7 ± 1.7 | 17.0 ± 1.7 (358) | DISCREPANCIA | D2 |

Nota: las cifras declaradas se reproducen exactamente desde `utmb_vitales_diarios.csv` (n, media y DE, a 2 decimales). Por tanto la discrepancia viene del CSV, no del paso de resumen (D11).

### 2.3 Percentiles P5–P95 durante IN

| Variable | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Pulso | 53–92 | 52.7–92.0 (≈ 53–92) | OK | |
| PAS | 99–135 | 99–135 | OK | |
| PAD | 56–86 | 57–86 | DISCREPANCIA | P5 depende de los datos: el CSV derivado da 56 |
| Temperatura | 35.8–37.1 | 35.9–37.1 | DISCREPANCIA | El CSV derivado da 35.8 |
| Frec. respiratoria | 14–20 | 14–20 | OK | |

Nota: la interpolación tipo 7 y el rango más próximo dan los mismos valores sobre datos limpios. El resumen derivado usa otra convención para P5/P95 (diferencias de hasta 0.25 frente a tipo 7 sobre el mismo CSV, por ejemplo pulso IN P5 = 52.85 en el resumen y 53.0 recalculado sobre el CSV). No es material.

### 2.4 Cambio individual (media IN − media PRE por sujeto)

| Variable | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Pulso | +1.5 ± 4.4 (rango −4.7 a +11.3) | +1.3 ± 4.5 (rango −4.8 a +11.3), n = 29 | DISCREPANCIA | Menor. El informe reproduce el CSV derivado (+1.48 ± 4.37), que conserva el pulso 16 de CFT70 8072 (D3) |
| PAS | −0.2 ± 4.9 | −0.2 ± 4.8, n = 29 | DISCREPANCIA | Menor. Sobre el CSV derivado sólo hay n = 24 (faltan 5 sujetos, D2) |
| Peso | −1.1 ± 1.1 kg | −1.1 ± 1.1 kg, n = 29 | OK | Sobre el CSV derivado sólo n = 22; el valor redondeado coincide |
| Temperatura | +0.03 ± 0.11 °C | +0.03 ± 0.11 °C, n = 29 | OK | |

### 2.5 Prueba de tilt

Se recalcularon las pruebas de Campaña 3 con HR utilizable (columna `HR`, o `HR (Dinamap)` cuando es la única). Estado según el conjunto correcto (78 pruebas, minutos corregidos). Entre paréntesis, el valor con el conjunto de 74 pruebas del derivado.

| Afirmación | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Número de pruebas | 74 | 78 con HR utilizable (C3) | DISCREPANCIA | D7. Excluidas 2 sin HR (D7). Campaña 1 (10 pruebas) no verificable (D8) |
| ΔHR supino→tilt PRE | +34.7 bpm | +34.1 bpm (n = 26) (con 74: +34.7) | DISCREPANCIA | D7 (4 pruebas Dinamap omitidas) |
| ΔHR IN | +56.9 bpm | +56.9 bpm (n = 11) (con 74: +56.9) | OK | |
| ΔHR POST | +43.8 bpm | +43.8 bpm (n = 41) (con 74: +43.8) | OK | |
| Minutos de tilt PRE | 22.2 | 22.7 (n = 26) (con 74 y minutos corregidos: 22.1) | DISCREPANCIA | D6, D7 |
| Minutos de tilt POST | 20.3 | 20.4 (n = 41) (con 74: 20.3) | DISCREPANCIA | Menor. D7 |

Nota: el derivado reproduce exactamente sus propios valores (ΔHR 34.67 / 56.89 / 43.77; minutos 22.21 / 20.31) con el HR de la columna `HR` (no con `AVE HR`, que no coincide en 73 de 74 pruebas). El mapeo de HR es correcto; el problema está en la selección y en el conteo de minutos.

### 2.6 `demo/demo_diario.csv` y `demo/LEEME.md`

| Afirmación | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Valores iguales al crudo (mismo sujeto y fecha) | Sí | 2,937 días casados (todas las filas). Pulso idéntico en todas las celdas pobladas. PAS, PAD, temperatura, FR y peso: 3,356 celdas vacías donde el crudo tiene valor | DISCREPANCIA | D2 (la demo hereda el mapeo erróneo) |
| Conversión Fahrenheit→Celsius correcta | Sí | No se ejercita: 1,987 filas sólo Celsius, 811 con ambas (diferencia máxima 0.04 °C), 0 sólo Fahrenheit | NO VERIFICABLE | La ruta de conversión nunca se usa en estos datos |
| Valores fuera de rango anulados | Sí | Demo: correcto (0 valores fuera de rango; pulso 16 y peso 0.0 anulados). Derivado: no (D3) | OK (demo) / DISCREPANCIA (derivado) | |
| 2 filas eliminadas por fecha imposible | Sí (una de 2001) | Derivado: no, 4 filas 2001 presentes (D4). Demo: el día se conserva pero los vitales de esos 2 días quedan vacíos | DISCREPANCIA (derivado) / parcial (demo) | Crudo: 2 filas con 2001 (C1G0001 y C1G0002) |
| Columnas de tilt en la demo | 74 pruebas | 73 pruebas; los 73 valores coinciden con el derivado (incluidos los minutos erróneos de D6) | DISCREPANCIA | Falta 7127 IN BR50 (D9) |
| Número de filas | 3,032 | 3,032 | OK | 2,937 con vitales y 95 días sin vitales (de otras fuentes) |
| Sujetos UTMB | 40 (29 con vitales) | 40 (29 con vitales) | OK | |

### 2.7 Duplicados, unidades y mezcla de campañas

| Afirmación | Valor declarado | Valor recalculado | Estado | Nota |
|---|---|---|---|---|
| Duplicados sujeto-día | No se declara (sólo se pide verificar) | 252 filas exactas (Campaña 1) y 1 duplicado real (C3A_5788, 2005-02-27) | DISCREPANCIA | D1, D5 |
| Mezcla de campañas | No se declara | Ningún ID numérico aparece en más de una campaña. Letras de campaña de vitales y tilt coinciden en los 22 sujetos compartidos | OK | |
| Unidades | No se declara | Peso C1 en kg; "Weight" de C3 sin unidad = kg (rango 40.7–108.6, sin contar los 0.0 de D3); "Body Temp" = °C (34–38); Fahrenheit coherente con Celsius | OK | Unidades inferidas: no hay ReadMe para estas tablas |
| Fechas tilt vs vitales (mismo sujeto, fase y BR) | No se declara | 67 coinciden; 8 no coinciden (una con año 2010 frente a 2009) | NO VERIFICABLE | Inconsistencia entre fuentes crudas. El derivado de tilt no tiene fechas (D10) |
| Archivo "HR" de Campaña 1 | No se declara | `MR001G_Campaign_1_Tilt_HR` es idéntico a `_DBP` (173 de 173 filas). Su cabecera es "DBP" | DISCREPANCIA (cruda) | D8 |

### 2.8 Integridad de archivos

| Verificación | Valor recalculado | Estado | Nota |
|---|---|---|---|
| MD5 de vitales y tilt | 116 entradas (CFT70 3, Campaña 1 4, Campaña 3 23, tilt C1 6, tilt C3 80): 116 OK, 0 fallos | OK | Rutas relativas a la carpeta que contiene el `.md5sum` |
| ZIP frente a archivos extraídos | 5 ZIP (4, 5, 24, 7 y 81 miembros): todos idénticos byte a byte | OK | |
| ReadMe de vitales y tilt | No existe ninguno. Los ReadMe presentes describen laboratorio, DXA, actigrafía y WinSCAT | NO VERIFICABLE | Unidades y significado de columnas inferidos de los rangos |

## 3. Discrepancias en detalle

### D1. Duplicación de Campaña 1: 252 filas (alta)
- Causa: `CRF_Campaign_1_Daily_Vitals_All` tiene exactamente los mismos 252 registros que `_Subject_1`, `_Subject_2` y `_Subject_3` (comparados valor a valor, ignorando la columna ID). El derivado los incluye dos veces.
- Ejemplo: C1G0001, 8/30/2004, PRE_TEST, BR 10, pulso 62, PAS 108, PAD 68, FR 18. Aparece 2 veces en `utmb_vitales_diarios.csv`. En crudo: `_All` línea 2 y `_Subject_1` línea 2.
- Efecto: el derivado tiene 60 filas PRE de Campaña 1 en lugar de 30, y 3,192 registros en lugar de 2,940 únicos.

### D2. Columnas no mapeadas: 3,356 celdas con dato crudo quedan vacías (alta)
- Causa: el derivado sólo reconoce las cabeceras `SysBP (mmHg)`, `DiaBP (mmHg)`, `Resp Rate (rpm)`, `Body Temp (Celsius)` y `Weight (Kg)`. Estos archivos usan otras cabeceras:
  - `CRF_Campaign_3_Daily_Vitals_C3D_3985`, `_C3D_7961`, `_C3D_7984`, `_C3D_8615`, `_C3D_8779`: `SysBP`, `DiaBP`, `Resp Rate`, `Body Temp`, `Weight`. El derivado deja vacíos PAS (582), PAD (582), temperatura (582), FR (580) y peso (582).
  - `CRF_Campaign_3_Daily_Vitals_C3A_0224` y `_C3A_0446`: `Respiration rate` y `Weight`. El derivado deja vacíos FR (229) y peso (219).
  - Totales: PAS 582, PAD 582, temperatura 582, FR 809, peso 801 = 3,356 celdas.
- Ejemplos:
  - C3D_8779, 2007-04-16, PRE_TEST (línea 2 del crudo): SysBP 131, DiaBP 89, Resp Rate 20, Body Temp 36.9, Weight 91.03. Derivado: PAS, PAD, FR, temperatura y peso vacíos. El pulso sí aparece, porque `Pulse` sí se mapeó.
  - C3A_0224, 2005-02-24, PRE_TEST (línea 2): Respiration rate 18, Weight 91.18. Derivado y demo: vacíos.
- Efecto: 7 sujetos (224, 446, 3985, 7961, 7984, 8615, 8779) pierden parte de sus días. Esto explica las diferencias de n y de media en 2.2 y 2.4.

### D3. Valores fuera de rango conservados en el derivado (media)
- CFT70 8072, 2013-01-26, PRE_TEST (línea 13 del crudo): pulso 16. Derivado `hr_bpm` = 16.0. Límite del informe: 30–200.
- C3E_6607, 2008-08-24, POST_TEST (línea 108): peso 0.0. Derivado `weight_kg` = 0.0.
- C3E_6607, 2008-08-26, POST_TEST (línea 109): peso 0.0. Derivado `weight_kg` = 0.0.
- La demo sí los anula. Las FR de 116 (C3A_0224, 2005-03-05) y 56 (C3D_7984, 2007-03-22) están vacías en el derivado sólo por D2, no por la regla.

### D4. Fechas imposibles no eliminadas (media)
- El informe afirma 2 filas eliminadas por fecha imposible, una de 2001. El crudo tiene 2 filas con fecha 2001: C1G0001 y C1G0002, ambas 10/29/2001, IN_TEST, BR 51 (línea 62 de `_Subject_1` y de `_Subject_2`). Las fechas vecinas son 10/28/2004 y 10/30/2004, así que es casi seguro un error de tecleo en el año.
- El derivado conserva las 4 filas (2 filas × 2 copias por D1).
- La demo conserva el día 2004-10-29 con los vitales vacíos.

### D5. Duplicado real sujeto-día: C3A_5788, 2005-02-27 (baja)
- Dos filas PRE_TEST con valores idénticos (pulso 55, PAS 103, PAD 56, temperatura 36.4). Difieren sólo en BR_Day: 12 (línea 2) y 11 (línea 3).
- El derivado conserva las dos; la demo conserva una. Hay que confirmar con el equipo de datos cuál es la correcta.

### D6. `minutes_tilt` inflado por filas vacías etiquetadas "Tilt" (media)
- `MR001G_Campaign_3_Tilt_C3A_224_BR61` (IN_TEST, sujeto 224): 30 filas Tilt con datos y 8 filas vacías con Stage = "Tilt" (líneas 54–61). Derivado: 38 minutos. Correcto: 30. La demo también tiene 38.
- `MR001G_Campaign_3_Tilt_C3A_992_BR-4` (PRE_TEST, sujeto 992): 30 filas con datos y 3 vacías (líneas 59–61). Derivado: 33. Correcto: 30. La demo también tiene 33.
- Efecto: la media PRE de minutos pasa de 22.21 a 22.08 sobre las 74 pruebas.

### D7. Pruebas tilt válidas omitidas: columna `HR (Dinamap)` (alta para tilt)
- Cuatro pruebas tienen la columna de HR llamada `HR (Dinamap)` con todos sus minutos. El derivado las omite sin avisar:
  - `MR001G_Campaign_3_Tilt_C3E_6043_BR-5` (PRE, ΔHR +25.5, 30 min)
  - `MR001G_Campaign_3_Tilt_C3E_6607_BR+0` (POST, ΔHR +54.5, 14 min)
  - `MR001G_Campaign_3_Tilt_C3E_6607_BR+3` (POST, ΔHR +35.4, 30 min)
  - `MR001G_Campaign_3_Tilt_C3E_6607_BR-5` (PRE, ΔHR +28.1, 30 min)
- Pruebas excluidas legítimamente: `C3A_5788_BR90` (HR = NA en todas las filas) y `C3A_992_BR+0` (sin columna HR).
- Efecto: ΔHR PRE pasa de +34.7 (74 pruebas) a +34.1 (78). Minutos PRE pasan de 22.2 a 22.7.
- Criterio del auditor: `HR (Dinamap)` se trata como HR válido. Si el equipo considera que no es comparable, habría que documentarlo.

### D8. El archivo "HR" de Campaña 1 contiene DBP (alta en crudo; sin efecto en el derivado)
- `MR001G_Campaign_1_Tilt_HR` tiene la cabecera `DBP` y valores idénticos a `MR001G_Campaign_1_Tilt_DBP` en 173 de 173 filas. No existe FC de Campaña 1 en el crudo.
- El derivado excluye las 10 pruebas de Campaña 1 sin aviso. No hay discrepancia numérica en el informe porque éste sólo cita Campaña 3, pero la FC de Campaña 1 no es verificable.

### D9. Demo: prueba tilt 7127 IN BR50 omitida (baja)
- 7127, 9/20/2005, IN_TEST, BR 50: ΔHR +60.1 y 12 minutos en el derivado. La demo no tiene ninguna fila de 7127 en esa fecha, así que el valor se pierde.

### D10. Fechas de tilt inconsistentes con las de vitales (baja, cruda)
- Ocho pruebas no coinciden con la fecha de vitales del mismo sujeto, fase y BR_Day:
  - C3D_7961 BR60: tilt 3/11/2007, vitales 3/30/2007
  - C3G_9139 BR+0: tilt 5/17/2010, vitales 5/17/2009 (año)
  - C3G_5580 BR-5: tilt 3/24/2009, vitales 3/25/2009
  - C3G_5814 BR+0: tilt 11/18/2009, vitales 11/8/2009
  - C3G_6858 BR-5: tilt 5/18/2009, vitales 5/21/2009
  - C3G_9032 BR-5: tilt 4/7/2009, vitales 4/9/2009
  - C3G_9139 BR-5: tilt 3/11/2009, vitales 3/13/2009
  - C3G_9314 BR+7: tilt 5/25/2009, vitales 5/29/2009
- El derivado de tilt no tiene fechas, así que no lo propaga. Aun así, indica errores de captura en una de las dos fuentes.

### D11. Resumen derivado: consecuencia de D1–D3 (informativa)
- Las n, medias y DE de `utmb_resumen_por_fase.csv` se reproducen exactamente desde `utmb_vitales_diarios.csv`. El resumen es coherente con su CSV; el error está antes.
- P5/P95 del resumen usan una convención no identificada (diferencias de hasta 0.25 respecto a tipo 7). No es material.

### Observaciones sin discrepancia
- Prueba tilt `C3G_9032_BR+0` (POST): tiene sólo 1 minuto de tilt y ΔHR −28.0. Está en el derivado, es una prueba incompleta y conviene marcarla como valor atípico.
- Un ΔHR de 18.2 en el derivado (9314 PRE BR8) frente a 18.3 recalculado es redondeo de 0.1 bpm, no un error.

## 4. Verificación de checksums

- 116 entradas MD5 en 5 carpetas (CFT70 3, Campaña 1 4, Campaña 3 23, tilt C1 6, tilt C3 80). Todas coinciden.
- Las rutas de los `.md5sum` son relativas a la carpeta que los contiene, no a la raíz del ZIP. Por ejemplo, `CRF_CFT70_VITALS/CRF_CFT70_VITALS_5160` se resuelve dentro de `CRF_CFT70_VITALS/`.
- Los 5 ZIP (`CRF_CFT70_VITALS.zip`, `CRF_Campaign_1_Daily_Vitals.zip`, `CRF_Campaign_3_Daily_Vitals.zip`, `MR001G_Campaign_1_Tilt.zip`, `MR001G_Campaign_3_Tilt.zip`) tienen 4, 5, 24, 7 y 81 miembros. Todos son idénticos a los archivos extraídos.

## 5. Hallazgos en los crudos (no son errores del derivado)

- Cabeceras heterogéneas. Vitales de Campaña 3: 12 variantes de cabecera (`Date` / `Test_Date` en C3C_7352; `Pulse` / `Pulse (bpm)`; `Weight` / `Weight (kg)`; etc.). Tilt de Campaña 3: 10 variantes, con orden de columnas SBP/DBP/HR distinto según el archivo, `Min` / `Minute`, `AVE HR` y `HR` juntos, `HR (Dinamap)`, y una columna `Unnamed: 14`.
- 56 filas vacías en los archivos de tilt de Campaña 3, algunas etiquetadas "Tilt".
- Minutos fraccionarios en tilt (por ejemplo 27.24 en C3A_5788_BR-4). No se usan.
- Textos como "NA" y "Not reported" en vitales (no numéricos, se tratan como vacíos).
- Vitales de Campaña 1 tienen temperatura y peso en "NA" en muchas filas (no es un error).

## 6. Código de verificación (resumen)

Script completo, autocontenido, ejecutable con `python3 -I`. Recalcula desde el crudo las cifras principales de esta sección.

```python
# Verificacion independiente: recalcula desde RAW (sin scripts del proyecto)
import csv, glob, io, os, re, math, hashlib, statistics as st
from datetime import date
RAW = "/home/user/hackathon-data/nlsp-raw/downloads/x"
DER = "/home/user/hackathon-data/utmb/utmb_vitales_diarios.csv"
def num(v):
    try: return float(v.strip())
    except (ValueError, AttributeError): return None   # NA, 'Not reported', ''
FIELDS = {"pulse": ["Pulse (bpm)", "Pulse"], "sbp": ["SysBP (mmHg)", "Blood Pressure, systolic", "SysBP"],
          "dbp": ["DiaBP (mmHg)", "Blood Pressure, diastolic", "DiaBP"],
          "resp": ["Resp Rate (rpm)", "Respiration rate (rpm)", "Respiration rate", "Resp Rate"],
          "wt": ["Weight (Kg)", "Weight (kg)", "Weight"], "tc": ["Body Temp (Celsius)", "Temperature, body (Celsius)", "Body Temp"]}
LIM = {"pulse": (30, 200), "sbp": (70, 220), "dbp": (35, 140), "resp": (6, 40), "tc": (34, 40.5), "wt": (30, 200)}
# 1) MD5 de todos los .md5sum de vitales y tilt (rutas relativas a la carpeta del .md5sum)
bad = 0
TILT_SETS = ["CRF_CFT70_VITALS", "CRF_Campaign_1_Daily_Vitals", "CRF_Campaign_3_Daily_Vitals", "MR001G_Campaign_1_Tilt", "MR001G_Campaign_3_Tilt"]
for md in [m for t in TILT_SETS for m in glob.glob(RAW + "/" + t + "/*.md5sum")]:
    for line in open(md):
        h, rel = line.split(None, 1)
        bad += hashlib.md5(open(os.path.join(os.path.dirname(md), rel.strip()), "rb").read()).hexdigest() != h
print("md5 fallos:", bad)
# 2) Registros crudos unicos (C1 '_All' excluido: es copia de Subject_1..3)
rows = []
for camp, pat in [("CFT70", "CRF_CFT70_VITALS/*/*"), ("C1", "CRF_Campaign_1_Daily_Vitals/*/*Subject*"), ("C3", "CRF_Campaign_3_Daily_Vitals/*/*")]:
    for f in sorted(glob.glob(RAW + "/" + pat)):
        for r in csv.DictReader(io.StringIO(open(f, encoding="utf-8-sig", newline="").read())):
            col = lambda k: next((c for c in FIELDS[k] if c in r), None)
            m, d, y = r[next(c for c in ("Date", "Test_Date") if c in r)].split("/")
            tc = num(r[col("tc")]) if col("tc") else None
            rows.append(dict(camp=camp, subj=r["Subject"].strip(), dt=date(int(y), int(m), int(d)), file=os.path.basename(f), phase=r["Test_Phase"],
                             **{k: (lambda v, k=k: v if v is not None and LIM[k][0] <= v <= LIM[k][1] else None)(num(r[col(k)]) if col(k) else None)
                                for k in FIELDS if k != "tc"}, tc=tc if tc is not None and LIM["tc"][0] <= tc <= LIM["tc"][1] else None))
print("registros crudos unicos:", len(rows), "| anios 2001:", sum(r["dt"].year == 2001 for r in rows))
ok = [r for r in rows if r["dt"].year != 2001]
seen, uniq = set(), []
for r in ok:
    k = (r["camp"], r["subj"], r["dt"])
    if k not in seen: seen.add(k); uniq.append(r)
print("validos sin duplicados sujeto-dia:", len(uniq), "| sujetos:", len({(r['camp'], r['subj']) for r in uniq}))
# 3) Estadistica por fase (media, DE muestral, n) sobre datos limpios
for var in ["pulse", "sbp", "dbp", "tc", "resp", "wt"]:
    out = []
    for ph in ["PRE_TEST", "IN_TEST", "POST_TEST"]:
        xs = [r[var] for r in uniq if r["phase"] == ph and r[var] is not None]
        out.append(f"{ph[:3]} n={len(xs)} {st.mean(xs):.2f}+-{st.stdev(xs):.2f}")
    print(f"{var:6s}", " | ".join(out))
# 4) Problemas en el derivado
der = list(csv.DictReader(open(DER, encoding="utf-8-sig")))
print("derivado filas:", len(der), "| duplicadas exactas:", len(der) - len({tuple(d.values()) for d in der}),
      "| filas con anio 2001:", sum(d["date"].endswith("2001") for d in der))
print("derivado sbp vacio en Campana 3 (incluye 582 por D2 y 1 'Not reported'):", sum(1 for d in der if d["sbp_mmhg"] == "" and d["campaign"] == "C3"))
print("derivado peso<30 o pulso<30:", [(d["subject"], d["date"], d["weight_kg"], d["hr_bpm"]) for d in der if (d["weight_kg"] and float(d["weight_kg"]) < 30) or (d["hr_bpm"] and float(d["hr_bpm"]) < 30)])
```

Salida de esta ejecución:

```
md5 fallos: 0
registros crudos unicos: 2940 | anios 2001: 2
validos sin duplicados sujeto-dia: 2937 | sujetos: 29
pulse  PRE n=394 69.26+-12.23 | IN_ n=2174 70.63+-11.91 | POS n=359 76.05+-14.26
sbp    PRE n=395 116.01+-10.35 | IN_ n=2182 116.17+-10.86 | POS n=359 114.99+-12.33
dbp    PRE n=395 70.05+-9.61 | IN_ n=2182 71.43+-8.72 | POS n=359 69.16+-9.70
tc     PRE n=369 36.50+-0.40 | IN_ n=2078 36.53+-0.37 | POS n=350 36.49+-0.41
resp   PRE n=394 16.91+-1.48 | IN_ n=2177 16.93+-1.63 | POS n=358 16.99+-1.71
wt     PRE n=377 74.96+-14.60 | IN_ n=2159 73.99+-15.00 | POS n=357 73.20+-14.08
derivado filas: 3192 | duplicadas exactas: 252 | filas con anio 2001: 4
derivado sbp vacio en Campana 3 (incluye 582 por D2 y 1 'Not reported'): 583
derivado peso<30 o pulso<30: [('6607', '8/24/2008', '0.0', '82.0'), ('6607', '8/26/2008', '0.0', '83.0'), ('8072', '1/26/2013', '70.95', '16.0')]
```

Las comparaciones fila a fila (2,940 filas crudas contra las 3,192 del derivado, y 2,937 días de la demo contra el crudo) y las de tilt (80 archivos contra las 74 pruebas del derivado) se ejecutaron con scripts de trabajo en `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/`, principalmente `compare_derived.py`, `mismatch_breakdown.py`, `demo_check.py`, `tilt_check.py`, `tilt_compare2.py` y `tilt_claims.py`.

## 7. Supuestos y limitaciones

- Límites de anulación: inclusivos, según el informe. Ningún valor cae exactamente en el borde.
- DE muestral (n−1). Coincide con el resumen derivado.
- Percentiles: interpolación tipo 7. Coincide con el rango más próximo sobre datos limpios.
- Duplicado C3A_5788 (D5): para la estadística se conservó una fila; los valores son idénticos.
- Pruebas `HR (Dinamap)` tratadas como HR válido (D7). Es un criterio del auditor.
- Minutos de tilt = número de filas Tilt con datos. No se usó el valor máximo de la columna `Min`, porque algunos valores son fraccionarios.
- Unidades de las tablas de vitales y tilt inferidas de los rangos (no hay ReadMe). Las inferencias son coherentes, incluido el peso en kg de Campaña 3.
- No se verificaron las demás columnas de la demo (sueño, cognición, z-scores, `estado_vitales`, `_sim`), porque no forman parte de las afirmaciones pedidas.
- No se verificó el resumen de otras tablas (laboratorio, sueño, cognición).

## 8. Archivos

- Este informe: `/home/user/hackathon-data/verificacion/01-vitales-utmb.md`
- Scripts de trabajo (fuera del proyecto): `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/`
- Ningún archivo existente fue modificado.
