# Resumen consolidado de la investigación (Space Apps 2026: Health Monitoring Software)

**Verificado el 2026-11-05** por 7 auditorías independientes (`verificacion/`). Leyenda: ✅ = verificado en la fuente original · ⚠️ = verificado con matiz o solo por fuente secundaria · ❌ = no usar.

## 1. Conclusión principal
- **De astronautas en vuelo** no hay series de tiempo públicas de signos vitales (LSDA y LSAH requieren solicitud).
- **Sí hay datos reales y abiertos del análogo oficial de microgravedad de NASA:** 30 experimentos de reposo en cama de UTMB en NLSP (28 completamente públicos y 2 en parte), descargables sin cuenta. Están procesados en `utmb/` y `demo/` con `scripts/build_all.py`:
  - Vitales: 29 sujetos, 2.939 días.
  - Laboratorio: 31 sujetos.
  - Sueño: 3 sujetos.
  - Cognición: 29 sujetos.
  - Tilt: 78 pruebas.
  - Síntomas con acciones: 1.053 eventos.
- **Inspiration4 (vuelo real, 4 tripulantes):** hemograma, panel metabólico y PCR de OSDR, con licencia CC0-1.0.
- **Estrategia:** líneas base y umbrales calibrados con UTMB, una demo que reproduce sujetos reales, y datos sintéticos solo para lo que falta (ánimo, HRV, SpO₂, radiación).

## 2. Cifras para umbrales y simulación (estado tras la verificación)

| Indicador | Valor | Fuente | Estado |
|---|---|---|---|
| Pérdida ósea (cadera y columna) | 1–1,5 % de densidad mineral por mes (promedio de cosmonautas del Mir) | HRR, reporte de fracturas 2024 | ✅ |
| Pérdida ósea (metaanálisis) | Piernas −0,8 %/mes (IC −1,1 a −0,5); lumbar y pelvis −6,2 % acumulado | Stavnichuk 2020, *npj Microgravity* | ✅ |
| Sueño en vuelo | **6,0–6,5 h** por noche según los estudios (en tierra, 6,3–6,9 h); 75 % de la tripulación de la ISS usa hipnóticos | Tabla del reporte de sueño del HRR (p. 11); Barger 2014, *Lancet Neurol* | ✅ (corregido: antes decía 6,1–6,8 h) |
| "8,5 h programadas" | No confirmado en el resumen de Barger 2014 | — | ⚠️ |
| Jornada laboral máxima | 6,5 h de trabajo por día y 48 h por semana (no es un límite de sueño) | Reporte de sueño del HRR | ✅ |
| SANS | ~70 % con signos tempranos; ~15 % con edema significativo (Frisén ≥ 1), del cual ~90 % es grado 1 | Reporte SANS 2022 del HRR | ✅ |
| SANS: coroides | +18 % al día 150; vuelve a lo normal unos 90 días después | Macias 2020, *JAMA Ophthalmol* | ✅ |
| Anemia tras vuelos largos | 48 % (origen: Trudel et al. 2020, 721 misiones) | Krittanawong 2022, *Cells* | ✅ |
| Radiación | Límite de carrera de 600 mSv | Reporte de radiación del HRR 2026 | ✅ |
| Radiación diaria en la ISS | **~0,2–0,5 mSv/día o más** | Shavers et al. 2023 (PMC10919966) | ✅ (corregido: antes 0,2–0,6) |
| Aptitud física | 12–38 % de los tripulantes de la estación pierde más del 20 % | Página de riesgo del HRP | ✅ |
| VO₂ máximo | −19 % y −26 %: **solo 2 tripulantes de Gemini VII**, no un rango poblacional | Reporte aeróbico y muscular del HRR, p. 11 | ⚠️ |
| Volumen muscular | −7 a −12 %: una misión de 17 días, medido al aterrizar | Ídem, p. 27 | ⚠️ |
| Cardiovascular | Volumen plasmático −5 a −19 % (Shuttle); más del 80 % con intolerancia ortostática al aterrizar (Mir) | Reporte cardiovascular del HRR | ✅ |
| Glucosa en reposo en cama | Captación en la pierna 9,1 → 5,2 mg/kg/min al día 28 (n=6) | Cree et al. **2010**, *Metabolism* 59(5) | ✅ |
| Riñón | Volumen de orina −39 % después del día 60 (−47 % al inicio); oxalato +115 %; brushita +150 % | Reporte renal del HRR | ⚠️ (matiz) |
| Pulso en reposo y mortalidad | RR 1,09 por cada 10 lpm (es RR, no HR) | Zhang et al. 2016, *CMAJ* | ✅ |
| Temperatura corporal +1 °C | Sin fuente; UTMB muestra +0,04 °C | — | ❌ |

