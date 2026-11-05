# NLSP: datos abiertos de reposo en cama de UTMB (verificado y corregido el 2026-11-05)

**Hallazgo clave:** el NASA Life Sciences Portal tiene **30 experimentos de reposo en cama de UTMB marcados como públicos**: 28 con "All datasets are publicly available" y 2 en parte (950b2ce4… y 26a8b51f…). Se descargan sin iniciar sesión. Son datos reales por sujeto del análogo terrestre oficial de NASA para la microgravedad: 60–70 días con la cabeza inclinada 6° hacia abajo, en las campañas 1, 3 y 11 (CFT70). Algunas fichas también incluyen la campaña 5.

La auditoría independiente (`verificacion/01`–`04`) confirmó que los archivos son auténticos: las nuevas descargas son idénticas, los MD5 coinciden y los 48 DOIs resuelven al experimento correcto. También encontró **errores en mi procesamiento**, ya corregidos en `scripts/build_all.py`. Las cifras de abajo son las corregidas.

## Cómo se accede
- Ficha: `https://nlsp.nasa.gov/explore/data/details/<GUID>?dataType=EXPERIMENTS`, sección "Open-Access Data", botón Download (página con JavaScript; se automatizó con Playwright: `scripts/dl_many.js`, `scripts/list_ds.js`).
- Metadatos (JSON público): `https://nlsp.nasa.gov/api/v1/data/experiments/<GUID>/full`. El campo `archive_status` dice si los datos son públicos.
- Licencia: NLSP no publica una licencia explícita (el pie de página dice "All rights reserved"). Hay que citar el DOI de cada experimento.

## Tablas procesadas (`utmb/`, generadas por `scripts/build_all.py`)

| Tabla | Origen (DOI) | Contenido | Tamaño |
|---|---|---|---|
| `utmb_vitales_diarios.csv` | Case Report Form (10.83263/wjw1-ta27) | Pulso, presión, respiración, temperatura, peso diarios | 2.939 días, 29 sujetos |
| `utmb_laboratorio.csv` | Clinical Laboratory Assessment (10.83263/rank-k271) | Hemograma, química, PCR, orina, electroforesis; con `marca_origen` | 8.036 valores, 31 sujetos |
| `utmb_cognicion_winscat.csv` | WinSCAT (10.83263/sbne-th55) | Memoria de trabajo, matemática, emparejamiento, código diferido | 302 sesiones, 29 sujetos |
| `utmb_sueno_actigrafia.csv` | Actilight (10.83263/v7n1-ht75) | Duración, eficiencia, latencia | 190 noches, 3 sujetos |
| `utmb_tilt_ortostatico.csv` | Response to Tilt (10.83263/gz1q-a824) | Pulso y PAS acostado frente a inclinado (solo campaña 3) | 78 pruebas |
| `utmb_resumen_por_fase.csv` | Todas | n, media, DE, P5 y P95 (percentiles inclusivos) por fase | — |
| `utmb_cambio_individual.csv` | Vitales | Cambio por sujeto, promedio en misión menos promedio previo | — |
| `registro_correcciones.csv` | — | Duplicados, fechas corregidas, valores imposibles, archivos omitidos | 45 registros |

## Resultados corregidos

| Variable | Antes del reposo | Durante | Después | P5–P95 durante |
|---|---|---|---|---|
| Pulso en reposo (lpm) | 69,3 ± 12,2 | 70,6 ± 11,9 | **76,1 ± 14,3** | 53–92 |
| Presión sistólica (mmHg) | 116,0 ± 10,4 | 116,2 ± 10,9 | 115,0 ± 12,3 | 99–135 |
| Presión diastólica (mmHg) | 70,1 ± 9,6 | 71,4 ± 8,7 | 69,2 ± 9,7 | 57–86 |
| Temperatura (°C) | 36,50 ± 0,40 | 36,53 ± 0,37 | 36,49 ± 0,41 | 35,9–37,1 |
| Respiración (rpm) | 16,9 ± 1,5 | 16,9 ± 1,6 | 17,0 ± 1,7 | 14–20 |
| Sueño (h, 3 sujetos) | solo 2 noches | 7,20 ± 0,53 | 7,40 ± 0,40 | 6,1–7,7 |
| Eficiencia del sueño (%) | solo 2 noches | 81,7 ± 8,5 | 83,3 ± 5,8 | 66–93 |
| Latencia del sueño (min) | solo 2 noches | 43 ± 32 | 33 ± 24 | 12–110 |
| Glucosa (mg/dL, 31 sujetos) | 81,4 ± 6,9 | 81,3 ± 6,6 | 82,9 ± 8,0 | 71–89 |
| Hemoglobina (g/dL) | 14,6 ± 1,5 | 14,9 ± 1,8 | 14,3 ± 1,9 | 12,1–17,7 |

**Cambio individual** (promedio en misión menos promedio previo, por sujeto):
- Pulso: +1,3 ± 4,5 lpm (rango −4,8 a +11,3; 29 sujetos).
- Presión sistólica: −0,2 ± 4,8 mmHg.
- Presión diastólica: +1,0 ± 5,1 mmHg.
- Peso: −1,1 ± 1,1 kg.
- Temperatura: +0,04 ± 0,12 °C. **No respalda** un alza de 1 °C.

**Prueba de tilt** (campaña 3, 78 pruebas): el pulso sube **+34,1 lpm** al inclinarse antes del reposo, **+56,9** durante y **+43,8** al terminar. Los minutos inclinados con dato son 22,5 antes, 15,5 durante y 20,1 después.

**Cognición:** los tiempos de reacción bajan en cada fase; en memoria de trabajo, de 524 a 493 y a 475 ms. La auditoría muestra que coincide con un **efecto de práctica**, unos −10,7 ms por sesión, así que no es evidencia de mejora fisiológica.

## Uso en la app
1. **Línea base personal y umbrales:** la variabilidad entre días de una misma persona permite definir "amarillo" como más de 2 DE respecto de su propia línea base.
2. **Datos sintéticos realistas:** muestrear trayectorias reales en lugar de inventarlas.
3. **Modo demo con datos reales:** `demo/` (ver `demo/LEEME.md`).
4. **Módulo ortostático** para la readaptación a la gravedad.
5. **Check cognitivo** con WinSCAT, controlando el número de sesión.

## Cuidados
- Son análogos terrestres, no vuelo.
- Problemas en el origen: en la campaña 1, el archivo de pulso del tilt es idéntico al de presión diastólica, así que se excluye. Hay 8 pruebas de tilt con fechas distintas a las de los vitales y algunos BR_Day mal tipeados.
- El texto libre de los síntomas de la campaña 3 contiene nombres de personal; hay que anonimizarlo antes de una demo pública.
