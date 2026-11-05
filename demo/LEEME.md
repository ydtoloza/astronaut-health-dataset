# Dataset de demo unificado (versión corregida tras la auditoría)

Junta **todos los datos reales** reunidos (reposo en cama de NASA en UTMB e Inspiration4) y agrega 4 indicadores **simulados**, marcados con el sufijo `_sim`. Esta versión corrige los errores encontrados por la auditoría independiente (`../docs/verificacion/01` a `04`).

Se regenera desde la raíz del repositorio con un solo script, que reemplaza a `tidy_utmb.py` y `build_demo.py` (ya obsoletos):

```
python3 -I scripts/build_all.py
```

La semilla es fija (2026), así que el resultado es reproducible. Cada corrección aplicada a los datos de origen queda registrada en `../data/utmb/registro_correcciones.csv`.

## Archivos

| Archivo | Filas | Qué es |
|---|---|---|
| `demo_astronautas.csv` | 44 | Perfiles: 40 de UTMB (análogo en tierra; 29 con vitales, 11 solo con cognición o laboratorio) y 4 de Inspiration4 (vuelo real) |
| `demo_diario.csv` | 3.034 | Una fila por astronauta UTMB y día: vitales, sueño, cognición, tilt, indicadores simulados, z-scores y semáforo |
| `demo_lineas_base.csv` | 40 | Media y desviación de la línea base personal |
| `demo_laboratorio.csv` | 9.126 | Laboratorio unificado: UTMB (31 sujetos, 8.036 valores) + Inspiration4 (hemograma 553, panel metabólico 509, PCR 28) |
| `demo_eventos.csv` | 1.053 | Síntomas de 26 sujetos (campañas 3 y CFT70) con acción, intervención y resultado, más una categoría homologada |

## Qué se corrigió respecto de la primera versión
- **Vitales:** se leían mal los encabezados `SysBP`, `DiaBP`, `Resp Rate`, `Weight`, `Body Temp` y `Respiration rate`, y se recuperaron 3.356 valores. Se eliminaron las filas duplicadas del archivo `_All` de la campaña 1. Se corrigieron 2 fechas con el año mal tipeado (2001 → 2004) y se anularon 5 valores imposibles (pulso 16, peso 0).
- **Laboratorio:** se agregaron 21 sujetos cuyo encabezado era `ParameterName`. Se conservan los valores con marca de origen (H), (L), A, B…, en la columna `marca_origen`. La PCR en mg/L se convirtió a mg/dL. La albúmina de electroforesis (SPE) se separa de la química estándar. Las grafías de unidades equivalentes se unificaron.
- **Sueño:** se usa solo el archivo principal de actigrafía. El archivo de consulta duplicaba y mezclaba noches entre sujetos.
- **Cognición:** se eliminaron 30 sesiones duplicadas y se corrigieron las etiquetas según el ReadMe de WinSCAT (CPT = Running Memory, MTS = Match to Sample, CDD = Code Substitution delayed). Se agregó `sesion_n` para controlar el efecto de práctica.
- **Tilt:** ahora lo genera el script. Se toman las columnas `HR` y `HR (Dinamap)`, y los minutos se cuentan solo con dato de pulso. La campaña 1 se excluye porque su archivo de pulso es idéntico al de presión diastólica en el origen.
- **Eventos:** se incluyen los 921 eventos de la campaña 3, que antes se perdían por distinguir mayúsculas en la búsqueda.
- **Radiación simulada:** el acumulado se calcula por días calendario de misión, no por filas observadas.
- **Fase:** 6 sesiones etiquetadas "en misión" con fecha anterior al día 1 se reclasificaron como `pre`.

## `demo_diario.csv`: columnas

