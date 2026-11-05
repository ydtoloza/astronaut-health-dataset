# Marcadores de salud global para la app de automonitorización astronauta

Fecha: 2026-11-05. Alcance: ranking de marcadores para un "estado de salud global" en una única puntuación compuesta, diseño del índice y viabilidad de PhenoAge con nuestros datos.

**Convención de verificación.** "Verificado" significa que la cifra o el dato aparece en un resumen de búsqueda o resumen de artículo consultado en esta sesión. "No verificado" significa que no se pudo confirmar en esta sesión y no debe citarse sin revisar el texto completo. No se leyeron textos completos de los artículos.

**Correcciones a las premisas de partida**
- Guidi et al. 2021 (carga alostática) es una **revisión sistemática** (267 estudios), no un metaanálisis, y **no reporta mortalidad** en lo verificado.
- Hillebrand 2013 está publicado en *Europace* y trata **primer evento cardiovascular**, con SDNN/LF/HF, no RMSSD. El dato de RMSSD y mortalidad corresponde a Jarczok et al. 2022 (*Neurosci Biobehav Rev*).
- Aune et al. 2017 aparece en *Nutr Metab Cardiovasc Dis* 27(6):504-517, no en *Eur Heart J*. Su cifra por 10 lpm (1.17, I² = 94%) no quedó verificada; por eso se usa el metaanálisis CMAJ 2016.
- Searle et al. 2008 es de *BMC Geriatrics*, no de *BMC Medical Research Methodology*.

---

## 1. Ranking de marcadores para "salud global"

Orden por fuerza de la evidencia de mortalidad o capacidad funcional, ajustada por si el astronauta puede medirlo en vuelo y si lo tenemos en nuestros datos.

