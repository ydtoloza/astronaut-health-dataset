# Dosimetría real de Artemis I (HERA, CAD, M-42, EAD)

Datos medidos dentro de la cápsula Orion durante Artemis I (16-nov a 11-dic-2022, sin tripulación y sin eventos solares). Vienen del *source data* del artículo:

> George SP, Gaza R, Matthiä D, et al. **Space radiation measurements during the Artemis I lunar mission.** *Nature* 634, 48–52 (2024). https://doi.org/10.1038/s41586-024-07927-7 — **CC BY 4.0** (se pueden usar y adaptar citando a los autores e indicando los cambios).

| Archivo | Contenido |
|---|---|
| `nature_2024_source_data_fig2.xlsx` | Original sin modificar: dosis de las figuras 2a–2e |
| `nature_2024_source_data_fig3.xlsx` | Original: tasa de HERA y orientación de Orion durante el paso por el cinturón de protones (fig. 3) |
| `artemis1_tasa_dosis.csv.gz` | **Derivado:** tasa de dosis absorbida (agua) en µGy/min por sensor. HERA HSU1 y HSU2 cada 1 min (38.881 filas c/u); M-42 y EAD cada 5 min |
| `artemis1_cad_acumulada.csv` | **Derivado:** dosis acumulada (mGy) del Crew Active Dosimeter CAD SN82 (95 puntos) |

## Cifras (calculadas aquí desde el source data)

| Sensor | Dosis total | Pico (cinturones de Van Allen) | Tasa típica en espacio profundo (mediana) |
|---|---|---|---|
| HERA HSU1 | 11,90 mGy | 133,5 µGy/min | 0,40 mGy/día |
| **HERA HSU2** | **13,47 mGy** (coincide con el artículo) | **287,5 µGy/min** | 0,39 mGy/día |
| M-42 SN127 (más blindado) | 11,23 mGy | 68,7 µGy/min (artículo: 69) | 0,41 mGy/día |
| EAD MU01 | 13,34 mGy | 239,9 µGy/min (artículo: 240) | 0,37 mGy/día |
| CAD SN82 | 12,18 mGy acumulados | — | — |

- Son **dosis absorbidas (mGy)**, no dosis equivalente (mSv). La dosis equivalente es mayor; el artículo da factores de calidad.
- Los picos son los **pasos por los cinturones de radiación** (inicio y fin de misión). El resto es el fondo de **rayos cósmicos galácticos**.
- La declaración de disponibilidad del artículo dice que los autores planean publicar todos los datos en **NASA OSDR RadLab** (https://visualization.osdr.nasa.gov/radlab/gui/overview/).
