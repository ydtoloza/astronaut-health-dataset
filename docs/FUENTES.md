# FUENTES: bibliografía y fuentes del proyecto (Space Apps 2026, Health Monitoring Software)

Verificado el 2026-11-05; ver verificacion/06-bibliografia.md

Fecha de consolidación: 2026-11-05. Carpeta: `/home/user/hackathon-data/`. Cambios aplicados tras la verificación: ver `verificacion/06b-correcciones-aplicadas.md`. Copia previa: `verificacion/backup/FUENTES.original.md`.

**Convenciones**
- **Nº**: número de fuente en esta lista. Las citas del resto del documento usan ese número. Un número marcado como **alias de N** es el mismo documento que N; no se cita por separado.
- **Estado**: ✅ = verificado (por el coordinador o en la verificación del 2026-11-05). ⚠️ = reportado por un subagente o con matiz, falta verificar. ❌ = no usar.
- **(cita incompleta)**: faltan datos en los archivos. No se completaron de memoria.
- **(sin fuente identificable — no citar)**: la búsqueda no encontró el documento; no citar hasta identificarlo.
- Los metadatos de los DOI se verificaron con la API de Crossref, DataCite, PubMed (E-utilities) y Europe PMC el 2026-11-05. Europe PMC y PubMed respondieron 500/503 de forma intermitente; los casos pendientes se indican en cada entrada.

---

## 1. Lista maestra de fuentes

### 1.1 Desafío y NASA HRP

1. Space Apps 2026, desafío "Health Monitoring Software". https://www.spaceappschallenge.org/2026/challenges/health-monitoring-software/ (sin verificar: error de certificado TLS con el bundle del proxy; verificar a mano).
2. NASA Human Research Program (HRP). https://www.nasa.gov/hrp/
3. NASA HRP, peligros (hazards). https://www.nasa.gov/hrp/hazards/ (cinco páginas `hazard-*` listadas en `04-hrp-base-conocimiento.json`, campo `peligros_contexto`). Verificadas: "Hazard: Space Radiation", "Hazard: Isolation and Confinement", "Hazard: Distance From Earth", "Hazard: Gravity Fields", "Hazard: Hostile/Closed Environments".
4. NASA HRP, riesgos (risks). https://www.nasa.gov/hrp/risks/
5. Human Research Roadmap, portal de evidencia. https://humanresearchroadmap.nasa.gov/evidence/
6. NASA HRP, página NLSP (lista tres datasets abiertos de reposo en cama). https://www.nasa.gov/hrp/nlsp/ (leída en `07-datasets-continuacion.md`).
7. Diecisiete páginas de riesgo de NASA: `https://www.nasa.gov/reference/<slug>/`. Las 22 URL concretas de `04-hrp-base-conocimiento.json` responden 200 y el título coincide con el riesgo (p. ej. "Risk of Hypoxia - NASA"). Fuente de la mayoría de cifras de la base de conocimiento (fitness, SANS, hueso, sueño, alimentación, EVA, etc.).
8. NASA HRP, contramedidas. https://www.nasa.gov/hrp/human-health-countermeasures/ (solo descripción general, sin cifras).

### 1.2 Reportes de evidencia HRR (Human Research Roadmap)

Fuente: `05-hrr-indice.csv` (26 filas) más dos PDF adicionales (35, 36). La columna "Local" indica si el PDF está en `hrr-pdfs/`. Las URL son las de la columna `pdf_url` del CSV, salvo donde se indica.

