# Integrated Medical Model (IMM) de NASA: resultados publicados

El IMM es el modelo probabilístico (Monte Carlo) con que NASA estima, antes de una misión, cuántos eventos médicos ocurrirán, cuánto afectan la capacidad de la tripulación (Crew Health Index, CHI) y la probabilidad de evacuación (EVAC) o de muerte (LOCL). Modela 100 condiciones con incidencias de la base iMED (vuelos Apollo, Skylab, Shuttle, Mir e ISS, más datos análogos y terrestres).

Los PDF son copias sin modificar de nasa.gov. Las páginas no indican una licencia; son publicaciones del Gobierno de EE. UU.

| Archivo | Contenido | Origen |
|---|---|---|
| `ranking-of-medical-conditions-by-probability.pdf` | Probabilidad de al menos un evento para 98 condiciones, en 6 misiones de referencia × 2 sexos (1 tripulante; iMED v5.0, 2-feb-2015) | [nasa.gov](https://www.nasa.gov/wp-content/uploads/2026/08/ranking-of-medical-conditions-by-probability.pdf) |
| `imm_probabilidades.csv` | Las tablas 2–7 de ese PDF en formato largo: 98 condiciones × 6 misiones × 2 sexos = 1.176 filas | Extraído con `pdftotext -layout`; muestras revisadas contra el PDF |
| `medical-risk-based-on-mission-duration.pdf` | TME, CHI, EVAC y LOCL para misiones de 14 a 1.195 días (S-20180531-405, 9-jul-2018) | [nasa.gov](https://www.nasa.gov/wp-content/uploads/2026/08/medical-risk-based-on-mission-duration.pdf) |
| `imm_resultados_por_duracion.csv` | Tablas 4–6 de ese PDF: 7 misiones × 3 escenarios (MedCap = botiquín de la ISS sin reabastecimiento; Tratado; Sin tratamiento) | Transcrito; todos los valores se comprobaron contra el texto del PDF |
| `2024-lunar.pdf` | Artemis 7,5 y 27,5 días: TME 2,65 y 21,66; CHI 97,63 y 96,87; EVAC 0,0037 y 0,0094; LOCL 0,0002 y 0,0005 | [nasa.gov](https://www.nasa.gov/wp-content/uploads/2026/08/2024-lunar.pdf) |
| `10-5-day-orion-optimization.pdf` | Optimización del botiquín de Orion para 10,5 días | [nasa.gov](https://www.nasa.gov/wp-content/uploads/2026/08/10-5-day-orion-optimization.pdf) |

Columnas de `imm_probabilidades.csv`: `drm`, `meses`, `eva`, `sexo` (M/F), `condicion` (nombre del PDF), `prob_al_menos_un_evento`, `prob_es_cota_inferior` (el PDF dice ">9.99E-01"), `adaptacion_espacial` (condición marcada "(SA)").

**Limitaciones (del propio NASA):** los datos de vuelo están incompletos (Shuttle STS-1 a 114, ISS Exp. 1-13). El modelo está calibrado para la ISS. Supone que todo se diagnostica bien y todo tratamiento funciona. Las condiciones de adaptación espacial ocurren una sola vez por misión, por eso su probabilidad no crece con la duración. NASA pide usar los resultados con cuidado.

Índice de documentos y fichas por condición (CLiFF): https://www.nasa.gov/integrated-medical-model-documentation/