| # | Marcador | Por qué | Evidencia (verificada) | Medible en vuelo | Disponible en nuestros datos | Fuente |
|---|---|---|---|---|---|---|
| 1 | **Aptitud cardiorrespiratoria (VO2max / METs)** | Predictor independiente de mortalidad y eventos CV; es el mejor "signo vital de capacidad" | Metaanálisis de 33 cohortes: RR todas causas **0.87 por MET** (IC95 0.84–0.90); bajo vs alto RR **1.70** (1.51–1.92). Verificado | No directo. Requiere ergómetro. Estimación con wearable limitada | **Parcial.** No hay VO2max por sujeto en los CSV revisados. Sí hay VO2 pre/post vuelo en `aerobic_muscle_2024.pdf` (−19 % y −26 % en dos casos, según notas locales) | Kodama et al. 2009, JAMA. [doi:10.1001/jama.2009.681](https://doi.org/10.1001/jama.2009.681) |
| 2 | **Fuerza de prensa (grip)** | Proxy de masa y función musculoesquelética; mejor predictor que la PA sistólica según los autores | PURE, 139 691 adultos analizados: **HR 1.16 por cada −5 kg** para mortalidad todas causas (IC95 1.13–1.20). Verificado en resumen | **Sí, con dispositivo** (dinamómetro portátil, barato) | **No.** No aparece en `utmb_*.csv` ni en `osdr-inspiration4-clinico.csv` | Leong et al. 2015, *Lancet* (PURE). Resumen: [Healio](https://www.healio.com/news/cardiology/20150821/grip-strength-may-predict-risk-for-mortality-cvd). DOI no verificado |
| 3 | **Edad biológica PhenoAge** | Combina 9 biomarcadores de rutina más edad cronológica | ~9 % más riesgo de mortalidad por año de edad fenotípica (NHANES IV, n=6 209). Verificado en resumen | No (sangre) | **Parcial.** Ver sección 3 | Levine et al. 2018, *Aging* 10(4):573-591. [doi:10.18632/aging.101414](https://doi.org/10.18632/aging.101414) |
| 4 | **Life's Essential 8 (AHA 2022)** | Índice cardiovascular con 8 métricas, cada una 0–100, media no ponderada | Población NHANES 2013–2018: media 64.7 (adultos). Umbrales: <50 bajo, 50–79 moderado, ≥80 alto (fuente secundaria, no verificado en la guía). Verificado | **Parcial.** PA, peso, sueño y glucosa sí. Dieta y nicotina por cuestionario | **Parcial.** PA (UTMB), peso, sueño (actigrafía), glucosa, lípidos (colesterol/HDL/TG en UTMB), IMC derivable | Lloyd-Jones et al. 2022, *Circulation*. [doi:10.1161/CIR.0000000000001078](https://doi.org/10.1161/CIR.0000000000001078). Algoritmo por métrica: no verificado en esta sesión |
| 5 | **Frecuencia cardiaca en reposo (FCR)** | Marcador barato y continuo de forma física y estrés | Metaanálisis CMAJ 2016 (población general): **HR 1.09 por 10 lpm** todas causas; FCR >80 lpm RR **1.45**. Verificado | **Sí, con wearable** | **Sí.** `hr_bpm` diario en `utmb_vitales_diarios.csv`. Sesgo: datos en reposo en cama, no equiparable a población general | Metaanálisis CMAJ 2016;188(3):E53. [cmaj.ca](https://cmaj.ca/content/188/3/E53.short) |
| 6 | **Regularidad del sueño (Sleep Regularity Index)** | Mejor predictor que la duración en UK Biobank | Quintiles altos vs bajo: **20–48 % menos mortalidad todas causas** (n = 60 977). Diferencia frente a duración no significativa (p 0.14–0.20). Verificado | **Sí, con wearable** (actigrafía de muñeca) | **Sí.** Actigrafía UTMB (`utmb_sueno_actigrafia.csv`). Regularidad derivable por día | Windred et al. 2024, *SLEEP* 47(1):zsad253. [doi:10.1093/sleep/zsad253](https://doi.org/10.1093/sleep/zsad253) |
| 7 | **Variabilidad de la FC (RMSSD) en reposo** | Marcador de tono vagal y recuperación | Cuartil más bajo de RMSSD: **HR combinado 1.56** (IC95 1.32–1.85), 32 estudios, 38 008 participantes. Verificado en resumen | **Sí, con wearable** (intervalos RR en reposo) | **No** en los CSV revisados (solo FC). HRV pooled de ESA HDBR existe pero es restringido | Jarczok et al. 2022, *Neurosci Biobehav Rev*. DOI no verificado |
| 8 | **Índice de fragilidad (acumulación de déficits)** | Estándar en geriatría; combina déficits de muchos sistemas | Searle et al. 2008 usó 40 déficits; el índice predice mortalidad en Cox. Verificado en resumen. Puntos de corte no verificados | Parcial | **Parcial.** Se puede construir con labs + vitales + actigrafía; N de déficits probablemente insuficiente, a verificar | Searle et al. 2008, *BMC Geriatr* 8:24. [doi:10.1186/1471-2318-8-24](https://doi.org/10.1186/1471-2318-8-24) |
| 9 | **Autopercepción de salud** | Predictor independiente de mortalidad en casi todos los estudios | Revisión de 27 estudios comunitarios; "malo" vs "excelente" ≈ 2× mortalidad (cifra de una revisión posterior, no verificada en el original). Verificado en resumen | **Sí, cuestionario** | **No** | Idler & Benyamini 1997, *J Health Soc Behav* 38:21-37. [PubMed 9097506](https://pubmed.ncbi.nlm.nih.gov/9097506/) |
| 10 | **Capacidad intrínseca OMS (5 dominios)** | Marco de envejecimiento saludable: locomoción, vitalidad, cognición, psicológico, sensorial | Estructura factorial confirmada en ELSA; predice pérdida de AVD. Dominios verificados. Propuesta de Cesari 2022 no leída; falta consenso de cálculo | Parcial | **Parcial.** Cognición (WinSCAT), vitalidad (FC, sueño), locomoción no | Concepto OMS 2015; uso como herramienta de cribado. [PMC10002144](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10002144/) |
| 11 | **Tiempo de reacción / lapsus del PVT** | Marcador de fatiga y alerta; las métricas de velocidad y lapsus son las más sensibles a la privación de sueño | Basner & Dinges 2011: 74 adultos, 33 h y 5 noches de 4 h. Verificado. Versión corta PVT-B validada (Acta Astronautica 2011) | **Sí, con tablet** | **Parcial.** WinSCAT (tiempos de reacción) en UTMB; no es el mismo test, equivalencia no verificada | Basner & Dinges 2011, *Sleep* 34(5):581-591. [doi:10.1093/sleep/34.5.581](https://doi.org/10.1093/sleep/34.5.581) |
| 12 | **Carga alostática** | Concepto integrador de desgaste fisiológico | Revisión sistemática: carga alostática alta vinculada a peor salud. **Sin evidencia de mortalidad** en lo verificado. Sin puntos de corte validados | Parcial | **Parcial.** Requiere muchos biomarcadores; ver PhenoAge | Guidi et al. 2021, *Psychother Psychosom* 90:11-27. [doi:10.1159/000510696](https://doi.org/10.1159/000510696) |
| 13 | **Estado de ánimo (PANAS, GHQ)** | Dominio conductual del Standard Measures de NASA | Instrumento de NASA; validez y puntos de corte no verificados en esta sesión | **Sí, cuestionario** | **No** en datos propios; sí en HERA (acceso controlado) | Notas locales `06-standard-measures-nlsp.md` |
| 14 | Peso corporal / IMC | Útil para cuidado, pero en cama la pérdida de peso es de desuso, no de salud global | No se citó evidencia de mortalidad en esta sesión | Sí | Sí (`weight_kg`) | Solo como dato de contexto |

**Nota sobre lo no buscado.** No se verificaron marcha/velocidad de la marcha, HRV de Inspiration4 ni un índice compuesto oficial de salud de NASA. No encontré un índice compuesto de NASA en esta sesión; no se afirma que no exista.

---

## 2. Diseño propuesto del índice compuesto

### 2.1 Cinco dominios y pesos

Los pesos son una **hipótesis de diseño justificada por la evidencia de la tabla**, no una estimación validada con nuestros datos. Deben someterse a análisis de sensibilidad.

| Dominio | Peso | Métricas (medibles en vuelo) | Justificación del peso |
|---|---|---|---|
| **Cardiovascular / capacidad** | 30 % | FCR, PA sistólica/diastólica, ΔFC en tilt, RMSSD (si hay wearable) | Mayor evidencia de mortalidad: CRF HR 1.70, FCR HR 1.09/10 lpm |
| **Sueño y recuperación** | 20 % | Regularidad (SRI), duración, latencia, eficiencia | SRI 20–48 % menos mortalidad, con evidencia más reciente |
| **Metabólico / sangre** | 20 % | PhenoAge (o z-scores de albúmina, creatinina, glucosa, PCR, ALP, WBC, linfocitos %, MCV, RDW) | Biomarcadores de rutina con mortalidad validada (NHANES) |
| **Cognitivo / conductual** | 15 % | Lapsus y RT del PVT o WinSCAT, PANAS/GHQ | Sensibilidad a fatiga; sin datos de mortalidad. Peso bajo a propósito |
| **Musculoesquelético** | 15 % | Grip (si hay dinamómetro), marcadores de remodelado óseo (NTX, osteocalcina en UTMB) | Grip HR 1.16 por −5 kg; sin dato de grip en nuestros datos, por lo que el peso se reasigna si falta |

**Regla de reasignación.** Si un dominio no tiene datos, sus pesos se redistribuyen entre los dominios disponibles y la app muestra la **cobertura** (% de peso con datos). Nunca mostrar una puntuación sin su cobertura.

### 2.2 Cálculo con línea base personal

1. **Línea base personal.** Por astronauta y métrica, usar la fase PRE_TEST (`utmb_laboratorio.csv`, `phase`) o los primeros 7 días disponibles. Con menos de 7 días, usar referencia poblacional con encogimiento hacia la media.
2. **z-score con signo.** `z = (x − μ_base) / σ_base`. Signo positivo = mejor: para FCR, PA, lapsus y PCR, invertir el signo.
3. **Subpuntuación de dominio.** Media de z de sus métricas, convertida a escala 0–100 con `50 + 15·z̄`, recortada a [0, 100].
4. **Índice global.** Media ponderada de dominios con reasignación de pesos (sección 2.1).
5. **Vigilancia de tendencia.** Usar el cambio de 7 días frente a la línea base, no el valor absoluto. Esto es lo relevante en bed-rest o en vuelo.

Cómo calcular cada métrica con nuestros datos:
- **FCR y PA:** media diaria de `hr_bpm`, `sbp_mmhg`, `dbp_mmhg` en `utmb_vitales_diarios.csv`.
- **SRI:** a partir de inicio y fin de sueño por día en `utmb_sueno_actigrafia.csv`. Usar la definición de Windred et al. (probabilidad de mismo estado a 24 h, escalada −100 a 100). La fórmula exacta no se verificó en esta sesión.
- **Lapsus / RT:** de WinSCAT en `utmb_cognicion_winscat.csv`, con z-score por sujeto.
- **Tilt:** incremento de FC en ortostatismo, de `utmb_tilt_ortostatico.csv`. Mayor incremento = peor.
- **Labs:** z por analito o PhenoAge (sección 3).

---

## 3. ¿Se puede calcular PhenoAge con nuestros datos?

**Respuesta corta.** Sí con **UTMB**, si se dispone de **edad cronológica** y los analitos coinciden en el mismo sujeto y día. Con el **CBC de Inspiration4** solo se puede calcular una parte.

Los nueve biomarcadores de PhenoAge son: albúmina, creatinina, glucosa, PCR, porcentaje de linfocitos, MCV, RDW, fosfatasa alcalina y leucocitos. Los resúmenes consultados confirman albúmina, creatinina, glucosa y PCR; los demás aparecen como "entre otros" o en fuentes secundarias. **Confirmar la Tabla 1 del artículo original antes de implementar.**

| Input de PhenoAge | UTMB (`utmb_laboratorio.csv`) | Inspiration4 (`osdr-inspiration4-clinico.csv`) | Unidad |
|---|---|---|---|
| Edad cronológica | **No** (no hay columna de edad en ninguno de los CSV revisados) | **No** (solo `sex`) | años |
| Albúmina | Sí (46 filas) | **No** | g/dL |
| Creatinina | Sí (35 filas) | **No** | mg/dL |
| Glucosa | Sí (18 filas; además i-STAT glucosa 24) | **No** encontrada entre los analitos revisados | mg/dL |
| PCR | Sí (32 filas) | **No** | mg/dL |
| Linfocitos % | Sí, "Lymphocytes" (30 filas) | Sí, `LYMPHOCYTES` | % relativo |
| MCV | Sí (36 filas) | Sí (27 muestras) | fL |
| RDW | Sí (31 filas) | Sí (28 muestras) | % |
| Fosfatasa alcalina | Sí (36 filas) | **No** | U/L |
| Leucocitos (WBC) | Sí (36 filas) | Sí (28 muestras) | miles/µL |

**Inputs que faltan.**
- **Edad cronológica** en ambos datasets. Obtenerla del manifiesto de la misión o de la documentación del estudio (OSDR/LSDA). **Dato crítico.**
- **Inspiration4:** faltan albúmina, creatinina, glucosa, PCR y fosfatasa alcalina. Con solo CBC no se puede calcular PhenoAge; quedan 4 de 9 entradas.
- **UTMB:** con todos los analitos, falta la edad y que coincidan fecha y sujeto. Verificar la estructura del CSV: hay valores con comas dentro de nombres de parámetro, así que cualquier conteo debe hacerse con un parser CSV y no con `cut`.

**Advertencias técnicas.**
- **Coeficientes.** No se verificaron los coeficientes ni las transformaciones (p. ej., logaritmo de PCR) de la fórmula de PhenoAge. **Tomarlos de la Tabla 3 / material suplementario del artículo original**, no de un resumen.
- **Población.** PhenoAge se entrenó en NHANES (población general). Los sujetos de UTMB están en bed-rest y son pocos (~9-10 IDs; el conteo de sujetos debe verificarse por un ligero desplazamiento de columnas en la salida). Los valores absolutos tienen poco sentido; **el cambio de edad fenotípica durante la misión** es la métrica útil.
- **Muestra Inspiration4.** Hay 28 muestras por analito, identificadas por `C00x` y tiempo (p. ej., L-92). No es posible asignar un individuo a todas las muestras sin revisar el diseño.

---

## 4. Recomendación resumida

1. Mantener como núcleo de la app: **FCR, PA, regularidad del sueño, PVT o WinSCAT y, si hay dinamómetro, grip**. Son medibles en vuelo y tienen evidencia de mortalidad o de capacidad.
2. Usar **PhenoAge como componente de laboratorio** solo en UTMB y solo con edad cronológica disponible. Para Inspiration4, usar z-scores de los analitos disponibles.
3. Presentar la puntuación siempre con su **cobertura de datos** y como **tendencia frente a línea base personal**.
4. Antes de publicar cifras al equipo, verificar: Tabla 1 y coeficientes de PhenoAge; algoritmo por métrica de LE8; fórmula de SRI; DOI de Leong 2015 y Jarczok 2022; y el texto completo de Cesari 2022 sobre intrinsic capacity.

---

## Fuentes

- Kodama S, et al. Cardiorespiratory fitness as a quantitative predictor of all-cause mortality and cardiovascular events. *JAMA* 2009. https://doi.org/10.1001/jama.2009.681
- Leong DP, et al. Prognostic value of grip strength (PURE). *Lancet* 2015. Resumen verificado en https://www.healio.com/news/cardiology/20150821/grip-strength-may-predict-risk-for-mortality-cvd. DOI no verificado.
- Levine ME, et al. An epigenetic biomarker of aging for lifespan and healthspan. *Aging* 2018;10(4):573-591. https://doi.org/10.18632/aging.101414 (resumen en https://pmc.ncbi.nlm.nih.gov/articles/PMC5940111/)
- Lloyd-Jones DM, et al. Life's Essential 8. *Circulation* 2022. https://doi.org/10.1161/CIR.0000000000001078 (algoritmo por métrica no verificado)
- Metaanálisis de frecuencia cardiaca en reposo. *CMAJ* 2016;188(3):E53. https://cmaj.ca/content/188/3/E53.short
- Windred DP, et al. Sleep regularity is a stronger predictor of mortality risk than sleep duration. *SLEEP* 2024;47(1):zsad253. https://doi.org/10.1093/sleep/zsad253
- Jarczok MN, et al. RMSSD and mortality. *Neurosci Biobehav Rev* 2022. DOI no verificado.
- Searle SD, et al. A standard procedure for creating a frailty index. *BMC Geriatr* 2008;8:24. https://doi.org/10.1186/1471-2318-8-24
- Guidi J, et al. Allostatic load and its impact on health: a systematic review. *Psychother Psychosom* 2021;90:11-27. https://doi.org/10.1159/000510696
- Idler EL, Benyamini Y. Self-rated health and mortality: a review of twenty-seven community studies. *J Health Soc Behav* 1997;38:21-37. https://pubmed.ncbi.nlm.nih.gov/9097506/
- Basner M, Dinges DF. Maximizing sensitivity of the psychomotor vigilance test (PVT) to sleep loss. *Sleep* 2011;34(5):581-591. https://doi.org/10.1093/sleep/34.5.581
- Concepto de capacidad intrínseca (OMS). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10002144/
- Notas locales: `/home/user/hackathon-data/06-standard-measures-nlsp.md`, `/home/user/hackathon-data/05-hrr-evidencia-cuantitativa.md`, `/home/user/hackathon-data/07-datasets-continuacion.md`
- Datos: `/home/user/hackathon-data/utmb/utmb_laboratorio.csv`, `/home/user/hackathon-data/utmb/utmb_vitales_diarios.csv`, `/home/user/hackathon-data/osdr-inspiration4-clinico.csv`
