# Resumen de la verificación (2026-11-05)

Siete auditorías independientes con subagentes revisaron todos los datos y afirmaciones del proyecto. Cada una recalculó desde los archivos originales o fue a la fuente en vivo, sin reutilizar los scripts del proyecto. Los reportes completos están en esta carpeta.

## Veredicto
- **Los datos de origen son auténticos.** Las nuevas descargas de NLSP y OSDR son idénticas, los MD5 de los 116 archivos coinciden y los 48 DOIs resuelven al experimento correcto (04).
- **Mi procesamiento tenía errores importantes**, ya corregidos con `scripts/build_all.py`. Encabezados no reconocidos hicieron perder miles de valores reales, había duplicados y faltaban 21 sujetos de laboratorio y 921 eventos. Las conclusiones cualitativas se mantienen; varias cifras cambiaron un poco.
- **Varias cifras de la literatura estaban imprecisas** y se corrigieron. Hubo además una cita con título inventado (Jarczok) y 4 referencias sin fuente identificable, que se eliminaron.

## Errores de procesamiento encontrados y corregidos

| Área | Error | Impacto | Corrección |
|---|---|---|---|
| Vitales (01, 03) | No se reconocían los encabezados `SysBP`, `DiaBP`, `Resp Rate`, `Weight`, `Body Temp` y `Respiration rate` | 3.356 valores reales perdidos (7 sujetos) | Lectura por nombre normalizado |
| Vitales | Archivo `_All` de la campaña 1 duplicaba los de cada sujeto | 252 filas duplicadas | Se omite `_All`; deduplicación por sujeto y día |
| Vitales | Fechas de 2001 (año mal tipeado) y valores imposibles (pulso 16, peso 0) | Filas perdidas o valores falsos | Año corregido si coincide con BR_Day; valores fuera de rango anulados |
| Laboratorio (02) | Encabezado `ParameterName` no reconocido | Faltaban 21 de 31 sujetos (6.762 filas) | Ahora entran los 31 sujetos (8.036 valores) |
| Laboratorio | Se descartaban los valores con marca (H)/(L) | Sesgo hacia valores normales (280 valores) | Se conservan, con la marca en `marca_origen` |
| Laboratorio | "Hemoglobina 182" citada | No existía; era un percentil 95 extrapolado | Percentiles inclusivos; la hemoglobina 131 queda marcada como error de coma |
| Laboratorio | Albúmina de electroforesis mezclada con la química estándar; PCR en mg/L sin convertir | Unidades y métodos mezclados | Se separan; mg/L → mg/dL |
| Sueño (03) | El archivo de consulta duplicaba y mezclaba noches entre sujetos | 11 noches copiadas de otro sujeto | Se usa solo el archivo principal (190 noches) |
| Cognición (03) | 30 sesiones duplicadas; etiquetas incorrectas | n inflado; nombres equivocados | Deduplicado; etiquetas según el ReadMe (Running Memory, etc.) |
| Tilt (01) | Faltaban 4 pruebas con `HR (Dinamap)`; minutos inflados por filas vacías | n = 74 en lugar de 78 | Generado en el script; minutos solo con dato |
| Eventos (03) | La búsqueda distinguía mayúsculas | 921 eventos de la campaña 3 perdidos | 1.053 eventos de 26 sujetos |
| Radiación simulada (03) | Acumulado por filas, no por días | Subestimado en 10 sujetos | Acumulado por días calendario |
| Informe 12 | PCR "ng/ml" | Error de 1.000 veces si se aplicaba | Corregido a pg/ml |

## Cifras corregidas (antes → ahora)
- Pulso después del reposo: 74,9 → **76,1 lpm**. Presión sistólica después: 112,9 → **115,0 mmHg**.
- Cambio individual del pulso: +1,5 → **+1,3 lpm**. Tilt antes del reposo: +34,7 → **+34,1 lpm**.
- Semáforo: 81/13/6 % → **79,1/14,8/6,1 %**. No verde por fase: 10/18/33 % → **11/20/36 %**.
- Sueño en misión: 7,22 → **7,20 h**. Eficiencia: 81,5 → **81,7 %**.
- Glucosa en UTMB: 84,7/79,9/81,3 → **81,4/81,3/82,9 mg/dL** (31 sujetos).
- Sueño en vuelo (literatura): 6,1–6,8 → **6,0–6,5 h**.
- Radiación en la ISS: 0,2–0,6 → **~0,2–0,5 mSv/día** (Shavers et al. 2023).

## Lo que se confirmó sin cambios
- Inspiration4: las 1.090 cifras coinciden con OSDR, con 0 diferencias. Leucocitos −26 %, linfocitos −36 %, glucosa 69,5 → 93,3 mg/dL.
- Tilt durante y después del reposo (+56,9 y +43,8 lpm), peso −1,1 kg y temperatura ~0 °C.
- Pérdida ósea 1–1,5 %/mes, SANS 70 % y 15 %, 600 mSv, aptitud física 12–38 %, volumen plasmático, intolerancia ortostática > 80 %, Cree 2010 y la anemia en el 48 %.
- HRP: las 22 páginas y los 22 enlaces de evidencia funcionan, y las 12 citas de los riesgos son literales (07).

## Advertencias nuevas
- **Cognición:** la mejora de los tiempos de reacción coincide con un efecto de práctica (unos −10,7 ms por sesión).
- **Licencias:** OSDR es CC0-1.0. NLSP no publica una licencia explícita (pie "All rights reserved"); hay que citar los DOIs.
- **Privacidad:** el texto libre de los eventos de la campaña 3 contiene nombres de personal.
- **PhenoAge:** el intercepto y los parámetros de Gompertz no se pudieron verificar, así que no se debe programar la fórmula todavía.
- **Problemas del propio origen:** en la campaña 1, el archivo de pulso del tilt es idéntico al de presión diastólica; Inspiration4 C003 tiene columnas desplazadas a los 92 días antes del vuelo; hay BR_Day mal tipeados.

## Reportes
| Archivo | Alcance |
|---|---|
| `01-vitales-utmb.md` | Vitales y tilt contra los archivos originales y sus MD5 |
| `02-laboratorio.md` | Laboratorio de UTMB e Inspiration4, con nueva descarga desde OSDR |
| `03-sueno-cognicion-eventos-logica.md` | Sueño, cognición, eventos, perfiles, semáforo, simulación y reproducibilidad |
| `04-procedencia.md` | NLSP y OSDR en vivo: metadatos, DOIs, descargas y licencias |
| `05-literatura.md` | Cifras de la literatura en su fuente primaria y fórmula de PhenoAge |
| `06-bibliografia.md` | 130 referencias contra Crossref, Europe PMC y doi.org |
| `07-hrp-base-conocimiento.md` | Base del HRP contra las páginas de NASA en vivo |
| `06b-…`, `07b-…` | Correcciones aplicadas a `FUENTES.md` y al JSON del HRP |
