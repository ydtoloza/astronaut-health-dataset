# Astronaut Health Dataset (NASA Space Apps 2026)

Dataset de demo para el desafío [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/). Reúne **datos abiertos reales de NASA**, verificados y procesados con un pipeline reproducible, más algunos indicadores simulados marcados como tales.

## Qué contiene

| Fuente | Tipo | Contenido |
|---|---|---|
| **UTMB, reposo en cama** ([NASA Life Sciences Portal](https://nlsp.nasa.gov/)) | Análogo en tierra de la microgravedad: 60–70 días en cama inclinada 6° con la cabeza abajo | Vitales diarios de 29 sujetos (2.939 días), laboratorio de 31 sujetos (8.036 valores), cognición WinSCAT, sueño por actigrafía, prueba ortostática (tilt), 1.053 síntomas con la acción tomada |
| **Inspiration4** ([NASA OSDR](https://osdr.nasa.gov/) OSD-569 y OSD-575) | Vuelo real (4 tripulantes, 3 días, septiembre de 2021) | Hemograma, panel metabólico y PCR en 7 tomas, de 92 días antes a 194 días después |
| **Simulados** (columnas `_sim`) | Escenario | Ánimo, HRV, SpO₂, radiación |

## Estructura

```
demo/                  dataset unificado listo para la app (ver demo/LEEME.md)
data/utmb/             tablas limpias de UTMB, resumen por fase y registro de correcciones
data/raw/nlsp/         archivos originales descargados de NLSP (con sus .md5sum)
data/raw/osdr/         archivos originales de OSDR (Inspiration4)
scripts/build_all.py   pipeline: datos originales -> data/utmb/ + demo/
scripts/*.js           descarga automatizada de NLSP (Playwright)
docs/                  resumen, fuentes, base de conocimiento del HRP y auditorías
```

## Reproducir

```
python3 -I scripts/build_all.py
```

Solo usa la biblioteca estándar de Python. Con la semilla fija (2026), los archivos generados son idénticos byte a byte.

## Verificación
Siete auditorías independientes revisaron el dataset (`docs/verificacion/`):
- **Autenticidad:** las descargas nuevas son idénticas a los archivos locales, los MD5 de los 116 archivos coinciden y los 48 DOIs resuelven al experimento correcto.
- **Recálculo:** los valores y estadísticas se recalcularon desde los archivos originales.
- **Literatura:** las cifras citadas se contrastaron con su fuente primaria.

Las correcciones aplicadas están en `data/utmb/registro_correcciones.csv` y `docs/verificacion/00-RESUMEN-VERIFICACION.md`.

## Limitaciones
- UTMB es un **análogo en tierra**, no vuelo real. Inspiration4 es vuelo real, pero con 4 personas.
- Las columnas `_sim` no son datos reales.
- El semáforo (verde, amarillo, rojo) es una **propuesta de diseño**, no un criterio clínico.
- La mejora en cognición coincide con un efecto de práctica.
- El texto libre de los síntomas de UTMB conserva los nombres del personal tal como vienen en el origen.
- No es un dispositivo médico.

## Licencias y citas
- **OSDR (Inspiration4):** CC0-1.0, según las páginas de estudio. Citar OSD-569 y OSD-575.
- **NLSP (UTMB):** los datasets están marcados como "Open-Access Data"; sus DOIs (10.83263/…) figuran en DataCite como CC0-1.0, pero el portal no muestra una licencia explícita. Citar el DOI de cada experimento:
  - wjw1-ta27: vitales y síntomas.
  - rank-k271: laboratorio.
  - gz1q-a824: tilt.
  - v7n1-ht75: actigrafía.
  - sbne-th55: WinSCAT.
- Bibliografía completa en `docs/FUENTES.md`.
