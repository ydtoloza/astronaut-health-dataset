# Astronaut Health Dataset (NASA Space Apps 2026)

Dataset verificado para el desafío [Create Health Monitoring Software for Astronauts on Space Missions](https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/). Reúne **datos abiertos reales de NASA**, procesados con un pipeline reproducible y revisados con tests, más algunos indicadores simulados marcados como tales.

## Qué contiene

| Fuente | Tipo | Contenido |
|---|---|---|
| **UTMB, reposo en cama** ([NASA Life Sciences Portal](https://nlsp.nasa.gov/)) | Análogo en tierra de la microgravedad: 60–70 días en cama inclinada 6° con la cabeza abajo | Vitales diarios de 29 sujetos (2.939 días), laboratorio de 31 sujetos (8.036 valores), cognición WinSCAT, sueño por actigrafía, prueba ortostática (tilt), 1.053 síntomas con la acción tomada |
| **Inspiration4** ([NASA OSDR](https://osdr.nasa.gov/) OSD-569 y OSD-575) | Vuelo real (4 tripulantes, 3 días, septiembre de 2021) | Hemograma, panel metabólico y PCR en 7 tomas, de 92 días antes a 194 días después |
| **Artemis I** ([Nature 2024](https://doi.org/10.1038/s41586-024-07927-7), CC BY 4.0) | Dosimetría real en Orion | Tasa de dosis por minuto de 2 sensores HERA, M-42 y EAD durante 27 días; dosis acumulada del dosímetro personal CAD |
| **NASA IMM** ([Integrated Medical Model](https://www.nasa.gov/nasa-integrated-medical-model-imm-overview/)) | Modelo de riesgo médico publicado | Probabilidad de 98 condiciones en 6 tipos de misión × sexo; eventos, Crew Health Index, evacuación y muerte para misiones de 14 a 1.195 días |
| **Simulados** (columnas `*_sim`) | Escenario | Ánimo, HRV, SpO₂, radiación |

## Estructura

```
├── data/
│   ├── raw/            originales de NASA, nunca se editan (NLSP con .md5sum, OSDR)
│   ├── external/hera_artemis1/  dosimetría real de Artemis I: HERA, CAD, M-42, EAD (Nature 2024)
│   ├── external/imm/   resultados publicados del Integrated Medical Model de NASA (PDF + CSV)
│   ├── interim/        tablas limpias por fuente + registro_correcciones.csv   (generado)
│   └── processed/      dataset unificado para análisis y la app + LEEME.md     (generado)
├── src/astrohealth/
│   ├── config.py       rutas, fases, columnas simuladas, rangos plausibles
│   ├── build.py        pipeline: raw -> interim -> processed
│   ├── load.py         funciones de carga con tipos (cargar_diario, cargar_laboratorio…)
│   ├── validate.py     reglas de integridad
│   └── alertas.py      motor de alertas verde/amarillo/rojo (docs/alertas.md)
├── notebooks/          01-exploracion.ipynb (plantilla de análisis)
├── reports/figures/    figuras generadas por los notebooks
├── tests/              tests de integridad y de las cifras verificadas
├── docs/               fuentes, base de conocimiento del HRP, auditorías (docs/verificacion/)
├── scripts/            descarga automatizada desde NLSP (Playwright)
├── Makefile · requirements.txt · pyproject.toml
```

Regla de oro: **`data/raw/` no se toca**. Todo lo demás en `data/` se regenera con `make data`.

## Primeros pasos

```bash
python -m venv .venv
```

Actívalo con `.venv\Scripts\activate` en Windows o con `source .venv/bin/activate` en macOS y Linux.

```bash
pip install -r requirements.txt
```

| Tarea | Con `make` (macOS/Linux) | Windows (PowerShell) |
|---|---|---|
| Regenerar los datos | `make data` | `$env:PYTHONPATH="src"; python -m astrohealth.build` |
| Revisar integridad | `make validate` | `$env:PYTHONPATH="src"; python -m astrohealth.validate` |
| Ejecutar tests | `make test` | `python -m pytest` |
| Resumen de alertas | `make alertas` | `$env:PYTHONPATH="src"; python -m astrohealth.alertas` |
| Abrir el notebook | `jupyter lab notebooks/` | `jupyter lab notebooks/` |

## Usar los datos en tu análisis

```python
import sys; sys.path.insert(0, "src")          # o: pip install -e .
from astrohealth import cargar_diario, cargar_laboratorio, serie_astronauta

d = cargar_diario()                             # una fila por astronauta y día
lab = cargar_laboratorio()                      # excluye atípicos por defecto
serie_astronauta("UTMB-05", ["pulso_lpm", "pas_mmhg", "estado_vitales"])
```

Para un análisis nuevo, copia `notebooks/01-exploracion.ipynb` con un número correlativo (`02-…`). El diccionario de columnas está en `data/processed/LEEME.md`.

## Alertas
`evaluar(cargar_diario(), cargar_lineas_base())` devuelve una fila por alerta con su nivel, acción y fuente. Combina umbrales clínicos absolutos con el desvío de la línea base personal, e incluye un catálogo de síntomas (reactivación viral, posible trombosis venosa, SANS…) y la dosis de radiación frente al límite de carrera de 600 mSv. Reglas y fuentes en `docs/alertas.md`.

## Revisión y calidad
- **`make validate`**: 17 reglas (sin duplicados, rangos plausibles, fases, semáforo, simulados aislados, cobertura de PhenoAge).
- **`make test`**: además de las reglas, fija las cifras verificadas en la auditoría (por ejemplo, el pulso al regresar de 76,1 lpm y los leucocitos de Inspiration4 −26 %). Si un cambio en el pipeline las altera, el test falla.
- **Auditoría independiente** en `docs/verificacion/`: descargas idénticas a la fuente, MD5 y DOIs verificados, y estadísticas recalculadas desde los originales. Las correcciones aplicadas están en `data/interim/registro_correcciones.csv`.

## Limitaciones
- UTMB es un **análogo en tierra**, no vuelo real. Inspiration4 es vuelo real, pero con 4 personas.
- Las columnas `*_sim` no son datos reales.
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
