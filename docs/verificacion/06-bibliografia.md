# Verificación de bibliografía (06)

Fecha de verificación: 2026-11-05. Revisor independiente (no modifica `FUENTES.md` ni los archivos de datos).

**Alcance:** las 90 fuentes numeradas de `FUENTES.md`, las dos adendas al final (09–14) y las referencias del informe indicadas en la solicitud (Overbey 2024, Hardy 2025, Krittanawong 2022, Jacobs 2026, Barger 2014, Stavnichuk 2020, Macias 2020, Cree 2010, Levine 2018, Kodama 2009, Lloyd-Jones 2022, Windred 2024, Searle 2008, CMAJ 2016, Leong 2015, Jarczok 2022, PhysioNet ×3, OSD-569 y OSD-575).

**Métodos**
- DOI de revistas: Crossref API (`api.crossref.org/works/<doi>`), ≤ 2 consultas/s, sin errores 429.
- DOI 10.83263/* (NLSP) y 10.13026/* (PhysioNet): DataCite API y resolución de `doi.org`.
- PMCID: Europe PMC (`PMCID:<id>`). PMID y DOI de Kodama: PubMed E-utilities (esummary).
- NLSP: `api/v1/data/{experiments|missions}/<GUID>/full` para 6 GUID.
- OSDR: `osdr.nasa.gov/osdr/data/osd/meta/<n>` (OSD-191, 569, 575) y `visualization.osdr.nasa.gov/biodata/api/v2/`.
- URL: `curl` con el bundle de CA del proxy (`/root/.ccr/ca-bundle.crt`); título de la página o texto del PDF (`pdftotext`) comparado con la descripción.
- Figshare API para 10281224; DOAJ API para 3f12f565…; NTRS API para NASA-STD-3001.

**Limitaciones**
- Europe PMC y PubMed respondieron 500/503 de forma intermitente. No se pudieron confirmar por esa vía: páginas de Lloyd-Jones 2022 (146(5): e18–e43 según conocimiento previo, no devueltas por Crossref), PMID de Comfort 2021, Fu 2019 y Hardy 2025.
- `spaceappschallenge.org` (fuente 1): error de certificado TLS con el bundle del proxy. No se desactivó TLS; queda sin verificar.
- `github.com/NazS2/...` (fuente 14): 403 del proxy; el repositorio no se pudo consultar.
- Las páginas de NLSP y OSDR son aplicaciones JavaScript (HTML sin título útil). Se verificaron por API, no por el `<title>`.
- Licencias de OSD-569/575 y PhysioNet: no confirmadas (el texto de licencia no aparece en `i_Investigation.txt` según búsqueda por texto).

**Leyenda de estado:** OK = coincide con la fuente primaria. CORREGIR = dato incorrecto, incompleto o inconsistente que hay que cambiar. NO RESUELVE = no se pudo identificar la fuente o acceder a ella.

---

## Resumen de problemas

1. **Placeholder citado como informe (fuentes 11, 12, 24, 27):** las cuatro apuntan a `Multiple Evidence Reports.pdf`. Es una página de 1 párrafo ("Multiple Evidence Reports are available for this Risk. Please see..."), tanto la copia remota como `hrr-pdfs/multiple_evidence_reports.pdf`. No es un informe. La 12 (renal) tiene informe propio (fuente 34); la 27 (alimentación) duplica la 32.
2. **Duplicados:** 25 y 28 son el mismo PDF (Hypoxia and DCS, 2023); 58 y 78 son el mismo póster de Figshare (10281224); 21 y 35 son dos versiones del informe de fractura ósea (60 y 34 páginas).
3. **Citas incompletas que sí se pueden completar:** Mendt 2021 (54), GLDS-191 = OSD-191 con publicación Turroni 2017 (63), NASA-STD-3001 Vol. 2 Rev. E (NTRS 20250004555), HI-SEAS 2022 (79, DOAJ), Collet/Figshare (58), Leong 2015 (DOI 10.1016/S0140-6736(14)62000-6), Jarczok 2022 (DOI 10.1016/j.neubiorev.2022.104907 y título real), CMAJ 2016 (autores Zhang, Shen, Qi; DOI 10.1503/cmaj.150535).
4. **Citas sin fuente identificable:** 55 (Sci Rep 2022, 10 astronautas), 56 (Basner 2019, IAC), 57 (Mars-500 PLoS ONE y SIRIUS-19), y Lee 2020 (npj Microgravity, no encontrado en Crossref). No hay indicios de invención verificada, pero no se pueden citar como están.
5. **Año incorrecto:** Cree 2009 en `00-RESUMEN.md` y `02-valores-cuantitativos.md` (la fuente es 2010; vol. 59(5)). Collet/Figshare: 2013 en FUENTES, 2019 en Figshare.
6. **Licencia y acceso:** Figshare 10281224 es CC BY 4.0 (FUENTES dice "no verificada" y "HTTP 403"; ya no aplica). HI-SEAS 2022 (79): el ID DOAJ sí corresponde a un artículo con monitorización de sueño y actividad con wearables; ya se puede verificar.
7. **Títulos o descripciones erróneos:** 40 (Degen.pdf) no trata de cánceres, sino de enfermedades degenerativas (cardiovasculares y otros tejidos) por radiación. 14 (HSIA): el PDF se titula "Risk of Inadequate Human-System Integration Architecture", no "...Earth Independent Human-Systems Operations". Jacobs 2026: título abreviado en FUENTES. Jarczok 2022 aparece como "RMSSD and mortality", título que no existe.
8. **DOI faltantes de NLSP que sí existen:** Actilight 10.83263/v7n1-ht75 (70), WinSCAT 10.83263/sbne-th55 (71), DXA 10.83263/7myc-5j86 (72).
9. **Kodama 2009:** Crossref solo devuelve 1 autor (metadatos incompletos). PubMed confirma 12 autores, JAMA 301(19):2024–2035 y el subtítulo "A Meta-analysis".
10. **Enlace redirigido:** `lsda.jsc.nasa.gov/Request/dataRequestFAQ` (80) redirige a `nlsp.nasa.gov/Request/dataRequestFAQ`.
11. **Año a revisar:** 9 (Medical.pdf, "s/f"; el nombre del archivo fuente sugiere 2017, sin confirmar). 25/28 (PDF aprobado el 31-oct-2023, FUENTES dice 2024).
12. **Sin verificar por limitación técnica:** 1 (SpaceApps, TLS), 14 (GitHub NazS2, 403), 84 (bulk-download, endpoint POST), Lloyd-Jones (páginas), y las autorías de Comfort/LeBlanc/Antonutto no verificadas en el texto.

---

## Tabla de verificación

Notación de datos verificados: "Crossref" = metadatos de Crossref; "PMC" = Europe PMC; "API" = API oficial del repositorio.

### A. Fuentes numeradas de FUENTES.md (1–90)

| n° | referencia declarada | metadatos verificados | estado | corrección propuesta |
|---|---|---|---|---|
| 1 | Space Apps 2026, desafío "Health Monitoring Software" (URL) | TLS: certificado no válido con el bundle del proxy; no se pudo leer la página | NO RESUELVE | Verificar a mano la URL. No cambiar la referencia. |
| 2 | NASA HRP, https://www.nasa.gov/hrp/ | HTTP 200; título "Human Research Program - NASA" | OK | Ninguna. |
| 3 | NASA HRP, hazards (cinco páginas hazard-*) | HTTP 200 en las 5: "Hazard: Space Radiation", "Hazard: Isolation and Confinement", "Hazard: Distance From Earth", "Hazard: Gravity Fields", "Hazard: Hostile/Closed Environments" | OK | Ninguna. |
| 4 | NASA HRP, riesgos https://www.nasa.gov/hrp/risks/ | HTTP 200; "Risks of Human Spaceflight - NASA" | OK | Ninguna. |
| 5 | Human Research Roadmap, portal de evidencia | HTTP 200 | OK | Ninguna. |
| 6 | NASA HRP, página NLSP (/hrp/nlsp) | HTTP 200 con redirección a /hrp/nlsp/; "NASA Life Sciences Portal - NASA" | OK | Usar la URL con barra final. |
| 7 | 17 páginas de riesgo `nasa.gov/reference/<slug>/` (+ cinco hazards) | Las 22 URL del JSON `04-hrp-base-conocimiento.json` responden 200 y el título coincide con el riesgo (p. ej. "Risk of Hypoxia - NASA", "Risk from Inadequate Sleep and Irregular Schedules - NASA") | OK | Ninguna. La plantilla `<slug>` no es una URL concreta; citar la lista. |
| 8 | NASA HRP, contramedidas | HTTP 200; "Human Health Countermeasures - NASA" | OK | Ninguna. |
| 9 | Medical.pdf ("s/f" en FUENTES y en el índice CSV) | HTTP 200 (PDF). Texto: "Evidence Report: Risk of Adverse Health Outcomes and Decrements in Performance due to In-Flight Medical Conditions". Metadatos del archivo: "Medical_2017_IOM.docx" | CORREGIR | Título según PDF. Año: "s/f"; sugerir 2017 solo como hipótesis a confirmar. |
| 10 | Dust.pdf (s/f) | HTTP 200. "Evidence Report: Risk of Adverse Health & Performance Effects of Celestial Dust Exposure" | OK | Ninguna (s/f). |
| 11 | Multiple Evidence Reports.pdf, Risk of Ineffective or Toxic Medications | PDF de 1 página: aviso "Multiple Evidence Reports are available for this Risk..." (copia remota y local idénticas) | CORREGIR | No citar ese PDF. Citar la página del riesgo: https://humanresearchroadmap.nasa.gov/Risks/?i=177 (URL de la columna `riesgo_url` del CSV). Indicar que no hay informe PDF descargable. |
| 12 | Multiple Evidence Reports.pdf, Risk of Renal Stone Formation | Mismo PDF placeholder | CORREGIR | Sustituir por la fuente 34 (2024 Renal Evidence Report_Final.pdf, "Evidence Report: Risk of Renal Stone Formation", 42 p.). |
| 13 | HRP-ER-BMED-HFBP-20250210.pdf (2025) | HTTP 200. "Evidence Report: Risk of Adverse Cognitive or Behavioral Changes and Psychiatric Disorders..." (222 p.) | OK | Ninguna. |
| 14 | Risk of Inadequate HSIA approved FINAL_6-13-2023.pdf (2023) | HTTP 200. Título en el PDF: "Evidence Report: Risk of Inadequate Human-System Integration Architecture" (254 p.). FUENTES y CSV: "Risk of Adverse Mission Outcomes Due to Earth Independent Human-Systems Operations" (título de la página de riesgo, i=175) | CORREGIR | Citar con el título del PDF; el nombre de la página de riesgo como "también conocido como". Año 2023 correcto. |
| 15 | OP Dynamic Loads EB FINAL_11-30-22.pdf (2022) | HTTP 200. "Evidence Report: Risk of Injury Due to Dynamic Loads" (106 p.) | OK | Ninguna. |
| 16 | Team 2022 - Evidence Report FINAL_5-9-2024.pdf (2024) | HTTP 200. "...Risk of Performance and Behavioral Health Decrements Due to Inadequate Cooperation, Coordination, Communication, and Psychosocial..." (114 p.) | OK | Ninguna. |
| 17 | Sleep.pdf (s/f) | HTTP 200. "Evidence Report: Risk of Performance Decrements and Adverse Health Outcomes Resulting from Sleep Loss, Circadian Desynchronization, and Work..." (83 p.) | OK | Ninguna. |
| 18 | IVD.pdf (s/f) | HTTP 200. Capítulo 5 del "HRP-47060 Human Health Countermeasures Element Evidence Book" (10 p.) | OK | Citar como capítulo de libro de evidencias, no como informe de riesgo. |
| 19 | Host_Micro EB_Final 7-6-22.pdf (2022) | HTTP 200. "Evidence Report: Risk of Adverse Health Effects Due to Host-Microorganism Interactions" (29 p.) | OK | Ninguna. |
| 20 | SM Evidence Report 2022_FINAL 6-13-2023.pdf (2023) | HTTP 200. "Evidence Report: Risk of Altered Sensorimotor/Vestibular Function..." (160 p.) | OK | Ninguna. |
| 21 | Bone Fracture Evidence Report_07-18-2024.pdf (2024) | HTTP 200. "Evidence Report: Risk of Bone Fracture due to Spaceflight-induced Changes to Bone" (60 p.) | OK | Ninguna. Ver 35 (duplicado). |
| 22 | Cardio Risk EB 2022 FINAL_4-3-2023.pdf (2023) | HTTP 200. "Evidence Report: Risk of Cardiovascular Adaptations..." (161 p.) | OK | Ninguna. |
| 23 | IMMUNE EB Update 2021 v02 FINAL_6-15-22.pdf (2021) | HTTP 200. "Evidence Report: Risk of Crew Adverse Health Event Due to Altered Immune Response" (56 p.) | OK | Año: 2022 según la fecha final del nombre; "2021" es la versión de actualización. Aclarar. |
| 24 | Multiple Evidence Reports.pdf, Risk of Mission Impacting Injury (EVA) | Mismo PDF placeholder | CORREGIR | Citar la página del riesgo EVA: https://humanresearchroadmap.nasa.gov/Risks/?i=84 (no hay informe PDF local). Cita verificada del riesgo: "Risk of Injury and Compromised Performance from Spacewalks - NASA" (ver fuente 7). |
| 25 | Evidence Report Hypoxia and DCS_FINAL_1-8-2024.pdf (2024) | HTTP 200 y local. "Evidence Report: Risk of Reduced Crew Health and Performance due to Decompression Sickness and Hypoxia", **aprobado el 31 de octubre de 2023** (94 p.). Nombre del archivo: 1-8-2024 | CORREGIR | Un solo informe que cubre DCS e hipoxia. Año: 2023 (aprobación), con el 2024 del nombre del archivo como fecha de versión. Unificar con la 28. |
| 26 | Evidence report aerobic and muscle_FINAL 4-3-2024.pdf (2024) | HTTP 200. "RISK TITLES: ... REDUCED MUSCLE MASS, STRENGTH & ENDURANCE (MUSCLE) AND ... REDUCED AEROBIC CAPACITY (AEROBIC)" (169 p.) | OK | Nota: el informe cubre dos riesgos (muscle y aerobic). La descripción de FUENTES corresponde al riesgo aerobic. |
| 27 | Multiple Evidence Reports.pdf, Risk of Performance Decrement ... Food and Nutrition | Mismo PDF placeholder. Existe el informe propio (fuente 32) | CORREGIR | Duplicado de la 32. Eliminar la 27 o apuntarla al informe de la 32. |
| 28 | Evidence Report Hypoxia and DCS_FINAL_1-8-2024.pdf, Risk of Reduced Crew Health ... Hypoxia | Mismo PDF que la 25 | CORREGIR | Duplicado de la 25. Una sola entrada: "Risk of Reduced Crew Health and Performance due to Decompression Sickness and Hypoxia". |
| 29 | SANS EB 2022 FINAL_8-15-22.pdf (2022) | HTTP 200. "Evidence Report: Risk of Spaceflight Associated Neuro-ocular Syndrome (SANS)" (66 p.) | OK | Ninguna. |
| 30 | HRP-ER-CANCER-SR-20260811.pdf (2026) | HTTP 200. "Evidence Report: Risk of Ionizing Radiation Carcinogenesis... Approved for Public Release: 2026" (75 p.) | OK | Ninguna. |
| 31 | Osteo.pdf (s/f; enlace complementario) | HTTP 200. "Evidence Report: Risk of Early Onset Osteoporosis Due to Space Flight" (119 p.) | OK | Completar título. |
| 32 | Food HRP-Evidence Report FINAL_4-15-24.pdf (2024) | HTTP 200. "Evidence Report: Risk of Performance Decrement and Crew Illness Due to Inadequate Food and Nutrition" (46 p.) | OK | Ninguna. Esta es la referencia válida para alimentación (ver 27). |
| 33 | Nutrition ER_human_adaptation_2020_final.pdf (2020) | HTTP 200. "Human Adaptation to Spaceflight: The Role of Nutrition" (135 p.) | OK | Completar título. |
| 34 | 2024 Renal Evidence Report_Final.pdf (2024) | HTTP 200. "Evidence Report: Risk of Renal Stone Formation", Exploration Medical Capabilities (42 p.) | OK | Ninguna. Referencia válida para cálculo renal (ver 12). |
| 35 | Fracture.pdf (Bone Fracture Evidence Report; local, sin URL) | Local, 34 p. Mismo título que la 21 ("Risk of Bone Fracture due to Spaceflight-induced Changes to Bone"), pero la 21 tiene 60 p. | CORREGIR | Posible duplicado o versión anterior. Indicar cuál versión se cita, la fecha y la URL de origen. No está registrada la URL. |
| 36 | hhc_risk_approach_plan_2026.pdf (sin URL) | Local, 9 p. Texto: "HRP Risk Approach Plans For the Human Health..." | CORREGIR | Falta la URL de origen. Citar el título completo del PDF. |
| 37 | ochmo-tb-030-bone-loss.pdf (nasa.gov/wp-content/uploads/2023/12/...) | HTTP 200. Título del PDF: "NASA-STD-3001 Medical Technical Brief: Bone Loss, OCHMO-MTB-013 Rev D" (26 p.) | CORREGIR | El nombre del archivo ("tb-030") no coincide con el identificador del documento ("MTB-013 Rev D"). Citar el identificador del PDF. |
| 38 | whatisyourspaceheight.pdf (2018) | HTTP 200. "WHAT'S YOUR SPACE HEIGHT?", fecha 4/25/2018 (7 p.) | OK | Ninguna. |
| 39 | Space training fact sheet (2015 en la URL) | HTTP 200. "Training for space: Astronaut training and mission preparation", NASA JSC (2 p.) | OK | Ninguna. |
| 40 | Degen.pdf (URL con ?rnd=...) | HTTP 200. "Evidence Report: Risk of Cardiovascular Disease and Other Degenerative Tissue Effects from Radiation Exposure" (52 p.) | CORREGIR | La descripción "riesgo de cánceres por radiación" es incorrecta. Cambiar a: "riesgo de enfermedad cardiovascular y otros efectos degenerativos por radiación". Quitar el parámetro ?rnd. |
| 41 | Barger, L., et al. (2014). Lancet Neurology 13(9), 904–912. doi:10.1016/S1474-4422(14)70122-X | Crossref: título, 8 autores (Barger, Flynn-Evans, Kubey, Walsh, Ronda, Wang…), The Lancet Neurology, 13(9), 904–912, 2014-09 | OK | Ninguna. FUENTES ya dice "Lancet Neurology" (no PLoS Medicine). |
| 42 | Stavnichuk, M., et al. (2020). npj Microgravity 6, 13. doi:10.1038/s41526-020-0103-2 | Crossref: título ✓, 5 autores ✓, vol. 6, art. 13, 2020-05-05. PMC7200725 = mismo artículo (PMID 32411816) | OK | Ninguna. |
| 43 | Comfort, P., et al. (2021). Sports Medicine 51(10), 2097–2114. doi:10.1007/s40279-021-01496-9 | Crossref: título ✓, Sports Med, vol. 51(10), 2097–2114; en línea 2021-06-11 | OK | PMID 34115344 no confirmado (Europe PMC caído). Las citas internas (LeBlanc, Antonutto) no se verificaron. |
| 44 | Macias, B., et al. (2020). JAMA Ophthalmology 138(5), 553. doi:10.1001/jamaophthalmol.2020.0673 | Crossref: título ✓, JAMA Ophthalmol, 138(5), 553, 2020-05-01; 13 autores (6 listados + "et al." correcto) | OK | Ninguna. |
| 45 | Cree, M., et al. (2010). Metabolism 59(5), 703–710. doi:10.1016/j.metabol.2009.09.014 | Crossref: 2010, vol. 59(5), 703–710. PMC2856785 (PMID 19919871): epub 2009-11-17, print 2010 | CORREGIR | Año 2010 (no 2009). Corregir "Cree 2009" en `00-RESUMEN.md` y `02-valores-cuantitativos.md`. |
| 46 | Garrett-Bakelman, F., et al. (2019). Science 364(6436). doi:10.1126/science.aau8650 | Crossref: 2019-04-12, Science 364(6436), art. eaau8650; 82 autores. PMC7580864 = mismo artículo | OK | Añadir número de artículo "eaau8650". |
| 47 | Jones, C., et al. (2024). Nature 632(8027), 1155–1164. doi:10.1038/s41586-024-07648-x | Crossref: título ✓ ("Molecular and physiological changes in the SpaceX Inspiration4 civilian crew"), vol. 632(8027), 1155–1164. PMC11357997 ✓ | OK | Ninguna. |
| 48 | Sanders, L., et al. (2024). npj Microgravity 10(1). doi:10.1038/s41526-024-00393-5 | Crossref: título ✓, vol. 10, art. 56, 2024-05-14. PMC11094041 ✓ | OK | Añadir "Article 56". |
| 49 | Bonmatí-Carrión, M., et al. (2024). npj Microgravity 10(1). doi:10.1038/s41526-024-00387-3 | Crossref: título ✓, vol. 10, art. 42, 2024-03-29. PMC10980770 ✓ | OK | Añadir "Article 42". |
| 50 | Solbiati, S., & Caiani, E. (2025). npj Microgravity 11(1). doi:10.1038/s41526-025-00509-5 | Crossref: título ✓, vol. 11, art. 48, 2025-07-31. PMC12313925 ✓ | OK | Ninguna. |
| 51 | Otsuka, K., et al. (2021). Scientific Reports 11(1). doi:10.1038/s41598-021-94478-w | Crossref: título ✓, vol. 11, art. 14907, 2021-07-21. PMC8295322 ✓ | OK | Añadir "Article 14907". |
| 52 | Baevsky, R., et al. (2007). J Appl Physiol 103(1), 156–161. doi:10.1152/japplphysiol.00137.2007 | Crossref: título ✓, 9 autores, vol. 103(1), 156–161, 2007-07 | OK | Ninguna. |
| 53 | Fu, Q., et al. (2019). Circulation 140, 729–738. doi:10.1161/CIRCULATIONAHA.119.041050 | Crossref: título ✓, 10 autores, vol. 140, **issue 9**, 729–738, 2019-08-27 | OK | Añadir "(9)". PMID 31319685 no confirmado (Europe PMC caído). |
| 54 | Mendt, S., et al. (2021). Long-term bed rest delays the circadian phase of core body temperature. **Cita incompleta** (revista y DOI no confirmados) | Crossref y Europe PMC: Mendt S, Brauns K, Friedl-Werner A, Belavy DL, Steinach M, Schlabs T, Werner A, Gunga HC, Stahn AC. Frontiers in Physiology 12:658707, epub 2021-05-10. DOI 10.3389/fphys.2021.658707. PMC8141791 = mismo artículo | CORREGIR | Completar: Mendt, S., Brauns, K., Friedl-Werner, A., Belavy, D. L., Steinach, M., Schlabs, T., Werner, A., Gunga, H.-C., & Stahn, A. C. (2021). Frontiers in Physiology, 12, Article 658707. https://doi.org/10.3389/fphys.2021.658707 |
| 55 | Artículo de Sci Rep 2022 sobre 10 astronautas (FC, VFC, ritmos circadianos). **Cita incompleta** | Búsqueda en Crossref sin resultado. Candidato no confirmado: Otsuka et al. 2018, Sci Rep 8:10381 (doi:10.1038/s41598-018-28740-z), "Circadian challenge of astronauts' unconscious mind... estimated by heart rate variability". Ni año ni número de sujetos coinciden | NO RESUELVE | Identificar el artículo o eliminar la cita. No citar el candidato sin revisar su contenido (año 2018, no 2022). |
| 56 | Basner, M., et al. (2019), presentación IAC 2019 (Concordia / VIPER / Somnopole). **Cita incompleta** | Sin registro en Crossref ni PubMed. Es una presentación de congreso | NO RESUELVE | Buscar en las actas del IAC 2019 o eliminar. |
| 57 | Artículos de Mars-500 (PLoS ONE) y SIRIUS-19. **Cita incompleta** | Búsqueda sin coincidencia clara. Candidatos no relacionados con el uso declarado (p. ej. Arbeille et al. 2014, PLoS ONE 9(1):e83063, sobre arteria periférica en Mars-500) | NO RESUELVE | Identificar el artículo concreto (título, año, DOI) o eliminar. |
| 58 | Collet et al. (WCSM 2013), póster "Sleep during an Antarctic overwintering...", Figshare 10281224. **Cita incompleta** | Figshare API: título ✓; autores: Collet G, Mairesse O, McDonald-Nethercott E, Ducrot YM, Meeusen R, Pattyn N; tipo "poster"; publicado 2019-11-10; licencia CC BY 4.0; DOI 10.6084/m9.figshare.10281224.v1 | CORREGIR | Año 2019 según Figshare (no 2013). Citar: Collet, G., Mairesse, O., McDonald-Nethercott, E., Ducrot, Y. M., Meeusen, R., & Pattyn, N. (2019). *Sleep during an Antarctic overwintering: Comparing an altitude base and a coastal station* [Poster]. Figshare. https://doi.org/10.6084/m9.figshare.10281224.v1. Si se conserva el WCSM 2013, citarlo aparte y no como esta entrada. Ver también 78 (duplicado). |
| 59 | PMC9818606 (artículo aportado por el usuario) | PMC: Krittanawong C et al., "Human Health during Space Travel: State-of-the-Art Review", Cells 12:40 (2022), doi:10.3390/cells12010040 | OK | Es el mismo artículo que la adenda 09. Fusionar. |
| 60 | PMC13289012 (artículo aportado por el usuario) | PMC: Jacobs S et al., "Astronauts of the US National Aeronautics and Space Administration (NASA): cohort profile", BMJ Open (2026), DOI 10.1136/bmjopen-2025-112490 | OK | Es el mismo artículo que la adenda 09. Fusionar. |
| 61 | NASA OSDR, OSD-569 "Whole Blood Measurements" (hemograma) | API OSDR: "Whole Blood Measurements from the SpaceX Inspiration4 Mission (RNA-seq, epitranscriptome, WGS, clonal hematopoiesis, CBC)" | OK | Licencia no confirmada (búsqueda de "licen" en `i_Investigation.txt` sin resultado legible). Usar el título completo. |
| 62 | OSD-570 a OSD-687 (Inspiration4) | API OSDR: OSD-575 y OSD-569 verificados. Los demás (570–574, 630, 656, 687) no se consultaron individualmente en esta revisión; la fuente 11 dice haber validado 630, 656 y 687 | OK (parcial) | Ninguna. Consultar cada OSD antes de citarla individualmente. |
| 63 | NASA GeneLab/OSDR, **GLDS-191** (microbiota Mars500). **Cita incompleta** (acceso y licencia no confirmados) | La URL redirige a OSDR **OSD-191** (GLDS-191 = OSD-191). API: "Temporal dynamics of the gut microbiota in people sharing a confined environment, a 520-day ground-based space simulation, MARS500". Publicación asociada (Crossref): Turroni, S., et al. (2017), Microbiome 5:39, doi:10.1186/s40168-017-0256-8 | CORREGIR | Citar: Turroni, S., Rampelli, S., Biagi, E., Consolandi, C., Severgnini, M., Peano, C., Quercia, S., Soverini, M., Carbonero, F. G., Bianconi, G., Rettberg, P., Canganella, F., Brigidi, P., & Candela, M. (2017). Temporal dynamics of the gut microbiota in people sharing a confined environment, a 520-day ground-based space simulation, MARS500. *Microbiome, 5*, Article 39. https://doi.org/10.1186/s40168-017-0256-8. Dataset: NASA OSDR, OSD-191 (GLDS-191). |
| 64 | UTMB, Case Report Form. DOI 10.83263/wjw1-ta27 | DataCite: "Case Report Form" (Ames Research Center, 2026, CC0). doi.org → NLSP eeb9bd34-bdd4-5115-b139-adf2c9927962 | OK | Ninguna. |
| 65 | UTMB, Clinical Laboratory Assessment. DOI 10.83263/rank-k271 | DataCite: "Clinical Laboratory Assessment (Flight Analog)" (2026, CC0). doi.org → NLSP | OK | Ninguna. Añadir "(Flight Analog)". |
| 66 | UTMB, Neuroendocrine and Cardiovascular Response to Tilt. DOI 10.83263/gz1q-a824 | DataCite: "Neuroendocrine and Cardiovascular Response to Tilt (Flight Analog)" (2026, CC0) | OK | Añadir "(Flight Analog)". |
| 67 | UTMB, Cardiovascular Function. DOI 10.83263/kw2c-zj80 | DataCite: "Bed Rest Standard Measures: Cardiovascular Function" (2026, CC0) | OK | Añadir el prefijo "Bed Rest Standard Measures:". |
| 68 | UTMB, Plasma Volume. DOI 10.83263/4dzb-2267 | DataCite: "Bed Rest Standard Measures: Plasma Volume" (2026, CC0) | OK | Añadir el prefijo "Bed Rest Standard Measures:". |
| 69 | UTMB, Aerobic Capacity. DOI 10.83263/w056-8t76 | DataCite: "Aerobic Capacity (Flight Analog)" (2026, CC0) | OK | Añadir "(Flight Analog)". |
| 70 | UTMB, Actilight. NLSP cd8a4a16-fcfd-5c32-a61f-22c590a10b35. **"DOI no indicado"** | API NLSP: "Bed Rest Standard Measures: Actilight"; registro con DOI **10.83263/v7n1-ht75** (DataCite: mismo título, Putcha L., 2026). Estado de archivo: publicado | CORREGIR | Añadir el DOI 10.83263/v7n1-ht75. |
| 71 | UTMB, WinSCAT. NLSP 80ee3231-7c42-5be4-b6c2-b8c788feeb50. **"DOI no indicado"** | API NLSP: "Neurocognitive Assessment (WinSCAT) (Cognitive Assessment Tool for Windows) (Flight Analog)"; DOI **10.83263/sbne-th55** (DataCite, 2026) | CORREGIR | Añadir el DOI 10.83263/sbne-th55. |
| 72 | UTMB, Bone Densitometry Assessment (DXA). NLSP 4469ebdc-0a65-55e8-bbff-3cf6b044c4c6. **"DOI no indicado"** | API NLSP: "Bone Densitometry Assessment (Flight Analog)"; DOI **10.83263/7myc-5j86** (DataCite, Sibonga JD, 2026) | CORREGIR | Añadir el DOI 10.83263/7myc-5j86. |
| 73 | UTMB, bed rest campaign 1. NLSP misión 6eaf1654-72d4-5d71-a9dd-a02e674c6473 | API NLSP: "Campaign 1 Flight Analog Bed Rest Study" (alias C1, "UTMB Campaign 1"). El estado de archivo a nivel de misión no aparece en el registro | OK | Actualizar: la ficha ya se pudo verificar por API (la nota de 07 decía que no). |
| 74 | UTMB, bed rest campaign 3. NLSP misión 593a6726-8650-551a-8d67-0f03468de92f | API NLSP: "Campaign 3 Flight Analog Bed Rest Study" ("UTMB Campaign 3") | OK | Igual que la 73. |
| 75 | UTMB, campaign 11 (CFT70). NLSP misión 8e583564-d124-58ce-b44a-a16bb5b5d981 | API NLSP: "Campaign 11: Countermeasure and Functional Testing in Head-Down Tilt Bed Rest" (alias CFT70) | OK | Igual que la 73. |
| 76 | PhysioNet, BIDSleep. DOI 10.13026/rees-1092 (physionet.org/content/bidsleep-dataset/1.0.1/) | DataCite: "A Multi-Night Instantaneous Heart Rate and Accelerometry Dataset with EEG Sleep Stage Labels" (Song T-A, Zhang Y, Zhou Z, Dutta J; PhysioNet, 2026). doi.org → 200. Página: "...v1.0.1" | OK | Añadir el título completo del dataset (BIDSleep es el nombre corto). Licencia ODC-BY 1.0 no confirmada en DataCite. |
| 77 | BioStudies S-EPMC8141791 (temperatura central HDBR; Mendt 2021) | OmicsDI y BioStudies: título "Long-Term Bed Rest Delays the Circadian Phase of Core Body Temperature". PMC8141791 = Mendt et al. 2021 (ver 54) | OK | Relacionar con la 54 completa. Acceso a los datos no confirmado. |
| 78 | Figshare 10281224 (póster "Concordia"). Licencia no verificada; HTTP 403 | Figshare API: título "Sleep during an Antarctic overwintering: comparing an altitude base and a coastal station", poster, CC BY 4.0, 2019-11-10. Mismo ítem que la 58 | CORREGIR | Duplicado de la 58. Eliminar la entrada 78 o fusionarla con la 58. Actualizar licencia (CC BY 4.0). Quitar "HTTP 403" (ya no aplica). |
| 79 | HI-SEAS 2022 (sueño y actividad, wearables). DOAJ 3f12f565bdcf493c8886cff9a53ece5d. **No confirmado (403)** | DOAJ API y Crossref: Dunn Rosenberg, J., Jannasch, A., Binsted, K., & Landry, S. (2022). "Biobehavioral and psychosocial stress changes during three 8–12 month spaceflight analog missions with Mars-like conditions of isolation and confinement". Frontiers in Physiology 13, art. 898841, DOI 10.3389/fphys.2022.898841. El resumen menciona HI-SEAS y "wearables monitoring (sleep and activity levels)" | CORREGIR | Actualizar: estado confirmado. Citar con DOI. El título no menciona sueño; citar el artículo, no solo el ID DOAJ. |
| 80 | NASA LSDA, solicitud de datos. https://lsda.jsc.nasa.gov/Request/dataRequestFAQ | HTTP 200 tras redirección a https://nlsp.nasa.gov/Request/dataRequestFAQ ("NASA Life Sciences Portal") | CORREGIR | Cambiar a https://nlsp.nasa.gov/Request/dataRequestFAQ (el dominio antiguo redirige). |
| 81 | NASA Life Sciences Portal https://nlsp.nasa.gov/ | HTTP 200; "NASA Life Sciences Portal (NLSP)". SPA | OK | Ninguna. |
| 82 | NLSP API `/api/v1/data/experiments/<GUID>/full` y `/missions/<GUID>/full` | Probada para 6 GUID (200 OK, JSON con `record`, `related`, `__doi`) | OK | Ninguna. |
| 83 | NLSP API `GET /api/v1/data/{dataType}` (timeout 120 s) | No probada en esta revisión (solo `/full`). La fuente 06 reporta 400 en `/MISSIONS/<GUID>` | OK (no probada) | Ninguna. Probar antes de citar el endpoint. |
| 84 | NLSP descarga masiva `POST /api/v1/files/bulk-download` | GET devuelve 404 (esperable en un endpoint POST); no se probó con POST | NO RESUELVE | No es una fuente bibliográfica. Documentar el método, no la URL. |
| 85 | NLSP, Standard Measures https://nlsp.nasa.gov/resources/standard-measures | HTTP 200; "NASA Life Sciences Portal (NLSP)". SPA. Las 27 medidas no se verificaron aquí | OK | Verificar la lista a mano en el navegador. |
| 86 | OSDR API de búsqueda `osdr.nasa.gov/osdr/data/search?term=...` | HTTP 200 para `term=Inspiration4&type=cgene&size=5` | OK | Ninguna. |
| 87 | OSDR Biodata API v2 `visualization.osdr.nasa.gov/biodata/api/v2/dataset/OSD-XXX/` | HTTP 200 para OSD-569 | OK | Ninguna. |
| 88 | OSDR descarga `osdr.nasa.gov/geode-py/ws/studies/OSD-XXX/download?...` | Plantilla con parámetros; no se probó con una URL concreta | OK (no probada) | Ninguna. Probar con un archivo concreto. |
| 89 | NTRS API de citas `ntrs.nasa.gov/api/citations/search` | HTTP 200, JSON con resultados (46 para "NASA-STD-3001") | OK | Ninguna. Es una propuesta del coordinador, no una fuente. |
| 90 | NASA Open APIs (incluye DONKI) https://api.nasa.gov | HTTP 200; "NASA Open APIs" | OK | Propuesta del coordinador, no una fuente. |

### B. Adendas y citas dentro de FUENTES.md

| n° | referencia declarada | metadatos verificados | estado | corrección propuesta |
|---|---|---|---|---|
| ADD-09a | Krittanawong C, et al. (2022). Human Health during Space Travel. *Cells* 12(1):40. doi:10.3390/cells12010040 | Crossref: 17 autores ✓ (primer autor Krittanawong), Cells 12(1):40, 2022-12-22. PMC9818606 ✓ | OK | Ninguna (ver referencia del informe R3). |
| ADD-09b | Jacobs et al. (2026). Astronauts of the US NASA: cohort profile. *BMJ Open*. doi:10.1136/bmjopen-2025-112490 | Crossref: título completo "Astronauts of the US National Aeronautics and Space Administration (NASA): cohort profile"; 5 autores; BMJ Open 16(6), e112490; en línea 2026-06-18. PMC13289012 ✓ | CORREGIR | Título completo (FUENTES lo abrevia "US NASA"). Añadir vol. 16(6) y e112490. |
| ADD-10 | Levine ME, et al. (2018). An epigenetic biomarker of aging for lifespan and healthspan. *Aging* 10(4):573–591. doi:10.18632/aging.101414 | Crossref: 18 autores, Aging 10(4), 573–591, 2018-04-18. PMC5940111 y PMID 29676998 (mismo artículo) | OK | Ninguna. |
| ADD-11a | Overbey EG, et al. (2024). "The Space Omics and Medical Atlas (SOMA)… " *Nature*. doi:10.1038/s41586-024-07639-y | Crossref: "The Space Omics and Medical Atlas (SOMA) and international astronaut biobank", Nature 632(8027), 1145–1154, 2024-06-11; 109 autores. PMC11357981 ✓ | CORREGIR | Título completo y volumen/páginas. Ver referencia R1. |
| ADD-11b | PhysioNet PRCP. doi:10.13026/C2PC7R | DataCite: "Physiologic Response to Changes in Posture", Heldt, T., PhysioNet, 2016, v1.0.0 (physionet.org/content/prcp/1.0.0) | OK | Añadir el título y la versión. |
| ADD-11c | PhysioNet cardioresp-response-orthostat. doi:10.13026/73w7-x881 | DataCite: "Two-tiered response of cardiorespiratory-cerebrovascular networks to orthostatic challenge", Eke, A., Mukli, P., Stylianou, O., Hartmann, A., PhysioNet, 2021, v1.0 | OK | Añadir el título. La licencia "PhysioNet Health Data License 1.5.0" de 11 no está en DataCite; no confirmada. |
| ADD-13 | Hardy JG, Theriot CA, Oswald T, Clément G. (2025). *npj Microgravity*. doi:10.1038/s41526-025-00532-6 · PMID 41224762 | Crossref: título ✓, 4 autores ✓, npj Microgravity 11, art. 78, 2025-11-12. PMC12612093 y PMID 41224762 ✓ (Europe PMC) | OK | Añadir "11, Article 78". Ver R2. |
| ADD-14a | NazS2. Astronaut-health-monitoring-system (GitHub). https://github.com/NazS2/Astronaut-health-monitoring-system | GitHub: 403 por el proxy (no habilitado en la sesión) | NO RESUELVE | Verificar a mano. Licencia no verificada. |
| ADD-14b | NASA Space Apps Challenge 2014. Astronaut Health Monitoring System. https://2014.spaceappschallenge.org/project/astronaut-health-monitoring-system/ | HTTP 200; "Astronaut Health Monitoring System \| Space Apps Challenge" | OK | La licencia AFL-3.0 indicada no se revisó. |

### C. Referencias del informe (solicitud)

| n° | referencia declarada | metadatos verificados | estado | corrección propuesta |
|---|---|---|---|---|
| R1 | Overbey 2024, *Nature*, doi:10.1038/s41586-024-07639-y | Crossref: "The Space Omics and Medical Atlas (SOMA) and international astronaut biobank", Nature 632(8027):1145–1154, 2024-06-11; 109 autores (Overbey EG primero). PMC11357981 ✓ | OK | Ver APA abajo (versión abreviada por tener más de 20 autores). |
| R2 | Hardy 2025, *npj Microgravity*, doi:10.1038/s41526-025-00532-6 | Crossref: título ✓, Hardy JG, Theriot CA, Oswald T, Clément G; vol. 11, art. 78; 2025-11-12. PMC12612093 y PMID 41224762 ✓ | OK | Añadir "11, Article 78". |
| R3 | Krittanawong 2022, *Cells*, doi:10.3390/cells12010040 | Crossref: título ✓, 17 autores, Cells 12(1):40, 2022-12-22 | OK | Ninguna. |
| R4 | Jacobs 2026, *BMJ Open*, doi:10.1136/bmjopen-2025-112490 | Crossref: título completo ✓, 5 autores ✓, BMJ Open 16(6), e112490, 2026-06 | CORREGIR | Título completo en la cita (ver ADD-09b). |
| R5 | Barger 2014, *Lancet Neurol*, doi:10.1016/S1474-4422(14)70122-X | Crossref ✓ (ver 41) | OK | Ninguna. |
| R6 | Stavnichuk 2020, *npj Microgravity*, doi:10.1038/s41526-020-0103-2 | Crossref ✓ (ver 42) | OK | Ninguna. |
| R7 | Macias 2020, *JAMA Ophthalmol*, doi:10.1001/jamaophthalmol.2020.0673 | Crossref ✓ (ver 44) | OK | Ninguna. |
| R8 | Cree 2010, *Metabolism*, doi:10.1016/j.metabol.2009.09.014 | Crossref: 2010, vol. 59(5), 703–710 ✓ | CORREGIR | El informe usa 2010 (correcto). Las notas de 00 y 02 dicen 2009. Unificar en 2010. |
| R9 | Levine 2018, *Aging*, doi:10.18632/aging.101414 | Crossref ✓ (ver ADD-10) | OK | Ninguna. |
| R10 | Kodama 2009, *JAMA*, doi:10.1001/jama.2009.681 | Crossref: 2009-05-20, JAMA 301(19), **2024** (pág. inicial; faltan páginas); **1 autor** (metadatos incompletos). PubMed (PMID 19454641): título con subtítulo "A Meta-analysis"; 12 autores: Kodama S, Saito K, Tanaka S, Maki M, Yachi Y, Asumi M, Sugawara A, Totsuka K, Shimano H, Ohashi Y, Yamada N, Sone H; JAMA 301(19):2024–2035 | CORREGIR | Completar autores, páginas 2024–2035 y subtítulo. Ver APA abajo. |
| R11 | Lloyd-Jones 2022, *Circulation*, doi:10.1161/CIR.0000000000001078 | Crossref: "Life's Essential 8: Updating and Enhancing the American Heart Association's Construct of Cardiovascular Health: A Presidential Advisory From the American Heart Association", Circulation 146(5), 2022-08-02, 12+ autores (Lloyd-Jones DM primero). Páginas no devueltas. Se cree e18–e43 (no confirmado: Europe PMC y PubMed caídos) | OK (páginas no confirmadas) | Añadir "146(5), e18–e43" cuando se confirme en PubMed. Ver APA abajo. |
| R12 | Windred 2024, *SLEEP*, doi:10.1093/sleep/zsad253 | Crossref: "Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study"; SLEEP 47(1), art. zsad253; en línea 2023-09-21; impresa 2024-01-11; 7 autores (Windred DP primero) | OK | Usar año 2024 (impreso) y vol. 47(1). El texto de 10 es correcto. |
| R13 | Searle 2008, *BMC Geriatrics* 8:24, doi:10.1186/1471-2318-8-24 | Crossref: "A standard procedure for creating a frailty index", BMC Geriatr 8(24), 2008-09-30; 5 autores (Searle SD primero) | OK | Ninguna. La revista es BMC Geriatrics (10 ya lo indica). |
| R14 | CMAJ 2016, 188(3):E53 (DOI y autores pendientes) | Crossref: DOI **10.1503/cmaj.150535**. "Resting heart rate and all-cause and cardiovascular mortality in the general population: a meta-analysis"; Zhang Dongfeng, Shen Xiaoli, Qi Xin; CMAJ 188(3):E53–E63; en línea 2015-11-23, impreso 2016-02-16 | CORREGIR | Completar la cita de 10 (solo dice "Metaanálisis CMAJ 2016"). Ver APA abajo. |
| R15 | Leong 2015, *Lancet*, PURE grip strength (DOI pendiente) | Crossref: DOI **10.1016/S0140-6736(14)62000-6**. "Prognostic value of grip strength: findings from the Prospective Urban Rural Epidemiology (PURE) study"; The Lancet 386(9990):266–273, 2015; 25 autores (Leong DP primero). 10 cita un resumen de Healio, no el artículo | CORREGIR | Completar DOI, autores, volumen y páginas. Ver APA abajo. |
| R16 | Jarczok 2022, *Neurosci Biobehav Rev* (RMSSD y mortalidad; DOI y título pendientes) | Crossref: DOI **10.1016/j.neubiorev.2022.104907**. "Heart rate variability in the prediction of mortality: A systematic review and meta-analysis of healthy and patient populations"; Neuroscience & Biobehavioral Reviews 143, art. 104907, 2022-12; 7 autores (Jarczok MN primero). El título de 10 ("RMSSD and mortality") no existe. No se revisó si las cifras de 10 (HR 1,56 para RMSSD) están en el resumen | CORREGIR | Completar título, DOI y autores. Ver APA abajo. Revisar la cifra 1,56 contra el resumen antes de usarla. |
| R17 | PhysioNet 10.13026/rees-1092 (BIDSleep) | DataCite ✓ (ver 76) | OK | Añadir título completo del dataset. |
| R18 | PhysioNet 10.13026/C2PC7R (PRCP) | DataCite: "Physiologic Response to Changes in Posture", Heldt T, 2016; doi.org → physionet.org/content/prcp/1.0.0 | OK | Ninguna. |
| R19 | PhysioNet 10.13026/73w7-x881 | DataCite: "Two-tiered response of cardiorespiratory-cerebrovascular networks to orthostatic challenge", 2021; doi.org → physionet.org/content/cardioresp-response-orthostat/1.0 | OK | Ninguna. |
| R20 | OSD-575 (Inspiration4 CMP y paneles séricos) | API OSDR: "SpaceX Inspiration4 Blood Serum Metabolic Panel and Immune/Cardiac Cytokine Arrays (Comprehensive Metabolic Panel and Multiplex)"; página HTTP 200 (SPA) | OK | Ninguna. |
| R21 | OSD-569 (hemograma) | Ver fuente 61 | OK | Ninguna. |

### D. Citas mencionadas sin número en FUENTES.md (sin verificar en los archivos)

| n° | referencia declarada | metadatos verificados | estado | corrección propuesta |
|---|---|---|---|---|
| D1 | Lee, S. M. C., et al. (2020), *npj Microgravity*. Citada en la solicitud original y en 06 | Búsqueda en Crossref sin coincidencia | NO RESUELVE | No citar hasta identificar el artículo. Sustituye a Macias 2020 (según 02). |
| D2 | Basner et al., batería Cognition (Standard Measures) | No verificada | NO RESUELVE | Verificar en NLSP (fuente 85) o eliminar. |
| D3 | LeBlanc et al. y Antonutto et al. (dentro de Comfort 2021) | No verificadas | NO RESUELVE | No citar sin leer Comfort 2021. |
| D4 | Dinges et al. y Barger et al. (dentro de `sleep.pdf`) | El PDF contiene las referencias; no se verificaron las entradas | NO RESUELVE | Verificar en el PDF `sleep.pdf` (fuente 17). |
| D5 | Rangos de referencia del hemograma, Quest Diagnostics | Sin documento | NO RESUELVE | Obtener el documento o citar la hoja ISA del OSD-569. |
| D6 | NASA-STD-3001 (requisitos de CO₂ y temperatura de cabina). **Cita incompleta** | NTRS 20250004555: "NASA-STD-3001 Volume 2, Revision E, NASA Spaceflight Human-System Standard Volume 2: Human Factors, Habitability, and Environmental Health" (creado 2025-05-05). El resumen no menciona CO₂ ni temperatura; no se verificaron los valores | CORREGIR | Completar con la referencia NTRS. Año 2025 (fecha de registro en NTRS). Ver APA abajo. |

---

## Lista APA corregida (solo referencias con correcciones)

Formato APA 7 (abreviado cuando hay más de 20 autores). Los campos no verificados se indican.

- Collet, G., Mairesse, O., McDonald-Nethercott, E., Ducrot, Y. M., Meeusen, R., & Pattyn, N. (2019). *Sleep during an Antarctic overwintering: Comparing an altitude base and a coastal station* [Poster]. Figshare. https://doi.org/10.6084/m9.figshare.10281224.v1

- Dunn Rosenberg, J., Jannasch, A., Binsted, K., & Landry, S. (2022). Biobehavioral and psychosocial stress changes during three 8–12 month spaceflight analog missions with Mars-like conditions of isolation and confinement. *Frontiers in Physiology, 13*, Article 898841. https://doi.org/10.3389/fphys.2022.898841

- Hardy, J. G., Theriot, C. A., Oswald, T., & Clément, G. (2025). Spaceflight Standard Measures is a multidisciplinary study that systematically monitors risks to astronaut health and performance. *npj Microgravity, 11*, Article 78. https://doi.org/10.1038/s41526-025-00532-6

- Jacobs, S., Charvat, J., Reitzel, R., Wear, M., & Van Baalen, M. (2026). Astronauts of the US National Aeronautics and Space Administration (NASA): Cohort profile. *BMJ Open, 16*(6), e112490. https://doi.org/10.1136/bmjopen-2025-112490

- Jarczok, M. N., Weimer, K., Braun, C., Williams, D. P., Thayer, J. F., Gündel, H. O., & Balint, E. M. (2022). Heart rate variability in the prediction of mortality: A systematic review and meta-analysis of healthy and patient populations. *Neuroscience & Biobehavioral Reviews, 143*, Article 104907. https://doi.org/10.1016/j.neubiorev.2022.104907

- Kodama, S., Saito, K., Tanaka, S., Maki, M., Yachi, Y., Asumi, M., Sugawara, A., Totsuka, K., Shimano, H., Ohashi, Y., Yamada, N., & Sone, H. (2009). Cardiorespiratory fitness as a quantitative predictor of all-cause mortality and cardiovascular events in healthy men and women: A meta-analysis. *JAMA, 301*(19), 2024–2035. https://doi.org/10.1001/jama.2009.681

- Leong, D. P., Teo, K. K., Rangarajan, S., Lopez-Jaramillo, P., Avezum, A., Orlandini, A., Seron, P., Ahmed, S. H., Rosengren, A., Kelishadi, R., Rahman, O., Swaminathan, S., Iqbal, R., Gupta, R., Lear, S. A., Oguz, A., Yusoff, K., Zatonska, K., Chifamba, J., Igumbor, E., Mohan, V., Anjana, R. M., Gu, H., Li, W., & Yusuf, S. (2015). Prognostic value of grip strength: Findings from the Prospective Urban Rural Epidemiology (PURE) study. *The Lancet, 386*(9990), 266–273. https://doi.org/10.1016/S0140-6736(14)62000-6

- Lloyd-Jones, D. M., Allen, N. B., Anderson, C. A. M., Black, T., Brewer, L. C., Foraker, R. E., Grandner, M. A., Lavretsky, H., Perak, A. M., Sharma, G., Rosamond, W., & American Heart Association. (2022). Life's Essential 8: Updating and enhancing the American Heart Association's construct of cardiovascular health: A presidential advisory from the American Heart Association. *Circulation, 146*(5), e18–e43. https://doi.org/10.1161/CIR.0000000000001078 [páginas no confirmadas]

- Mendt, S., Brauns, K., Friedl-Werner, A., Belavy, D. L., Steinach, M., Schlabs, T., Werner, A., Gunga, H.-C., & Stahn, A. C. (2021). Long-term bed rest delays the circadian phase of core body temperature. *Frontiers in Physiology, 12*, Article 658707. https://doi.org/10.3389/fphys.2021.658707

- NASA. (2023). *Evidence report: Risk of inadequate human-system integration architecture* [Informe PDF]. NASA Human Research Program. https://humanresearchroadmap.nasa.gov/evidence/reports/Risk%20of%20Inadequate%20HSIA%20approved%20FINAL_%206-13-2023.pdf

- NASA. (2023). *Evidence report: Risk of reduced crew health and performance due to decompression sickness and hypoxia* [Informe PDF]. NASA Human Research Program. Aprobado el 31 de octubre de 2023. https://humanresearchroadmap.nasa.gov/evidence/reports/Evidence%20Report%20Hypoxia%20and%20DCS_FINAL_1-8-2024.pdf

- NASA. (s. f.). *Evidence report: Risk of cardiovascular disease and other degenerative tissue effects from radiation exposure* [Informe PDF]. NASA Human Research Program. https://humanresearchroadmap.nasa.gov/evidence/reports/Degen.pdf

- NASA. (2025). *NASA-STD-3001, Volume 2, Revision E: NASA spaceflight human-system standard, Volume 2: Human factors, habitability, and environmental health* [NTRS 20250004555]. https://ntrs.nasa.gov/citations/20250004555 [año según registro NTRS; valores de CO₂ y temperatura no verificados]

- NASA Open Science Data Repository. (s. f.). *OSD-191: Temporal dynamics of the gut microbiota in people sharing a confined environment, a 520-day ground-based space simulation, MARS500* (GLDS-191) [Conjunto de datos]. https://osdr.nasa.gov/bio/repo/data/studies/OSD-191

- Overbey, E. G., Kim, J., Tierney, B. T., Park, J., Houerbi, N., Lucaci, A. G., … Meydan, C., & Mason, C. E. (2024). The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. *Nature, 632*(8027), 1145–1154. https://doi.org/10.1038/s41586-024-07639-y

- Sanders, L. M., Grigorev, K. A., Scott, R. T., Saravia-Butler, A. M., Polo, S. L., Gilbert, R., Overbey, E. G., Kim, J., Mason, C. E., & Costes, S. V. (2024). Inspiration4 data access through the NASA Open Science Data Repository. *npj Microgravity, 10*, Article 56. https://doi.org/10.1038/s41526-024-00393-5

- Turroni, S., Rampelli, S., Biagi, E., Consolandi, C., Severgnini, M., Peano, C., Quercia, S., Soverini, M., Carbonero, F. G., Bianconi, G., Rettberg, P., Canganella, F., Brigidi, P., & Candela, M. (2017). Temporal dynamics of the gut microbiota in people sharing a confined environment, a 520-day ground-based space simulation, MARS500. *Microbiome, 5*, Article 39. https://doi.org/10.1186/s40168-017-0256-8

- Windred, D. P., Burns, A. C., Lane, J. M., Saxena, R., Rutter, M. K., Cain, S. W., et al. (2024). Sleep regularity is a stronger predictor of mortality risk than sleep duration: A prospective cohort study. *SLEEP, 47*(1), zsad253. https://doi.org/10.1093/sleep/zsad253 [año impreso 2024; epub 2023-09-21]

- Zhang, D., Shen, X., & Qi, X. (2016). Resting heart rate and all-cause and cardiovascular mortality in the general population: A meta-analysis. *Canadian Medical Association Journal, 188*(3), E53–E63. https://doi.org/10.1503/cmaj.150535

---

## Notas para el coordinador

- Los datos de los archivos 00 a 14 no se revisaron más allá de las citas bibliográficas. Las cifras (p. ej. "−0,8 %/mes", "HR 1,56", "+18 % coroides") no se verificaron contra el texto de cada artículo, salvo lo indicado en la tabla.
- Pendiente de nueva consulta (PubMed/Europe PMC caídos): páginas de Lloyd-Jones 2022; PMID de Comfort 2021, Fu 2019 y Hardy 2025; cifra 1,56 de Jarczok 2022 en el resumen.
- Ninguna referencia parece inventada en el sentido de no existir: las no resueltas (55, 56, 57, D1) no tienen DOI ni registro, por lo que deben retirarse hasta que alguien aporte el documento.