| Columna | Unidad | Tipo | Origen |
|---|---|---|---|
| `fase` | pre / mision / post | real | `mision` = en cama, inclinada 6° con la cabeza abajo (análogo de microgravedad) |
| `dia_mision` | días | derivado | Día 1 = primer día en cama. Se ancla con la mediana de (fecha − BR_Day). En 4 filas el BR_Day del origen es inconsistente con la fecha; se usa la fecha |
| `pulso_lpm`, `pas_mmhg`, `pad_mmhg`, `resp_rpm`, `temp_c`, `peso_kg` | lpm, mmHg, rpm, °C, kg | **real** | Case Report Form, doi:10.83263/wjw1-ta27 |
| `sueno_h`, `sueno_eficiencia_pct`, `sueno_latencia_min` | h, %, min | **real** | Actigrafía de la campaña 1 (3 sujetos, 190 noches; solo 2 noches antes del reposo), doi:10.83263/v7n1-ht75 |
| `tipo_test`, `sesion_n` | — | real / derivado | Nasa1p = con instrucciones; `sesion_n` = número de sesión de esa persona |
| `cog_memoria_trabajo_ms` / `_precision_pct` | ms, % | **real** | WinSCAT Running Memory, doi:10.83263/sbne-th55 |
| `cog_matematica_ms`, `cog_emparejamiento_ms`, `cog_codigo_diferido_ms` (+ `_precision_pct`) | ms, % | **real** | WinSCAT: matemática, Match to Sample, Code Substitution diferido |
| `tilt_aumento_pulso_lpm`, `tilt_minutos_inclinado` | lpm, min | **real** | Prueba de tilt de la campaña 3, doi:10.83263/gz1q-a824 |
| `animo_0a10_sim` | 0–10 | **simulado** | Base por persona 6,5–8; leve caída en misión y bajón hacia el 75 % (supuesto) |
| `hrv_rmssd_ms_sim` | ms | **simulado** | Base ~45 ± 12 ms; baja cuando sube el pulso real de ese día |
| `spo2_pct_sim` | % | **simulado** | 97,6 ± 0,7, acotado a 93–100 |
| `radiacion_msv_dia_sim`, `radiacion_msv_acum_sim` | mSv | **simulado** | 0,4 mSv/día en misión, dentro del rango de ~0,2–0,5 mSv/día reportado para la ISS (Shavers et al. 2023). Límite de carrera de NASA: 600 mSv |
| `z_*`, `estado_vitales` | — | derivado | z frente a la línea base personal, con DE mínima (pulso 6, PAS 8, PAD 6, temp 0,3, peso 1). Semáforo por el peor \|z\| de pulso, PAS, PAD y temperatura: < 2 verde, 2–3 amarillo, ≥ 3 rojo. **Propuesta de diseño, no un criterio clínico** |

Semáforo: verde 79,1 %, amarillo 14,8 %, rojo 6,1 %. No verde por fase: antes 11 %, misión 20 %, regreso 36 %.

## Advertencias de interpretación
- **Cognición:** los tiempos de reacción mejoran a lo largo de las fases, pero coincide con un **efecto de práctica** (unos −10,7 ms por sesión). No hay que interpretarlo como mejora fisiológica; conviene comparar por `sesion_n` o usar solo las sesiones posteriores a la familiarización.
- **Sueño:** antes del reposo hay solo 2 noches, así que no hay línea base de sueño fiable.
- **Atípicos:** 23 valores de laboratorio marcados en `atipico`. Incluyen una hemoglobina de 131 (probable error de coma decimal: 13,1 g/dL), la toma de 92 días antes de C003 en Inspiration4 (columnas desplazadas en el origen) y 3 glucosas de 36–44 mg/dL a los 45 días tras el aterrizaje.
- **PCR de Inspiration4:** convertida de pg/ml a mg/dL (÷ 10⁷). Los valores son altos para personas sanas (mediana ~1,2 mg/dL); no se pudo explicar.
- **Privacidad:** el texto libre de los eventos de la campaña 3 contiene nombres de personal médico. Antes de mostrarlos en una demo pública conviene anonimizarlos.
- **PhenoAge:** hay 98 de 105 sujeto-fechas de UTMB y 23 de 28 de Inspiration4 con las 9 entradas de sangre. Falta la edad, y el intercepto y los parámetros de Gompertz de la fórmula no se pudieron verificar (están en un suplemento del artículo).

## Licencias
- OSDR (Inspiration4): **CC0-1.0**, según las páginas de estudio OSD-569 y OSD-575.
- NLSP (UTMB): los datasets están marcados como "Open-Access Data", pero el portal no publica una licencia explícita. Hay que citar el DOI de cada experimento. De los 30 experimentos marcados como públicos, 28 lo son por completo y 2 en parte.

## Fuentes
UTMB vía NLSP: doi:10.83263/wjw1-ta27 (vitales y síntomas), 10.83263/rank-k271 (laboratorio), 10.83263/gz1q-a824 (tilt), 10.83263/v7n1-ht75 (actigrafía), 10.83263/sbne-th55 (WinSCAT). Inspiration4: NASA OSDR OSD-569 y OSD-575. Lista completa en `../docs/FUENTES.md`; auditoría en `../docs/verificacion/`.