| Nº | Informe (archivo) | Año | Riesgo / tema (título del PDF) | URL del PDF oficial | Local |
|---|---|---|---|---|---|
| 9 | Medical.pdf | s/f | Evidence Report: Risk of Adverse Health Outcomes and Decrements in Performance due to In-Flight Medical Conditions (el año 2017 del nombre de los metadatos del archivo no está confirmado) | https://humanresearchroadmap.nasa.gov/evidence/reports/Medical.pdf | no descargado |
| 10 | Dust.pdf | s/f | Evidence Report: Risk of Adverse Health & Performance Effects of Celestial Dust Exposure | https://humanresearchroadmap.nasa.gov/evidence/reports/Dust.pdf | no descargado |
| 11 | Multiple Evidence Reports.pdf | s/f | Risk of Ineffective or Toxic Medications During Long-Duration Exploration Spaceflight. **(placeholder; no es un reporte)**: el PDF es un aviso de una página. Citar la página del riesgo: https://humanresearchroadmap.nasa.gov/Risks/?i=177 | ~~.../Multiple%20Evidence%20Reports.pdf~~ (placeholder) | `hrr-pdfs/multiple_evidence_reports.pdf` (placeholder) |
| 12 | Multiple Evidence Reports.pdf | s/f | Risk of Renal Stone Formation. **Alias de 34** (informe propio). No citar el PDF placeholder | ~~.../Multiple%20Evidence%20Reports.pdf~~ (placeholder) | — |
| 13 | HRP-ER-BMED-HFBP-20250210.pdf | 2025 | Evidence Report: Risk of Adverse Cognitive or Behavioral Changes and Psychiatric Disorders Leading to In-mission H... (222 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/HRP-ER-BMED-HFBP-20250210.pdf | `hrr-pdfs/behav_psych_2025.pdf` |
| 14 | Risk of Inadequate HSIA approved FINAL_ 6-13-2023.pdf | 2023 | **Evidence Report: Risk of Inadequate Human-System Integration Architecture** (254 p.). También conocido como "Risk of Adverse Mission Outcomes Due to Earth Independent Human-Systems Operations" (título de la página de riesgo, i=175) | https://humanresearchroadmap.nasa.gov/evidence/reports/Risk%20of%20Inadequate%20HSIA%20approved%20FINAL_%206-13-2023.pdf | no descargado |
| 15 | OP Dynamic Loads EB FINAL_11-30-22.pdf | 2022 | Evidence Report: Risk of Injury Due to Dynamic Loads (106 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/OP%20Dynamic%20Loads%20EB%20FINAL_11-30-22.pdf | no descargado |
| 16 | Team 2022 -Evidence Report FINAL_5-9-2024.pdf | 2024 | Evidence Report: Risk of Performance and Behavioral Health Decrements Due to Inadequate Cooperation, Coordination, Communication, and Psychosocial... (114 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/Team%202022%20-Evidence%20Report%20FINAL_5-9-2024.pdf | no descargado |
| 17 | Sleep.pdf | s/f | Evidence Report: Risk of Performance Decrements and Adverse Health Outcomes Resulting from Sleep Loss, Circadian Desynchronization, and Work... (83 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/Sleep.pdf | `hrr-pdfs/sleep.pdf` |
| 18 | IVD.pdf | s/f | Concern of Intervertebral Disc Damage upon and immediately after re-exposure to Gravity [inactive]. Capítulo 5 del HRP-47060 Human Health Countermeasures Element Evidence Book (10 p.); citar como capítulo, no como informe de riesgo | https://humanresearchroadmap.nasa.gov/evidence/reports/IVD.pdf | no descargado |
| 19 | Host_Micro EB_Final 7-6-22.pdf | 2022 | Evidence Report: Risk of Adverse Health Effects Due to Host-Microorganism Interactions (29 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/Host_Micro%20EB_Final%207-6-22.pdf | no descargado |
| 20 | SM Evidence Report 2022_FINAL 6-13-2023.pdf | 2023 | Evidence Report: Risk of Altered Sensorimotor/Vestibular Function Impacting Critical Mission Tasks, Human Health, ... (160 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/SM%20Evidence%20Report%202022_FINAL%206-13-2023.pdf | no descargado |
| 21 | Bone Fracture Evidence Report_07-18-2024.pdf | 2024 | Evidence Report: Risk of Bone Fracture due to Spaceflight-induced Changes to Bone (60 p.). Ver 35 (alias, versión anterior) | https://humanresearchroadmap.nasa.gov/evidence/reports/Bone%20Fracture%20Evidence%20Report_07-18-2024.pdf | `hrr-pdfs/bone_fracture_2024.pdf` |
| 22 | Cardio Risk EB 2022 FINAL_4-3-2023.pdf | 2023 | Evidence Report: Risk of Cardiovascular Adaptations Contributing to Adverse Mission Performance and Health Outcomes (161 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/Cardio%20Risk%20EB%202022%20FINAL_4-3-2023.pdf | `hrr-pdfs/cardio_2023.pdf` |
| 23 | IMMUNE EB Update 2021 v02 FINAL_6-15-22.pdf | 2022 | Evidence Report: Risk of Crew Adverse Health Event Due to Altered Immune Response (56 p.). Año 2022 por la fecha final del nombre; "2021" es la versión de actualización | https://humanresearchroadmap.nasa.gov/evidence/reports/IMMUNE%20EB%20Update%202021%20v02%20FINAL_6-15-22.pdf | `hrr-pdfs/immune_2022.pdf` |
| 24 | Multiple Evidence Reports.pdf | s/f | Risk of Mission Impacting Injury and Compromised Performance and Long-Term Health Effects due to ... **(placeholder; no es un reporte)**. Citar la página del riesgo EVA: https://humanresearchroadmap.nasa.gov/Risks/?i=84 | ~~.../Multiple%20Evidence%20Reports.pdf~~ (placeholder) | `hrr-pdfs/multiple_evidence_reports.pdf` (placeholder) |
| 25 | Evidence Report Hypoxia and DCS_FINAL_1-8-2024.pdf | 2023 (aprobado el 31-oct-2023; 2024 en el nombre del archivo) | **Evidence Report: Risk of Reduced Crew Health and Performance due to Decompression Sickness and Hypoxia** (94 p.). Cubre DCS e hipoxia en un solo informe. Alias: 28 | https://humanresearchroadmap.nasa.gov/evidence/reports/Evidence%20Report%20Hypoxia%20and%20DCS_FINAL_1-8-2024.pdf | no descargado |
| 26 | Evidence report aerobic and muscle_FINAL 4-3-2024.pdf | 2024 | Evidence Report sobre dos riesgos: Reduced Muscle Mass, Strength & Endurance (muscle) y Reduced Aerobic Capacity (aerobic) (169 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/Evidence%20report%20aerobic%20and%20muscle_FINAL%204-3-2024.pdf | `hrr-pdfs/aerobic_muscle_2024.pdf` |
| 27 | Multiple Evidence Reports.pdf | s/f | Risk of Performance Decrement and Crew Illness Due to Inadequate Food and Nutrition. **Alias de 32** (informe propio). No citar el PDF placeholder | ~~.../Multiple%20Evidence%20Reports.pdf~~ (placeholder) | — |
| 28 | Evidence Report Hypoxia and DCS_FINAL_1-8-2024.pdf | 2023/2024 | **Alias de 25** (mismo PDF; el título de 28 "Due to Hypoxia" es un tema parcial del mismo informe) | https://humanresearchroadmap.nasa.gov/evidence/reports/Evidence%20Report%20Hypoxia%20and%20DCS_FINAL_1-8-2024.pdf | no descargado |
| 29 | SANS EB 2022 FINAL_8-15-22.pdf | 2022 | Evidence Report: Risk of Spaceflight Associated Neuro-ocular Syndrome (SANS) (66 p.) | https://humanresearchroadmap.nasa.gov/evidence/reports/SANS%20EB%202022%20FINAL_8-15-22.pdf | `hrr-pdfs/sans_2022.pdf` |
| 30 | HRP-ER-CANCER-SR-20260811.pdf | 2026 | Evidence Report: Risk of Ionizing Radiation Carcinogenesis (75 p.). Approved for Public Release: 2026 | https://humanresearchroadmap.nasa.gov/evidence/reports/HRP-ER-CANCER-SR-20260811.pdf | `hrr-pdfs/radiation_cancer_2026.pdf` |
| 31 | Osteo.pdf | s/f | Evidence Report: Risk of Early Onset Osteoporosis Due to Space Flight (119 p.) | https://humanresearchroadmap.nasa.gov/evidence/other/Osteo.pdf | `hrr-pdfs/osteo_legacy.pdf` |
| 32 | Food HRP-Evidence Report FINAL_4-15-24.pdf | 2024 | Evidence Report: Risk of Performance Decrement and Crew Illness Due to Inadequate Food and Nutrition (46 p.). Referencia válida para alimentación (ver 27) | https://humanresearchroadmap.nasa.gov/evidence/other/Food%20HRP-Evidence%20Report%20FINAL_4-15-24.pdf | `hrr-pdfs/food_nutrition_2024.pdf` |
| 33 | Nutrition ER_human_adaptation_2020_final.pdf | 2020 | Human Adaptation to Spaceflight: The Role of Nutrition (135 p.) | https://humanresearchroadmap.nasa.gov/evidence/other/Nutrition%20ER_human_adaptation_2020_final.pdf | `hrr-pdfs/nutrition_human_adapt_2020.pdf` |
| 34 | 2024 Renal Evidence Report_Final.pdf | 2024 | Evidence Report: Risk of Renal Stone Formation (42 p.), Exploration Medical Capabilities. Referencia válida para cálculo renal (ver 12) | https://humanresearchroadmap.nasa.gov/evidence/other/2024%20Renal%20Evidence%20Report_Final.pdf | `hrr-pdfs/renal_2024.pdf` |

35. **Alias de 21.** Bone Fracture Evidence Report, archivo `Fracture.pdf` (versión anterior: "Approved for Public Release: May 12, 2017", 34 p.; mismo título que 21). Descargado en `hrr-pdfs/Fracture.pdf`; no aparece en el CSV y su URL de origen no está registrada en los archivos. Usado en: 00, 05.
36. `hhc_risk_approach_plan_2026.pdf`. **HRP Risk Approach Plans For the Human Health Countermeasures Element** (junio 2026, 9 p.; M2M Deliverable). URL de origen no registrada en los archivos; descargado, sin uso en los reportes. Usado en: 05 (lista de descargas).

Enlaces a PDF de NASA desde `04-hrp-base-conocimiento.json` (no descargados ni verificados salvo indicación):

37. **NASA-STD-3001 Medical Technical Brief: Bone Loss, OCHMO-MTB-013 Rev D** (26 p.). `ochmo-tb-030-bone-loss.pdf` (el nombre del archivo "tb-030" no coincide con el identificador del documento, MTB-013 Rev D). https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-030-bone-loss.pdf?emrc=705e1b (riesgo de cambios óseos).
38. `whatisyourspaceheight.pdf` ("WHAT'S YOUR SPACE HEIGHT?", 25-abr-2018, 7 p.; verificado). https://www.nasa.gov/wp-content/uploads/2018/05/whatisyourspaceheight.pdf?emrc=87cc88 (riesgo de cambios óseos; fuente de la cifra de crecimiento de estatura).
39. Space training fact sheet, "Training for space: Astronaut training and mission preparation", NASA JSC (2 p.; verificado). https://www.nasa.gov/wp-content/uploads/2015/10/160410main_space_training_fact_sheet.pdf?emrc=6cb004 (apoyo a operaciones de sistemas; fuente de la cifra de 300 h de simulador).
40. **Evidence Report: Risk of Cardiovascular Disease and Other Degenerative Tissue Effects from Radiation Exposure** (52 p.). `Degen.pdf`. No trata de cánceres (esos están en 30). https://humanresearchroadmap.nasa.gov/evidence/reports/Degen.pdf (el enlace del JSON tenía el parámetro `?rnd=`; se eliminó).

### 1.3 Artículos científicos

Formato tipo APA. Solo se incluyen los artículos citados en los archivos. "Usado en" indica los archivos que los citan.

41. Barger, L., Flynn-Evans, E., Kubey, A., Walsh, L., Ronda, J., Wang, W., et al. (2014). Prevalence of sleep deficiency and use of hypnotic drugs in astronauts before, during, and after spaceflight: an observational study. *The Lancet Neurology, 13*(9), 904–912. https://doi.org/10.1016/S1474-4422(14)70122-X. Metadatos confirmados. Usado en: 00, 02. Verificado en el resumen: 6,09 h [DE 0,67] de sueño en vuelo ISS (n = 21); 12 de 16 tripulantes ISS (75 %) usaron hipnóticos. **La cifra de 8,5 h programadas no aparece en el resumen; no atribuirla a este artículo.** (La solicitud original decía *PLoS Medicine*; la revista correcta es *Lancet Neurology*.)
42. Stavnichuk, M., Mikolajewicz, N., Corlett, T., Morris, M., & Komarova, S. (2020). A systematic review and meta-analysis of bone loss in space travelers. *npj Microgravity, 6*, 13. https://doi.org/10.1038/s41526-020-0103-2 (PMC7200725). Metadatos confirmados. Usado en: 00, 02. Verificado en 05: −0,8 %/mes [IC −1,1; −0,5] en extremidad inferior (misiones > 30 días); el propio artículo da cifras acumuladas ligeramente distintas en el resumen y en Resultados (−5,4 % frente a −4,9 %).
43. Comfort, P., McMahon, J., Jones, P., Cuthbert, M., Kendall, K., Lake, J., et al. (2021). Effects of Spaceflight on Musculoskeletal Health: A Systematic Review and Meta-analysis, Considerations for Interplanetary Travel. *Sports Medicine, 51*(10), 2097–2114. https://doi.org/10.1007/s40279-021-01496-9 (PMID 34115344). Metadatos confirmados. Usado en: 02. Cita dentro del texto a LeBlanc et al. y Antonutto et al., no verificados.
44. Macias, B., Patel, N., Gibson, C., Samuels, B., Laurie, S., Otto, C., et al. (2020). Association of Long-Duration Spaceflight With Anterior and Posterior Ocular Structure Changes in Astronauts and Their Recovery. *JAMA Ophthalmology, 138*(5), 553. https://doi.org/10.1001/jamaophthalmol.2020.0673. Metadatos confirmados. Usado en: 00, 02. Verificado en 05: coroides +18 % el día 150 (media 43 µm; IC95 35–46) y valor basal a los 90 días tras el regreso. El informe SANS (p. 12) lo cita como "2021"; el artículo es de 2020. (Sustituye a "Lee 2020" de la solicitud original, según 02.)
45. Cree, M., Paddon-Jones, D., Newcomer, B., Ronsen, O., Aarsland, A., Wolfe, R., et al. (2010). Twenty-eight-day bed rest with hypercortisolemia induces peripheral insulin resistance and increases intramuscular triglycerides. *Metabolism, 59*(5), 703–710. https://doi.org/10.1016/j.metabol.2009.09.014 (PMC2856785). Metadatos confirmados (Crossref: 2010, vol. 59, nº 5; epub 2009-11-17). Usado en: 00, 02. **Año 2010 (corregido).** Los archivos `00-RESUMEN.md` y `02-valores-cuantitativos.md` aún dicen 2009 (pendiente de corregir en esos archivos; no modificados aquí). Reposo en cama, no vuelo.
46. Garrett-Bakelman, F., Darshi, M., Green, S., Gur, R., Lin, L., Macias, B., et al. (2019). The NASA Twins Study: A multidimensional analysis of a year-long human spaceflight. *Science, 364*(6436), eaau8650. https://doi.org/10.1126/science.aau8650 (PMC7580864). Metadatos confirmados. Usado en: 01, 02, 07.
47. Jones, C., Overbey, E., Lacombe, J., Ecker, A., Meydan, C., Ryon, K., et al. (2024). Molecular and physiological changes in the SpaceX Inspiration4 civilian crew. *Nature, 632*(8027), 1155–1164. https://doi.org/10.1038/s41586-024-07648-x (PMC11357997). Metadatos confirmados. Usado en: 02 (texto no leído).
48. Sanders, L., Grigorev, K., Scott, R., Saravia-Butler, A., Polo, S., Gilbert, R., et al. (2024). Inspiration4 data access through the NASA Open Science Data Repository. *npj Microgravity, 10*, Article 56. https://doi.org/10.1038/s41526-024-00393-5 (PMC11094041). Metadatos confirmados. Usado en: 01. Licencia CC BY 4.0 del texto del artículo (según 01; no re-verificada).
49. Bonmatí-Carrión, M., Santhi, N., Atzori, G., Mendis, J., Kaduk, S., Dijk, D., et al. (2024). Effect of 60 days of head down tilt bed rest on amplitude and phase of rhythms in physiology and sleep in men. *npj Microgravity, 10*, Article 42. https://doi.org/10.1038/s41526-024-00387-3 (PMC10980770). Metadatos confirmados. Usado en: 01. Datos "available on request" (ver 76, 80).
50. Solbiati, S., & Caiani, E. (2025). Heart rate variability adaptation due to head-down tilt bed rest: insights from pooled data of six campaigns. *npj Microgravity, 11*, Article 48. https://doi.org/10.1038/s41526-025-00509-5 (PMC12313925). Metadatos confirmados. Usado en: 01, 07. Datos no públicos (acuerdos con ESA); solicitud al autor.
51. Otsuka, K., Cornelissen, G., Furukawa, S., Kubo, Y., Shibata, K., Mizuno, K., et al. (2021). Astronauts well-being and possibly anti-aging improved during long-duration spaceflight. *Scientific Reports, 11*, Article 14907. https://doi.org/10.1038/s41598-021-94478-w (PMC8295322). Metadatos confirmados. Usado en: 01, 07. Datos restringidos por JAXA.
52. Baevsky, R., Baranov, V., Funtova, I., Diedrich, A., Pashenko, A., Chernikova, A., et al. (2007). Autonomic cardiovascular and respiratory control during prolonged spaceflights aboard the International Space Station. *Journal of Applied Physiology, 103*(1), 156–161. https://doi.org/10.1152/japplphysiol.00137.2007. Metadatos confirmados. Usado en: 02 (solo snippet).
53. Fu, Q., Shibata, S., Hastings, J. L., Platts, S. H., Hamilton, D. M., Bungo, M. W., et al. (2019). Impact of Prolonged Spaceflight on Orthostatic Tolerance During Ambulation and Blood Pressure Profiles in Astronauts. *Circulation, 140*(9), 729–738. https://doi.org/10.1161/CIRCULATIONAHA.119.041050 (PubMed 31319685, no confirmado en esta revisión). Metadatos confirmados (Crossref). Usado en: 02 (pendiente de lectura del texto completo).
54. Mendt, S., Brauns, K., Friedl-Werner, A., Belavy, D. L., Steinach, M., Schlabs, T., Werner, A., Gunga, H.-C., & Stahn, A. C. (2021). Long-term bed rest delays the circadian phase of core body temperature. *Frontiers in Physiology, 12*, Article 658707. https://doi.org/10.3389/fphys.2021.658707 (PMC8141791). Metadatos confirmados (Crossref y Europe PMC; citación completada el 2026-11-05). Datos de origen: 77. Usado en: 01.
55. **(sin fuente identificable — no citar).** Artículo de Sci Rep 2022 sobre 10 astronautas (frecuencia cardíaca, VFC y ritmos circadianos). La búsqueda en Crossref no lo encontró. Usado en: 02 (revisar esa cita antes de presentar).
56. **(sin fuente identificable — no citar).** Basner, M., et al. (2019), presentación IAC 2019 sobre Concordia / VIPER / Somnopole. Sin registro en Crossref ni PubMed; es una presentación de congreso sin acta localizada. Usado en: 07.
57. **(sin fuente identificable — no citar).** Artículos de Mars-500 (PLoS ONE) y SIRIUS-19. Sin coincidencia clara en Crossref. Usado en: 07.
58. Collet, G., Mairesse, O., McDonald-Nethercott, E., Ducrot, Y. M., Meeusen, R., & Pattyn, N. (2019). *Sleep during an Antarctic overwintering: Comparing an altitude base and a coastal station* [Póster]. Figshare. https://doi.org/10.6084/m9.figshare.10281224.v1. Metadatos confirmados (Figshare API: publicado 2019-11-10; licencia CC BY 4.0). Usado en: 01, 07. Es un póster, no un dataset. **Año 2019 (corregido; el 2013 del nombre del archivo no está respaldado).** Si existe un WCSM 2013 distinto, citarlo aparte. **Alias: 78 (mismo ítem).**
59. **Mismo artículo que 09a** (Krittanawong et al., 2022; PMC9818606, aportado por el usuario). Metadatos confirmados: ver 09a.
60. **Mismo artículo que 09b** (Jacobs et al., 2026; PMC13289012, aportado por el usuario). Metadatos confirmados: ver 09b.
61. NASA OSDR, **OSD-569** "Whole Blood Measurements from the SpaceX Inspiration4 Mission (RNA-seq, epitranscriptome, WGS, clonal hematopoiesis, CBC)" (hemograma completo). https://osdr.nasa.gov/bio/repo/data/studies/OSD-569 . Acceso: descarga directa (archivo `LSDS-7_Complete_Blood_Count_CBC.upload_SUBMITTED.csv`). Título verificado por API OSDR. **Licencia: CC0-1.0** (campo "License" de la página del estudio; ver sección 4). El ISA no contiene licencia. Usado en: 03, `osdr-inspiration4-clinico.csv`, 00.
62. NASA OSDR, otros estudios Inspiration4: OSD-570, 571, 572, 573, 574, 575, 630, 656, 687. https://osdr.nasa.gov/bio/repo/data/studies/OSD-### . Acceso: directo para datos procesados; crudos y datos genéticos por solicitud con comité de ética. **Licencia: CC0-1.0 verificada en OSD-569 y OSD-575**; los demás, sin comprobar individualmente (ver sección 4). OSD-575: "SpaceX Inspiration4 Blood Serum Metabolic Panel and Immune/Cardiac Cytokine Arrays (Comprehensive Metabolic Panel and Multiplex)". Usado en: 01, 03.
63. NASA GeneLab/OSDR, **GLDS-191 = OSD-191** (microbiota de Mars500). La URL de origen (https://osdr.nasa.gov/genelab/accession/GLDS-191/) redirige a OSD-191. Título del estudio: "Temporal dynamics of the gut microbiota in people sharing a confined environment, a 520-day ground-based space simulation, MARS500". Publicación asociada: Turroni, S., Rampelli, S., Biagi, E., Consolandi, C., Severgnini, M., Peano, C., Quercia, S., Soverini, M., Carbonero, F. G., Bianconi, G., Rettberg, P., Canganella, F., Brigidi, P., & Candela, M. (2017). *Microbiome, 5*, Article 39. https://doi.org/10.1186/s40168-017-0256-8. Metadatos confirmados (Crossref). Licencia del dataset: no verificada. Usado en: 01.
64. UTMB, *Case Report Form*. DOI 10.83263/wjw1-ta27 (https://doi.org/10.83263/wjw1-ta27). DataCite: "Case Report Form" (Ames Research Center, 2026; CC0-1.0). Procesado en 08: vitales diarios, 3.192 registros, 29 sujetos. Usado en: 00, 08.
65. UTMB, *Clinical Laboratory Assessment (Flight Analog)*. DOI 10.83263/rank-k271 (https://doi.org/10.83263/rank-k271). DataCite: 2026, CC0-1.0. Procesado en 08: laboratorio, 2.010 valores, 10 sujetos. Usado en: 00, 08.
66. UTMB, *Neuroendocrine and Cardiovascular Response to Tilt (Flight Analog)*. DOI 10.83263/gz1q-a824 (https://doi.org/10.83263/gz1q-a824). DataCite: 2026, CC0-1.0. Procesado en 08: 74 pruebas de inclinación. Usado en: 08.
67. UTMB, *Bed Rest Standard Measures: Cardiovascular Function*. DOI 10.83263/kw2c-zj80 (https://doi.org/10.83263/kw2c-zj80). DataCite: 2026, CC0-1.0. Descargado, sin procesar. Usado en: 08 (ecocardiografía pendiente).
68. UTMB, *Bed Rest Standard Measures: Plasma Volume*. DOI 10.83263/4dzb-2267 (https://doi.org/10.83263/4dzb-2267). DataCite: 2026, CC0-1.0. Descargado, sin procesar. Usado en: 08 (pendiente).
69. UTMB, *Aerobic Capacity (Flight Analog)*. DOI 10.83263/w056-8t76 (https://doi.org/10.83263/w056-8t76). DataCite: 2026, CC0-1.0. Sin uso documentado en los archivos.
70. UTMB, *Bed Rest Standard Measures: Actilight* (sueño y actigrafía). **DOI 10.83263/v7n1-ht75** (DataCite: Putcha, L., 2026; estado: publicado). Experimento NLSP `cd8a4a16-fcfd-5c32-a61f-22c590a10b35`. https://nlsp.nasa.gov/explore/data/details/cd8a4a16-fcfd-5c32-a61f-22c590a10b35?dataType=EXPERIMENTS . Procesado en 08: 200 noches, 3 sujetos.
71. UTMB, *Neurocognitive Assessment (WinSCAT) (Cognitive Assessment Tool for Windows) (Flight Analog)*. **DOI 10.83263/sbne-th55** (DataCite: Sipes, W. E., 2026). Experimento NLSP `80ee3231-7c42-5be4-b6c2-b8c788feeb50`. https://nlsp.nasa.gov/explore/data/details/80ee3231-7c42-5be4-b6c2-b8c788feeb50?dataType=EXPERIMENTS . Procesado en 08: 332 sesiones, 29 sujetos. Normas: sin valores verificados.
72. UTMB, *Bone Densitometry Assessment (Flight Analog)* (DXA). **DOI 10.83263/7myc-5j86** (DataCite: Sibonga, J. D., 2026). Experimento NLSP `4469ebdc-0a65-55e8-bbff-3cf6b044c4c6`. https://nlsp.nasa.gov/explore/data/details/4469ebdc-0a65-55e8-bbff-3cf6b044c4c6?dataType=EXPERIMENTS . Descargado, sin procesar.
73. UTMB, *Campaign 1 Flight Analog Bed Rest Study* (alias C1, "UTMB Campaign 1") (NLSP, misión `6eaf1654-72d4-5d71-a9dd-a02e674c6473`). Ficha confirmada por API NLSP (06, 2026-11-05); el estado de archivo a nivel de misión no aparece en el registro. https://nlsp.nasa.gov/explore/data/details/6eaf1654-72d4-5d71-a9dd-a02e674c6473?dataType=MISSIONS . Usado en: 06, 07.
74. UTMB, *Campaign 3 Flight Analog Bed Rest Study* (alias "UTMB Campaign 3") (NLSP, misión `593a6726-8650-551a-8d67-0f03468de92f`). Ficha confirmada por API NLSP; igual que 73. https://nlsp.nasa.gov/explore/data/details/593a6726-8650-551a-8d67-0f03468de92f?dataType=MISSIONS .
75. UTMB, *Campaign 11: Countermeasure and Functional Testing in Head-Down Tilt Bed Rest* (alias CFT70; 70 días; NLSP misión `8e583564-d124-58ce-b44a-a16bb5b5d981`). Ficha confirmada por API NLSP; igual que 73. https://nlsp.nasa.gov/explore/data/details/8e583564-d124-58ce-b44a-a16bb5b5d981?dataType=MISSIONS . Usado en: 06, 07.
76. PhysioNet, **A Multi-Night Instantaneous Heart Rate and Accelerometry Dataset with EEG Sleep Stage Labels** (BIDSleep; 47 adultos, 253 noches, FC y actigrafía en muñeca). Song, T.-A., Zhang, Y., Zhou, Z., & Dutta, J. (2026). PhysioNet, v1.0.1. https://physionet.org/content/bidsleep-dataset/1.0.1/ . DOI de cita 10.13026/rees-1092 (DataCite ✓). Licencia: Open Data Commons Attribution v1.0 según la versión anterior de esta lista; **no registrada en DataCite; no confirmada** (ver sección 4). Acceso abierto sin login. Usado en: 07.
77. BioStudies **S-EPMC8141791** (temperatura central en HDBR; Mendt 2021). Solo metadatos JSON/XML; archivos de datos no listados. Acceso a datos **no confirmado**. Usado en: 01. (Cita de la fuente: 54.)
78. **Alias de 58** (mismo póster de Figshare 10281224). Entrada eliminada como duplicada; citar 58. Licencia verificada: CC BY 4.0 (Figshare API). Usado en: 01, 07.
79. Dunn Rosenberg, J., Jannasch, A., Binsted, K., & Landry, S. (2022). Biobehavioral and psychosocial stress changes during three 8–12 month spaceflight analog missions with Mars-like conditions of isolation and confinement. *Frontiers in Physiology, 13*, Article 898841. https://doi.org/10.3389/fphys.2022.898841. Metadatos confirmados (Crossref; DOAJ 3f12f565bdcf493c8886cff9a53ece5d). Estudio HI-SEAS con monitorización de sueño y actividad mediante wearables (según el resumen). El título no menciona el sueño; citar el artículo, no solo el ID de DOAJ. Usado en: 01.
80. NASA Life Sciences Data Archive (LSDA), solicitud de datos (Twins, HERA y otros estudios de NASA). https://nlsp.nasa.gov/Request/dataRequestFAQ (el dominio antiguo `lsda.jsc.nasa.gov/Request/dataRequestFAQ` redirige aquí; verificado). Acceso controlado, formulario, hasta 6 meses (07). Usado en: 00 (LSDA; "LSAH" no tiene fuente en los archivos), 07, 46.

**Mencionadas en los archivos pero no verificadas (no citar sin revisar):**
- Lee, S. M. C. et al. (2020), npj Microgravity. **(sin fuente identificable — no citar.)** Citada en la solicitud original y en 06; no encontrada en Crossref.
- Basner et al., batería Cognition (Standard Measures). Citada en 06; sin valores normativos verificados.
- LeBlanc et al. y Antonutto et al., citados dentro de Comfort 2021 (02).
- Dinges et al. y Barger et al., citados dentro de `sleep.pdf` (05).
- NASA. (2025). *NASA-STD-3001, Volume 2, Revision E: NASA spaceflight human-system standard, Volume 2: Human factors, habitability, and environmental health* [NTRS 20250004555]. https://ntrs.nasa.gov/citations/20250004555 (registro NTRS creado 2025-05-05; el resumen no menciona CO₂ ni temperatura). Usado en: 02, 00. **Los valores de CO₂ y temperatura de cabina no están verificados.**
- Rangos de referencia del hemograma, Quest Diagnostics (nombre del archivo ISA de OSD-569; 03). Sin documento verificado.

### 1.4 Datasets

61–63: ver sección 1.3 (artículos y datasets OSDR con cita completa).

**Datos de reposo en cama de UTMB en NLSP** (30 experimentos con el flag `public`; 28 con la frase "All datasets are publicly available" y 2 parciales, ver nota; acceso sin login). Usado en: 08, 00.

Nota: los experimentos `950b2ce4-5f5b-5f00-a870-1f24e2897771` (Human Cerebral Cortex Plasticity…) y `26a8b51f-df92-5a52-9fc0-b8b77067246a` (Retention of Skeletal, Musculature, and Postural Status…) dicen "Privacy-protected datasets are available via data request. Remaining datasets are publicly available." No tratarlos como públicos completos.

### 1.5 APIs y portales

81. NASA Life Sciences Portal (NLSP). https://nlsp.nasa.gov/ . Portal SPA; las fichas de experimentos son JavaScript.
82. NLSP, API de metadatos por experimento: `https://nlsp.nasa.gov/api/v1/data/experiments/<GUID>/full`. Misiones: `https://nlsp.nasa.gov/api/v1/data/missions/<GUID>/full`. El campo `archive_status` indica si los datos son públicos. Probada en 6 GUID (06). Usado en: 08.
83. NLSP, API de listado y detalle: `GET https://nlsp.nasa.gov/api/v1/data/{dataType}` (timeout de 120 s). `GET /api/v1/data/MISSIONS/<GUID>` respondió HTTP 400 en la prueba de 06. Usado en: 06.
84. NLSP, descarga masiva: `POST https://nlsp.nasa.gov/api/v1/files/bulk-download` (devuelve un ZIP). Se usó desde navegador con Playwright, secuencial, 2 s entre descargas. Usado en: 08. (Método de descarga, no fuente bibliográfica.)
85. NLSP, Standard Measures. https://nlsp.nasa.gov/resources/standard-measures . Lista 27 medidas en el chunk JS de la página (no es API). Usado en: 06.
86. NASA OSDR, API de búsqueda. https://osdr.nasa.gov/osdr/data/search?term=TERM&type=cgene&size=50 . Usado en: 03.
87. NASA OSDR, Biodata API v2. https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/OSD-XXX/ (con `/files/` y `/assays/`). Usado en: 03.
88. NASA OSDR, descarga de archivos. https://osdr.nasa.gov/geode-py/ws/studies/OSD-XXX/download?source=datamanager&file=NOMBRE . Plantilla; no probada con un archivo concreto. Usado en: 03.
89. NASA NTRS, API de búsqueda de citas. https://ntrs.nasa.gov/api/citations/search . Propuesta del coordinador; no es una fuente.
90. NASA Open APIs (incluye DONKI). https://api.nasa.gov . Propuesta del coordinador; sin uso en los archivos.

### 1.6 Artículos añadidos en la verificación del 2026-11-05

91. Shavers, M., Semones, E., Tomi, L., Chen, J., Straube, U., Komiyama, T., Shurshakov, V., Li, C., & Rühm, W. (2024). Space agency-specific standards for crew dose and risk assessment of ionising radiation exposures for the International Space Station. *Zeitschrift für Medizinische Physik, 34*, 14–30. https://doi.org/10.1016/j.zemedi.2023.06.005 (PMC10919966; publicado en línea en 2023; la fecha de fascículo en Crossref es 2024-02). Metadatos confirmados (Crossref y Europe PMC). Revisión, no fuente primaria de NASA. Cifra: dosis efectiva "usually accumulate at a rate of ∼0.2 to ∼0.5 mSv or more each day of a mission". Usado en: sección 2 (radiación en la ISS).
92. Trudel, G., Shafer, J., Laneuville, O., & Ramsay, T. (2020). Characterizing the effect of exposure to microgravity on anemia: More space is worse. *American Journal of Hematology, 95*(3), 267–273. https://doi.org/10.1002/ajh.25699. Metadatos confirmados (Crossref; publicado en línea 2019-12-24). Fuente original del 48 % de anemia citado en Krittanawong 2022 (09a). Agrupa 721 misiones y 17 336 mediciones de hemoglobina. Usado en: sección 2.

---

## 2. Afirmación clave → fuente

Estado según `verificacion/05-literatura.md` (2026-11-05) salvo donde se indica otra fuente. "08" significa que el archivo no asigna estado por cifra; su encabezado dice "VERIFICADO y descargado".

| Afirmación | Valor | Fuente(s) nº | Estado | Nota |
|---|---|---|---|---|
| Pérdida ósea, cadera y columna | 1–1,5 %/mes | 21 (alias 35), 7 (página de cambios óseos), 37 | ✅ | Promedio NASA de pérdida de aBMD (Leblanc 2000, cosmonautas Mir). Confirmado en `bone_fracture_2024.pdf` p. 10 (05). |
| Pérdida ósea, piernas (metaanálisis) | −0,8 %/mes (IC −1,1 a −0,5) | 42 | ✅ | Verificado en el texto de Stavnichuk 2020 (05, fila 2a). Misiones > 30 días. |
| Sueño en vuelo (ISS) | 6,0–6,5 h/noche (tabla HRR); 6,09 ± 0,67 h (Barger 2014) | 17 (`sleep.pdf` p. 11, Tabla 1); 41 | ✅ | **Corregido.** En la columna de vuelo ningún valor llega a 6,8 h (6,8 h es el valor en tierra). Columna en tierra: 6,3–6,9 h. Valores de la tabla verificados en imagen (05, fila 3d). |
| Sueño programado de 8,5 h | 8,5 h/noche | 17 (`sleep.pdf` p. 7; cita a Klerman & Dijk 2005) | ⚠️ | **No atribuir a Barger 2014**: la cifra no aparece en su resumen (05, fila 3b; texto completo no accesible). Es el sueño de un adulto con oportunidad extendida en condiciones óptimas. |
| Hipnóticos en ISS | 75 % de la tripulación (12 de 16) | 41 | ✅ | Verificado en Barger 2014, Findings (05, fila 3c). |
| Jornada laboral máxima | 6,5 h/día de trabajo | 17 (`sleep.pdf` p. 8); 7 | ✅ | Límite de *trabajo* ("fitness for duty"), no de sueño. El límite de 48 h/semana es recomendación. |
| Sueño de adulto con oportunidad extendida | ~8,5 h/noche | 17 (`sleep.pdf` p. 7) | ⚠️ | Referencia de condiciones óptimas; ver fila anterior. |
| SANS: signos en la tripulación (OCT) | ~70 % | 29 (`sans_2022.pdf` p. 7); 7 | ✅ | "About 70% of crewmembers have the earliest signs of ODE, as determined by OCT" (05, fila 4a). |
| SANS: edema de papila clínicamente significativo (Frisén ≥ 1) | ~15 % | 29 (`sans_2022.pdf` p. 7, 10) | ✅ | **Verificado** (05, fila 4b): "only about 15% of crewmembers develop clinically significant mild ODE, as evidenced by Frisén grade ≥ 1". ~90 % de esos casos son grado 1 (p. 10). |
| SANS: coroides | +18 % al día 150; valor basal a los 90 días | 44 | ✅ | Verificado en Macias 2020 (05, filas 4d–4e). El informe SANS lo cita como 2021; el año correcto es 2020. |
| Límite de dosis de carrera | 600 mSv | 30 (`radiation_cancer_2026.pdf` p. 43, 49) | ✅ | Cita textual del PDF (05, fila 5a). |
| Dosis diaria en la ISS | 0,2–0,5 mSv/día (dosis efectiva) | 91 (Shavers 2023/2024; revisión) | ⚠️ | **Corregido.** El 0,6 mSv/día no tiene respaldo y se retira. No hay cifra NASA primaria en las fuentes locales (05, fila 5b). Otras estimaciones no revisadas (p. ej. 0,5–1 mSv/día en una presentación) no se citan. |
| Pérdida de aptitud física | 12–38 % de la tripulación pierde > 20 % | 7 (página de fitness); 26 (`aerobic_muscle_2024.pdf`); 4 | ✅ | Verificado en la página de NASA "Risk of Reduced Cardiorespiratory and Musculoskeletal Fitness" (05, fila 6a). Pérdida media de fuerza y aptitud de 10–12 % (7). |
| VO₂ al final de la prueba (postvuelo) | −19 % y −26 % | 26 (`aerobic_muscle_2024.pdf` p. 11) | ✅ | **Corregido.** Son dos tripulantes de Gemini VII (1965), no un rango poblacional. En ISS, 15 % pierde > 20 % de capacidad aeróbica (p. 38). |
| Volumen muscular postvuelo | −7 a −12 % | 26 (p. 27) | ✅ | **Corregido.** Medido el día de aterrizaje tras una misión LMS de 17 días (no una misión de ISS); a R+10 volvió a lo previo al vuelo. |
| Volumen plasmático postvuelo | −5 a −19 % | 22 (`cardio_2023.pdf` p. 31–32) | ✅ | Misiones del **Space Shuttle** (05, fila 7a). |
| Intolerancia ortostática al aterrizar | > 80 % (misiones Mir de 4–6 meses) | 22 (p. 25) | ✅ | Cita a Meck et al. 2001 (05, fila 7b). |
| Glucosa, captación (28 días de reposo) | 9,1 → 5,2 mg/kg·pierna/min | 45 | ✅ | Verificado (05, fila 8). Año 2010 (corregido de 2009). Reposo en cama, no vuelo. |
| Volumen urinario | −39 % después del día 60 (−47 % antes del día 30) | 34 (`renal_2024.pdf` p. 11) | ✅ | **Corregido.** El −39 % solo se da en la fase tardía de misión; al inicio fue −47 % (05, fila 9a). |
| Sobresaturación en vuelo | Oxalato de calcio +115 %; brushita +150 % | 34 (p. 12) | ✅ | Son valores **calculados** a partir de orina (Pak 1985; Smith 2015), no medidos en vuelo (05, fila 9b). |
| Frecuencia cardiaca en reposo y mortalidad | **RR** 1,09 por cada 10 lpm (IC95 1,07–1,12); RR 1,45 con FCR > 80 lpm | Adenda 3 (Zhang, CMAJ 2016) | ✅ | **Corregido.** El valor es riesgo relativo, no hazard ratio ("HR 1,09" era la etiqueta incorrecta). Verificado (05, filas 13d–13e). |
| Anemia tras vuelos largos | 48 % de astronautas anémicos al aterrizar | 92 (Trudel 2020); citado en 09a (Krittanawong 2022) | ✅ | Cifra original de Trudel 2020 (721 misiones). Krittanawong la llama "small study"; no lo es (05, filas 10a–10b). |
| Leucocitos postvuelo (R+1 vs L-3) | −26 % | 61 (OSD-569); 03 §3 | ✅ (datos descargados) | Cálculo propio sobre n = 4; no es estadística poblacional. Ver 47 para contexto (texto no leído). |
| Linfocitos postvuelo | −36 % | 61 | ✅ (datos descargados) | Igual que arriba. |
| Temperatura corporal +1 °C en vuelo | — | Ninguna | ❌ | No hay fuente. No usar. |
| Pulso en reposo (antes / durante / después) | 68,6 ± 12,4 / 70,2 ± 11,7 / 74,9 ± 14,1 lpm | 64 (CRF) | 08 | P5–P95 durante: 53–92 lpm. |
| Presión sistólica / diastólica | 115,4 ± 10,2 / 68,7 ± 9,9 mmHg (antes) | 64 | 08 | P5–P95 sistólica 99–135; diastólica 56–86 mmHg. |
| Temperatura corporal (UTMB) | 36,50 ± 0,40 °C (antes) | 64 | 08 | Cambio individual +0,03 ± 0,11 °C. No respalda +1 °C. |
| Respiración | 16,9 ± 1,6 rpm (antes) | 64 | 08 | P5–P95 14–20 rpm. |
| Peso (cambio individual) | −1,1 ± 1,1 kg | 64 | 08 | |
| Pulso, cambio individual | +1,5 ± 4,4 lpm | 64 | 08 | Rango −4,7 a +11,3. |
| Sueño (n = 3) | 7,8 h antes; 7,2 ± 0,5 h durante | 70 (Actilight) | 08 | P5–P95 durante: 6,1–7,7 h. |
| Eficiencia del sueño | 94 % → 81,5 ± 8,7 % | 70 | 08 | |
| Latencia del sueño | 10 → 41 min | 70 | 08 | |
| Glucosa (n pequeño) | 84,7 → 79,9 ± 4,9 mg/dL | 65 (laboratorio) | 08 | |
| Pulso en inclinación (tilt) | +34,7 lpm antes; +56,9 durante; +43,8 después | 66 (tilt) | 08 | 74 pruebas. |
| Duración de pruebas de tilt posteriores | 20,3 vs 22,2 min | 66 | 08 | Interpretación de 08 (posibles cortes por intolerancia). |
| Volumen de datos UTMB | 29 sujetos; ~3.200 registros diarios; ~110 días por sujeto | 64, 70, 71, 65 | 08 | Hemoglobina de 182 en un registro: error de captura (08). |
| Umbral "amarillo" de línea base | > 2 DE personales (DE ≈ 4–5 lpm, ≈ 5 mmHg, 0,1 °C) | 64 (cálculo propio de 08) | 08 | Propuesta de diseño, no clínica. |
| Normas WinSCAT | Sin valores | 71; 06 §4 | Pendiente (06) | 06 no verificó las normas. |
| Inspiration4 (contexto) | Cambios moleculares y cardiovasculares "modestos" | 47 | ⚠️ (02: snippet) | Texto no leído. |
| Dataset de humanos en vuelo | Ningún dataset público de series temporales de FC, PA, sueño o glucosa en vuelo | 01, 07; 80 (LSDA) | sin marca (00 §1) | Los candidatos requieren solicitud. |

---

## 3. Archivos de este repositorio

| Archivo | Contenido | Fuentes nº |
|---|---|---|
| `00-RESUMEN.md` | Resumen y tabla de cifras para umbrales | 4, 5, 7, 17, 21, 22, 26, 29, 30, 34, 35, 37, 41, 42, 44, 45, 61, 64–66, 80 |
| `01-datasets-publicados.md` | Datasets buscados y su disponibilidad | 46, 48, 49, 50, 51, 54, 58, 61–63, 73–75, 77–79, 81–84 |
| `02-valores-cuantitativos.md` | Cifras de papers, con tabla maestra y propuesta de umbral de sueño | 41–47, 52, 53, 55; 80 |
| `03-osdr-datos-humanos.md` | 73 estudios humanos en OSDR; análisis de Inspiration4 | 61, 62, 86, 87, 88 |
| `04-hrp-base-conocimiento.json` | 17 riesgos HRP con enlaces y cifras citadas | 3, 4, 7, 37–40, 13–16, 17, 19–24, 26–30, 33 |
| `04-hrp-resumen.md` | Resumen de las páginas HRP descargadas | 2, 3, 4, 7, 8 |
| `05-hrr-evidencia-cuantitativa.md` | Cifras con cita textual y página de los PDF HRR | 5, 13, 17, 21, 22, 23, 26, 29, 30, 31, 34, 35, 36 |
| `05-hrr-indice.csv` | Índice de informes HRR con URL oficial de PDF | 5, 9–34 |
| `06-standard-measures-nlsp.md` | 27 Standard Measures y catálogo NLSP | 6, 75, 81, 83, 85 |
| `07-datasets-continuacion.md` | Twins, JAXA, ESA, HERA, Concordia, BIDSleep | 6, 46, 50, 51, 56, 57, 73–76, 80 |
| `08-nlsp-utmb-datos-abiertos.md` | Datos abiertos UTMB, vitales, sueño, tilt, laboratorio | 64–72, 81–84 |
| `osdr-inspiration4-clinico.csv` | Hemograma tidy de Inspiration4 (OSD-569) | 61 |
| `utmb/` (CSV procesados), `scripts/`, `nlsp-raw/`, `osdr-raw/`, `hrp-raw/`, `hrr-pdfs/` | Datos y scripts de origen de las tablas anteriores | Las mismas fuentes que sus archivos padre; 64–72, 81–84 (NLSP); 61–62, 86–88 (OSDR); 9–36 (PDF HRR); 1–8 (HRP) |

Notas sobre las fuentes:
- Los DOI de experimentos UTMB (64–72) se leyeron de `08-nlsp-utmb-datos-abiertos.md` y se confirmaron en DataCite (70–72 completados en esta revisión). Los DOI de `nlsp-raw/` (como `10.83263/0njm-h670`) no se citan aquí porque los archivos no los describen.
- Los enlaces `risk.aspx?i=...` de la página HRP aparecen en varias páginas de riesgo (`04-hrp-resumen.md`). Pueden ser navegación del sitio y no evidencia específica.
- Las listas de datasets de `07` (campañas 1, 3 y 11) estaban marcadas como "no verificado"; las fichas ya se confirmaron por API NLSP (73–75). Las de `08` (30 experimentos) se describen en la sección 1.4.

---

## 4. Licencias y términos

Textos citados de las páginas de cada fuente, tal como se leyeron el 2026-11-05. No es asesoría legal.

- **NASA OSDR (OSD-569 y OSD-575; Inspiration4 en general):** la página del estudio indica **"License: CC0-1.0"**, con enlace a https://spdx.org/licenses/CC0-1.0.html. CC0-1.0 es una dedicación al dominio público y no exige atribución; el repositorio pide que se cite el estudio. El ISA (`i_Investigation.txt`) no contiene campo de licencia. Verificado para OSD-569 y OSD-575; los demás estudios, sin comprobar individualmente.
- **NASA Life Sciences Portal (NLSP), datos abiertos de UTMB:** no se encontró ninguna licencia ni texto de términos de uso en las fichas, la guía o los ZIP descargados. Lo que hay: la sección **"Open-Access Data"** ("Data preservation is complete. All datasets are publicly available.") y el pie **"© 2026 NASA Life Sciences Portal. All rights reserved."** Por tanto, los datos se describen como "etiquetados como open access por NASA"; no se presentan como CC0 ni como abiertos sin condiciones.
- **Conflicto a resolver:** los DOI `10.83263/*` de UTMB (p. ej. 70–72) tienen en DataCite la licencia **CC0-1.0** (verificado para `v7n1-ht75`, `sbne-th55` y `7myc-5j86`), mientras que el pie de NLSP dice "All rights reserved". Citar el DOI, no asumir la licencia CC0 para el contenido de NLSP hasta aclarar el conflicto con NASA.
- **PhysioNet:** la licencia no está confirmada en esta verificación. DataCite no registra derechos para `10.13026/rees-1092` (BIDSleep), `10.13026/C2PC7R` (PRCP) ni `10.13026/73w7-x881` (cardioresp-response-orthostat). La versión anterior de esta lista indicaba Open Data Commons Attribution v1.0 para BIDSleep, y la verificación de 06 mencionaba "PhysioNet Health Data License 1.5.0" para PRCP y cardioresp. **Antes de citar la licencia, verificarla en la página de cada dataset.**
- **Figshare 10281224 (fuente 58/78):** CC BY 4.0 (Figshare API).
- **Artículos (texto):** la fuente 48 (npj Microgravity) se cita con licencia CC BY 4.0 según 01; no re-verificado aquí. Las demás fuentes de artículos no tienen licencia registrada en esta lista.
- **Informes HRR (NASA HRP):** los PDF indican "Approved for Public Release" (p. ej., `Fracture.pdf`, 2017; `HRP-ER-CANCER-SR-20260811`, 2026). No se encontró una licencia formal en los archivos.
- **NASA-STD-3001, Space Apps (fuente 14b):** la página de Space Apps indica AFL-3.0 para el proyecto; no revisada. El repositorio de GitHub (14a) no pudo consultarse; su licencia no está verificada.

---

## Adenda (coordinador): fuentes de los archivos 09–12
- 09a: Krittanawong C, et al. (2022). Human Health during Space Travel: State-of-the-Art Review. *Cells* 12(1):40. https://doi.org/10.3390/cells12010040 · https://pmc.ncbi.nlm.nih.gov/articles/PMC9818606/ (alias: 59). Metadatos confirmados (Crossref: 17 autores, 2022-12-22).
- 09b: Jacobs, S., Charvat, J., Reitzel, R., Wear, M., & Van Baalen, M. (2026). Astronauts of the US National Aeronautics and Space Administration (NASA): Cohort profile. *BMJ Open, 16*(6), e112490. https://doi.org/10.1136/bmjopen-2025-112490 · https://pmc.ncbi.nlm.nih.gov/articles/PMC13289012/ (alias: 60). Metadatos confirmados (Crossref).
- 10: Levine ME, et al. (2018). An epigenetic biomarker of aging for lifespan and healthspan. *Aging* 10(4):573–591. https://doi.org/10.18632/aging.101414 (PhenoAge). Las demás referencias citadas en `10-marcadores-salud-global.md` están en la Adenda 3.
- 11/12: NASA OSDR OSD-575, Inspiration4 CMP y paneles séricos: https://osdr.nasa.gov/bio/repo/data/studies/OSD-575
- 11: Overbey, E. G., Kim, J., Tierney, B. T., Park, J., Houerbi, N., Lucaci, A. G., Garcia Medina, S., Damle, N., Najjar, D., Grigorev, K., Afshin, E. E., Ryon, K. A., Sienkiewicz, K., Patras, L., Klotz, R., Ortiz, V., MacKay, M., Schweickart, A., Chin, C. R., … Mason, C. E. (2024). The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. *Nature, 632*(8027), 1145–1154. https://doi.org/10.1038/s41586-024-07639-y . Metadatos confirmados (Crossref; 109 autores; PMC11357981).
- 11: PhysioNet PRCP: Heldt, T. (2016). *Physiologic response to changes in posture* (v1.0.0). PhysioNet. https://doi.org/10.13026/C2PC7R . Licencia no confirmada (ver sección 4).
- 11: PhysioNet cardioresp-response-orthostat: Eke, A., Mukli, P., Stylianou, O., & Hartmann, A. (2021). *Two-tiered response of cardiorespiratory-cerebrovascular networks to orthostatic challenge* (v1.0). PhysioNet. https://doi.org/10.13026/73w7-x881 . Licencia no confirmada (ver sección 4).

## Adenda 2 (coordinador): fuentes de los archivos 13–14
- 13: Hardy, J. G., Theriot, C. A., Oswald, T., & Clément, G. (2025). Spaceflight Standard Measures is a multidisciplinary study that systematically monitors risks to astronaut health and performance. *npj Microgravity, 11*, Article 78. https://doi.org/10.1038/s41526-025-00532-6 · https://pmc.ncbi.nlm.nih.gov/articles/PMC12612093/ (PMID 41224762). Metadatos confirmados (Crossref y Europe PMC). Datos: LSDA vía NLSP, por solicitud.
- 14: NazS2. Astronaut-health-monitoring-system (GitHub). https://github.com/NazS2/Astronaut-health-monitoring-system. Sin verificar (403 del proxy). Licencia por verificar.
- 14: NASA Space Apps Challenge 2014. Astronaut Health Monitoring System. https://2014.spaceappschallenge.org/project/astronaut-health-monitoring-system/ (la página indica licencia AFL-3.0; no revisada).

## Adenda 3 (verificación 2026-11-05): referencias de `10-marcadores-salud-global.md`
- Kodama, S., Saito, K., Tanaka, S., Maki, M., Yachi, Y., Asumi, M., Sugawara, A., Totsuka, K., Shimano, H., Ohashi, Y., Yamada, N., & Sone, H. (2009). Cardiorespiratory fitness as a quantitative predictor of all-cause mortality and cardiovascular events in healthy men and women: A meta-analysis. *JAMA, 301*(19), 2024–2035. https://doi.org/10.1001/jama.2009.681 . Autores y páginas según PubMed (PMID 19454641); Crossref solo devuelve el primer autor. Corrección: el año es 2009, las páginas 2024–2035 y el título lleva el subtítulo "A meta-analysis".
- Leong, D. P., Teo, K. K., Rangarajan, S., Lopez-Jaramillo, P., Avezum, A., Orlandini, A., Seron, P., Ahmed, S. H., Rosengren, A., Kelishadi, R., Rahman, O., Swaminathan, S., Iqbal, R., Gupta, R., Lear, S. A., Oguz, A., Yusoff, K., Zatonska, K., Chifamba, J., … Yusuf, S. (2015). Prognostic value of grip strength: Findings from the Prospective Urban Rural Epidemiology (PURE) study. *The Lancet, 386*(9990), 266–273. https://doi.org/10.1016/S0140-6736(14)62000-6 . Metadatos confirmados (Crossref; 25 autores). Corrección: el texto de 10 citaba un resumen de prensa, no el artículo.
- Jarczok, M. N., Weimer, K., Braun, C., Williams, D. P., Thayer, J. F., Gündel, H. O., & Balint, E. M. (2022). Heart rate variability in the prediction of mortality: A systematic review and meta-analysis of healthy and patient populations. *Neuroscience & Biobehavioral Reviews, 143*, Article 104907. https://doi.org/10.1016/j.neubiorev.2022.104907 . Metadatos confirmados (Crossref). Corrección: el título "RMSSD and mortality" no existe. Revisar la cifra HR 1,56 (cuartil más bajo de RMSSD) contra el resumen antes de usarla.
- Zhang, D., Shen, X., & Qi, X. (2016). Resting heart rate and all-cause and cardiovascular mortality in the general population: A meta-analysis. *Canadian Medical Association Journal, 188*(3), E53–E63. https://doi.org/10.1503/cmaj.150535 . Metadatos confirmados (Crossref; publicado en línea 2015-11-23). Corrección: el valor 1,09 por 10 lpm es riesgo relativo (RR), no HR.
- Windred, D. P., Burns, A. C., Lane, J. M., Saxena, R., Rutter, M. K., Cain, S. W., et al. (2024). Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. *SLEEP, 47*(1), zsad253. https://doi.org/10.1093/sleep/zsad253 . Metadatos confirmados (Crossref; impreso 2024; en línea 2023-09-21).
- Lloyd-Jones, D. M., et al. (2022). Life's Essential 8: Updating and enhancing the American Heart Association's construct of cardiovascular health: A presidential advisory from the American Heart Association. *Circulation, 146*(5). https://doi.org/10.1161/CIR.0000000000001078 . Páginas e18–e43 **no confirmadas** (no devueltas por Crossref ni por PubMed en esta verificación).
- Searle, S. D., et al. (2008). A standard procedure for creating a frailty index. *BMC Geriatrics, 8*, 24. https://doi.org/10.1186/1471-2318-8-24 . Metadatos confirmados (Crossref).

---

## Notas de la lista para el coordinador
- Las cifras de los archivos 00 a 14 no se han revisado más allá de las citas, salvo lo indicado en la sección 2. Las fuentes 55, 56, 57 y Lee 2020 no tienen fuente identificable: retirar sus usos en 02 y 07 o reemplazarlos antes de presentar.
- Pendiente de nueva consulta (Europe PMC y PubMed inestables): páginas de Lloyd-Jones 2022; PMID de Comfort 2021, Fu 2019 y Hardy 2025; cifra 1,56 de Jarczok 2022 en el resumen; licencias de PhysioNet; conflicto de licencia de NLSP.