**Datos propios (UTMB, corregidos):**
- Pulso en reposo: 69,3 antes, 70,6 durante y **76,1 lpm después**.
- Prueba de tilt: el pulso sube +34,1 antes, +56,9 durante y +43,8 lpm después.
- Glucosa: 81,4 / 81,3 / 82,9 mg/dL.

**Inspiration4:**
- Leucocitos −26 %, linfocitos −36 %.
- Glucosa de 69,5 a 93,3 mg/dL entre 3 días antes del vuelo y el día siguiente al aterrizaje.

Detalle en `08-nlsp-utmb-datos-abiertos.md` y `12-inspiration4-cmp-phenoage.md`.

## 3. Archivos

| Archivo | Contenido |
|---|---|
| **`verificacion/00-RESUMEN-VERIFICACION.md`** | **Resultado de las 7 auditorías y correcciones aplicadas** |
| **`demo/` (ver `demo/LEEME.md`)** | **Dataset de demo unificado y corregido: 44 astronautas, diario con semáforo, laboratorio (9.126 valores), 1.053 eventos; columnas `_sim` marcadas** |
| `scripts/build_all.py` | Pipeline único de los datos originales a `utmb/` y `demo/` (reemplaza a `tidy_utmb.py` y `build_demo.py`) |
| **`FUENTES.md`** | Bibliografía consolidada y verificada, con tabla "afirmación → fuente" y licencias |
| `08-nlsp-utmb-datos-abiertos.md` + `utmb/*.csv` | Datos reales de reposo en cama, con resumen por fase, cambio individual y registro de correcciones |
| `04-hrp-base-conocimiento.json` | Los 17 riesgos del HRP (corregido según `verificacion/07`). **Base directa de la app.** |
| `10-marcadores-salud-global.md` | Marcadores de "overall health" y diseño del puntaje de 5 dominios |
| `12-inspiration4-cmp-phenoage.md` | Panel metabólico de Inspiration4 y viabilidad de PhenoAge |
| `13-articulo-PMC12612093.md` | Spaceflight Standard Measures (Hardy 2025) |
| `14-proyectos-previos.md` | Proyectos previos y diferenciación |
| `09`, `11`, `07`, `01` | Artículos del usuario y búsqueda de datasets |
| `02`, `05` + `hrr-pdfs/` | Cifras de papers y de los 15 reportes del HRR |
| `03`, `06` | Estudios humanos en OSDR y Standard Measures de NLSP |

## 4. Pendientes
- PhenoAge: falta el intercepto y los parámetros de Gompertz (Suplemento 2, Tabla S6 de Levine 2018) y la edad de los sujetos.
- Presión arterial, frecuencia cardíaca y HRV en vuelo con cifras exactas.
- Valores de CO₂ y temperatura de cabina en NASA-STD-3001 Vol. 2 Rev. E (NTRS 20250004555).
- Anonimizar los nombres de personal que aparecen en el texto libre de los eventos de la campaña 3 antes de una demo pública.
- La PCR de Inspiration4 sale alta para personas sanas (mediana ~1,2 mg/dL); está sin explicar.
