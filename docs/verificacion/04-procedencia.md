# Verificación de procedencia: datos NASA (NLSP y OSDR)

- Fecha de verificación: 2026-11-05. Auditor: agente independiente de procedencia.
- Alcance: catálogo UTMB de NLSP (48 experimentos), tres GUID de misión, seis DOI nombrados, re-descarga de siete ZIP de NLSP, OSD-569 y OSD-575 de OSDR, y condiciones de licencia y uso de ambas fuentes.
- Fuentes en vivo: `https://nlsp.nasa.gov/api/v1/data/experiments/<GUID>/full`, `.../missions/<GUID>/full`, `https://doi.org/<DOI>`, páginas `nlsp.nasa.gov` y `osdr.nasa.gov` (renderizadas con Playwright), `https://osdr.nasa.gov/osdr/data/osd/files/<n>`, `https://visualization.osdr.nasa.gov/biodata/api/v2/dataset/OSD-<n>/`, y descargas de `https://osdr.nasa.gov/geode-py/ws/studies/...`.
- Ningún archivo del proyecto se modificó. Las descargas, extracciones y capturas están en `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/`. Los ZIP y archivos descargados se trataron como datos no confiables.

## 1. Resumen

- **Experimentos del catálogo:** 48 de 48 existen en vivo. Los títulos coinciden. Los 48 DOI vivos resuelven al GUID del experimento (el catálogo local no tiene campo DOI).
- **Flag `public`:** 30 experimentos con `public: true`. Según `archive_status` en vivo, 28 son "All datasets are publicly available" y 2 son sólo parcialmente públicos (el resto requiere solicitud). Los otros 18 no son públicos y el catálogo lo refleja bien.
- **Misiones:** 24 de 48 fichas vivas incluyen "UTMB Campaign 5", que el catálogo local no tiene. Es la única discrepancia de campo en el catálogo.
- **GUID de misión** (Campaign 11, 1 y 3): correctos, con nombre y año. Los JSON locales tienen el mismo registro que la API viva (3 de 3).
- **Re-descargas NLSP:** tamaño, lista de archivos, md5 de cada archivo extraído y manifiestos `.md5sum` coinciden en los siete ZIP. Los md5 de los ZIP en sí difieren, pero sólo por marcas de tiempo internas (CRC y contenido idénticos).
- **OSDR:** OSD-569 y OSD-575 corresponden a Inspiration4 con organismo Homo sapiens. Los archivos locales son idénticos byte a byte a los vivos (aunque OSD-575 usa nombres distintos).
- **Licencia:** el ISA `i_Investigation.txt` no contiene ningún campo de licencia ni de cita. La licencia está en la página de OSDR ("License: CC0-1.0"). Las notas del proyecto esperaban encontrarla en el ISA.
- **Licencia NLSP:** ninguna página de NLSP declara licencia. Sólo consta "All rights reserved" en el pie. NO VERIFICABLE como dato abierto con licencia.
- **Discrepancias totales:** 25 experimentos con alguna discrepancia de campo (24 de misiones, 2 de público parcial, con solapamiento en uno de ellos), más las discrepancias de licencia y de notas del proyecto listadas en la sección 8.

## 2. Tabla principal

| elemento | local | fuente en vivo | estado | nota |
|---|---|---|---|---|
| Experimentos del catálogo UTMB | 48 (`nlsp-raw/utmb-experimentos.json`) | 48 fichas `experiments/<GUID>/full`, HTTP 200 | OK | Mismo GUID en todos los registros |
| Títulos de experimento | 48 | `experiment_title` en las 48 fichas | OK | Coinciden exactamente, incluidos dobles espacios |
| Flag `public` = true | 30 | 30 con `archive_status` que contiene "publicly available" | DISCREPANCIA (matiz) | Sólo 28 dicen "All datasets are publicly available". Las otras 2 (`950b2ce4…`, `26a8b51f…`) dicen "Privacy-protected datasets are available via data request. Remaining datasets are publicly available." |
| Flag `public` = false | 18 | 18 con datos privados, sin datos o en otro repositorio (13 C, 4 D, 1 E) | OK | Coherente |
| Misiones UTMB por experimento | 48 listas de misiones | 48 fichas vivas | DISCREPANCIA | 24 fichas vivas incluyen "UTMB Campaign 5" que falta en el catálogo; ninguna otra diferencia |
| DOI de los 48 experimentos | No está en el catálogo | `__doi` en 48/48; `doi.org` resuelve al GUID correcto en 48/48 | OK | Ver sección 3 |
| Seis DOI nombrados | No aplica | 6/6 resuelven al GUID esperado (sección 4) | OK | Incluye `wjw1-ta27`, `rank-k271`, `gz1q-a824`, `kw2c-zj80`, `4dzb-2267`, `w056-8t76` |
| Campaign 11 `8e583564-d124-58ce-b44a-a16bb5b5d981` | `mission-8e583564….json` = `utmb-c11.json` (md5 idéntico) | `mission_id` "UTMB Campaign 11", año 2011 | OK | Coincide |
| Campaign 1 `6eaf1654-72d4-5d71-a9dd-a02e674c6473` | `mission-6eaf1654….json` | `mission_id` "UTMB Campaign 1", año 2004 | OK | Coincide |
| Campaign 3 `593a6726-8650-551a-8d67-0f03468de92f` | `mission-593a6726….json` | `mission_id` "UTMB Campaign 3", año 2005 | OK | Coincide |
| Re-descarga de 7 ZIP NLSP (6 pedidos + BRSMCF) | ZIP en `nlsp-raw/downloads/` | ZIP nuevos vía Playwright, mismos bytes | OK | Tamaños iguales; contenido, CRC y manifiestos idénticos (sección 5) |
| Etiquetas de dataset del catálogo `utmb-datasets.jsonl` | 79 etiquetas, 11 experimentos | 79/79 presentes en la ficha viva | OK | Las etiquetas no se han renombrado ni retirado |
| OSD-569: misión y organismo | `osd-569-meta.json` | API: Inspiration4 (9/16/21–9/18/21), Homo sapiens | OK | Coincide con la página y el ISA |
| OSD-575: misión y organismo | ISA 575: `Comment[Mission Name]` = SpaceX Inspiration4 (`i_Investigation.txt`); `Homo sapiens` en 28 líneas de `s_OSD-575.txt` | API: Inspiration4, Homo sapiens | OK | Coincide. El catálogo local no tiene metadatos de misión de OSD-575 fuera del ISA |
| OSD-569: archivos locales (3) | `osd-569/` | Listado: 11 archivos. Los 3 locales tienen mismo nombre, tamaño y md5 | OK | Ver sección 6 |
| OSD-575: archivos locales (2) | `osd-575/CMP.csv`, `osd-575/cardio_eve.csv` | Listado: 9 archivos. Mismo tamaño y md5 que `LSDS-8_Comprehensive_Metabolic_Panel_CMP.upload_SUBMITTED.csv` y `LSDS-8_Multiplex_serum.cardiovascular.EvePanel_SUBMITTED.csv` | OK | Nombres locales distintos (renombrados). Mismo contenido |
| OSD-575: ZIP de metadatos ISA | No hay copia local | Listado 71 702 bytes; descarga 71 702 bytes | NO VERIFICABLE | No estaba en el proyecto; se descargó y se analizó |
| Licencia de datos OSD-569 y OSD-575 | ISA `i_Investigation.txt`: sin campo de licencia (búsqueda en los dos ZIP) | Páginas de estudio: "License: CC0-1.0" (ambas) | DISCREPANCIA frente a notas del proyecto | `00-RESUMEN.md` y `03-osdr-datos-humanos.md` §4 esperaban la licencia en el ISA. Ver sección 7 |
| Licencia de datos NLSP | Ninguna en el proyecto | Ninguna licencia en fichas, guía ni pie. Pie: "© 2026 NASA Life Sciences Portal. All rights reserved." | NO VERIFICABLE | La sección "Open-Access Data" existe. El texto de licencia no. Ver sección 7 |
| Acceso sin inicio de sesión (NLSP) | Nota de `08-nlsp-utmb-datos-abiertos.md` | Descargas OK en contexto de navegador sin sesión | OK | Confirma la afirmación de sin login |

## 3. Detalle por experimento (48 fichas NLSP)

Códigos de `archive_status` en vivo: **A** = "All datasets are publicly available" (28); **B** = parcial, datasets con privacidad vía solicitud y el resto público (2); **C** = "All datasets are privacy-protected. Data is available via data request." (13); **D** = "No data from this study was submitted to LSDA" (4); **E** = "held by another repository" (1).

| elemento | local | fuente en vivo | estado | nota |
|---|---|---|---|---|
| Aerobic Capacity (Flight Analog) (`07f12dd0-6725-582c-a4d2-618ed8b8c452`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/w056-8t76`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures:  Acetaminophen Test (`7ab565bb-f9d6-510f-bd07-407caccaeb9f`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/0njm-h670`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures:  Actilight (`cd8a4a16-fcfd-5c32-a61f-22c590a10b35`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/v7n1-ht75`; misiones: C1, C3 | OK | Coincide |
| Bed Rest Standard Measures:  Performance Testing (`0efe87dd-d04a-5755-add7-860dc0f67e56`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/7081-d617`; misiones: C1, C3 | OK | Coincide |
| Bed Rest Standard Measures:  Urea Breath Test (`4b0bbf22-c9d7-51fa-9262-7328f3ad70df`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/2427-0p13`; misiones: C1, C3 | OK | Coincide |
| Bed Rest Standard Measures: Cardiovascular Function (`9af6f9ba-3730-54ab-a82a-1a32798667ae`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/kw2c-zj80`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Functional Mobility Test (`dcff3b64-7700-5441-b4c3-2af31b9bb7b0`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/ahtd-k915`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Functional Stretch Reflex (`99479246-dbfe-5e92-bb6b-8ff96457a0b5`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/mwn3-tw13`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: General Immunity (`e21cc209-b6c4-5b47-b33b-6e31f51b784f`) | public: true; misiones: C11, C3 | archive_status: A; DOI: `10.83263/75we-ch31`; misiones: C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Glucose Breath Test (`8aae3ece-7d06-5078-8b48-ec84eb633833`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/kr2r-gr18`; misiones: C1, C3 | OK | Coincide |
| Bed Rest Standard Measures: Hepatic and Renal Function (`f1a74e0f-dad5-5109-992c-7271f39da690`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/qmr9-ek59`; misiones: C1, C3 | OK | Coincide |
| Bed Rest Standard Measures: Lactulose Test (`5ff5f10d-fb82-5af3-b2eb-ffd60cad1381`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/7ng5-5112`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Latent Virus Reactivation (`28d79ca9-2cb0-5fbe-a4ac-021be1cd2df8`) | public: true; misiones: C11, C3 | archive_status: A; DOI: `10.83263/zakw-zt39`; misiones: C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Plasma Volume (`adf51ad3-4370-545b-8d48-fbd33d73e796`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/4dzb-2267`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Reactive Hyperemia and Vasodilation (Vascular Function) (`adc0daf5-c8ac-5418-8fc7-d11115617671`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/pz53-yg20`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Tendon Reflex (`a3090eb9-34bd-5248-8549-4c8fbde4b76a`) | public: true; misiones: C11, C3 | archive_status: A; DOI: `10.83263/b0g4-j398`; misiones: C11, C3 | OK | Coincide |
| Bed Rest Standard Measures: Viral Specific Immunity (`82e288d5-82d9-51a0-8e33-bc9bef232dfe`) | public: true; misiones: C11, C3 | archive_status: A; DOI: `10.83263/m3hm-nj40`; misiones: C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bone Densitometry Assessment (Flight Analog) (`4469ebdc-0a65-55e8-bbff-3cf6b044c4c6`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/7myc-5j86`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Case Report Form (`eeb9bd34-bdd4-5115-b139-adf2c9927962`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/wjw1-ta27`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Clinical Laboratory Assessment (Flight Analog) (`2858df7a-0072-5cb4-ae70-cf73997832a8`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/rank-k271`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Clinical Nutritional Assessment (Flight Analog) (`72616c68-3046-5d36-8f1d-a26d856107ff`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/r8re-xs50`; misiones: C1, C3 | OK | Coincide |
| Functional Fitness Assessment (Flight Analog) (`b70ca856-2dc3-5c50-b690-6ff45be3a126`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/a4w0-1b14`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Functional Neurological Assessment: Computerized Dynamic Posturography (Flight Analog) (`df780931-6b24-5a6e-b9b1-ab6fd5efe8b1`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/yczt-jj10`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Gender Differences in Bedrest: Autonomic and Neuroendocrine Changes and Vascular Responses in Lower and Upper Extremities (`707feb44-29c9-50b1-863a-8348c61f0359`) | public: true; misiones: C3 | archive_status: A; DOI: `10.83263/wtxf-sf78`; misiones: C3 | OK | Coincide |
| Human Cerebral Cortex Plasticity in Response to Long-term Bedrest as an Analog to Microgravity (`950b2ce4-5f5b-5f00-a870-1f24e2897771`) | public: true; misiones: C3 | archive_status: B; DOI: `10.83263/xm32-7921`; misiones: C3 | DISCREPANCIA | public=true, pero la ficha dice que 2 grupos de datasets son solo bajo solicitud |
| Isokinetic Muscle Function (Flight Analog) (`f97392b8-b9dd-5bae-af9e-dd76a33bf049`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/bk5h-r757`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Neurocognitive Assessment (WinSCAT) (Cognitive Assessment Tool for Windows) (Flight Analog) (`80ee3231-7c42-5be4-b6c2-b8c788feeb50`) | public: true; misiones: C1, C3 | archive_status: A; DOI: `10.83263/sbne-th55`; misiones: C1, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Neuroendocrine and Cardiovascular Response to Tilt (Flight Analog) (`09bd2406-b323-5f7c-b0ac-d4585f0015ff`) | public: true; misiones: C1, C11, C3 | archive_status: A; DOI: `10.83263/gz1q-a824`; misiones: C1, C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Peripheral Quantitative Computed Tomography (pQCT) (`abf33b2e-3085-5c85-ad58-487ccbeaa762`) | public: true; misiones: C3 | archive_status: A; DOI: `10.83263/e30m-bb67`; misiones: C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Retention of Skeletal, Musculature, and Postural Status with a Non-Invasive, Extremely Low-Level Mechanical Signal: A Ground-Based Evaluation of Efficacy (`26a8b51f-df92-5a52-9fc0-b8b77067246a`) | public: true; misiones: C3 | archive_status: B; DOI: `10.83263/dk30-xz29`; misiones: C3, C5 | DISCREPANCIA | public=true, pero la ficha dice que 2 grupos de datasets son solo bajo solicitud; misiones: falta en local C5 |
| AD ASTRA: Automated Detection of Attitudes and States through Transaction Recordings Analysis (`f48b517c-44f6-5ad7-9ac9-6750450698b5`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/rm36-3p76`; misiones: C11 | OK | Coincide |
| Alterations of Steroidogenesis by Exercise Countermeasures during Bed Rest (`17dcac68-0b7c-5a8d-bafb-dc988c314b61`) | public: false; misiones: C1 | archive_status: D; DOI: `10.83263/cjjk-9k20`; misiones: C1 | OK | Coincide |
| Bed Rest Standard Measures: Functional Neurological Status Exam (`4baf392a-f08e-5fc3-896a-2fc7d94c68ab`) | public: false; misiones: C1 | archive_status: C; DOI: `10.83263/2p74-bd95`; misiones: C1 | OK | Coincide |
| Bed Rest Standard Measures: Intelligent Dual-Energy X-ray Absorptiometry (`caa3b09f-28b8-5c50-b0af-5f6540147f24`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/mdba-ek79`; misiones: C11 | OK | Coincide |
| Bed Rest Standard Measures: Physiological Stress Measures (`c961d7f4-bf8f-502c-97d7-ef7fed16218a`) | public: false; misiones: C3 | archive_status: C; DOI: `10.83263/vdrb-6710`; misiones: C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Psychological Stress Measures (`1fa64cbd-ae4a-5368-85b0-f9df9fa26937`) | public: false; misiones: C3 | archive_status: C; DOI: `10.83263/mr93-hy04`; misiones: C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Bed Rest Standard Measures: Vertical Jump (`ec4d5d93-3c06-5468-ba11-36a6000a6b01`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/fkz6-s185`; misiones: C11 | OK | Coincide |
| Bed Rest and Immunity (`943468a7-3de2-5b6f-b777-69ef96c1952b`) | public: false; misiones: C1 | archive_status: D; DOI: `10.83263/qrev-5a41`; misiones: C1 | OK | Coincide |
| Bed Rest as a Spaceflight Analog to Study Neurocognitive Changes: Extent, Longevity, and Neural Bases (`e76e94d1-500e-56e2-88e6-36ec83bd0239`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/qs2r-t591`; misiones: C11 | OK | Coincide |
| Combined Effects of Nutritional and Exercise Countermeasures (`5a13785c-1a9f-5a3f-b09d-ca2d6004bf1c`) | public: false; misiones: C3 | archive_status: D; DOI: `10.83263/b1ja-6377`; misiones: C3 | OK | Coincide |
| Effects of Retronasal Smelling, Variety and Choice on Appetite and Satiety (`a9f342db-fd12-52b0-8e17-0bf264f392f5`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/ee8v-7f24`; misiones: C11 | OK | Coincide |
| Integrated Resistance and Aerobic Exercise Training With Small Compact Exercise Equipment (`bb0a11e1-ecc4-5b2c-8f0f-cf7da73e159c`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/j9rp-4981`; misiones: C11 | OK | Coincide |
| Non-Invasive Near Infrared Spectroscopy (`2cf34b75-eb36-5661-9dd7-d65d26dc7320`) | public: false; misiones: C3 | archive_status: E; DOI: `10.83263/9nz3-tr43`; misiones: C3 | OK | Coincide |
| Physiological Factors Contributing to Post Bed Rest Changes in Functional Performance (Functional Task Test) (`ab997b6f-ef4e-5316-9ac2-9badfca1ddf1`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/n55t-gt10`; misiones: C11 | OK | Coincide |
| Quantitative Computerized Tomography (`185ce6b8-ca27-581f-a908-3678065f3798`) | public: false; misiones: C11, C3 | archive_status: C; DOI: `10.83263/4bs4-7j94`; misiones: C11, C3, C5 | DISCREPANCIA | misiones: falta en local C5 |
| Surveillance of Ocular Parameters and Visual Function in Bed Rest Subjects (`71c993e7-1b34-5ceb-8abf-b4ec8450de8f`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/c1tp-zf15`; misiones: C11 | OK | Coincide |
| Testosterone Supplementation as a Countermeasure against Musculoskeletal Losses during Space Exploration (`7b314f94-efbd-565d-bea2-9403e48b997f`) | public: false; misiones: C11 | archive_status: C; DOI: `10.83263/hk52-gc75`; misiones: C11 | OK | Coincide |
| Ultrasonic Bone Stimulation: Countermeasure to Orthostatic Intolerance (`c8b8e8f7-0ebe-58f0-81f7-12648a716a12`) | public: false; misiones: C3 | archive_status: D; DOI: `10.83263/w1bp-jx22`; misiones: C3 | OK | Coincide |

Texto literal de `archive_status` de los dos casos parciales:

- `950b2ce4-5f5b-5f00-a870-1f24e2897771` (Human Cerebral Cortex Plasticity in Response to Long-term Bedrest as an Analog to Microgravity): "Data preservation is complete. Privacy-protected datasets are available via data request. Remaining datasets are publicly available."
- `26a8b51f-df92-5a52-9fc0-b8b77067246a` (Retention of Skeletal, Musculature, and Postural Status with a Non-Invasive, Extremely Low-Level Mechanical Signal: A Ground-Based Evaluation of Efficacy): "Data preservation is complete. Privacy-protected datasets are available via data request. Remaining datasets are publicly available."

## 4. Seis DOI nombrados (resolución vía doi.org)

| elemento | local | fuente en vivo | estado | nota |
|---|---|---|---|---|
| Case Report Form | DOI nombrado; GUID esperado `eeb9bd34-bdd4-5115-b139-adf2c9927962` | https://doi.org/10.83263/wjw1-ta27 redirige a `https://nlsp.nasa.gov/explore/data/details/eeb9bd34-bdd4-5115-b139-adf2c9927962?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |
| Clinical Laboratory Assessment (Flight Analog) | DOI nombrado; GUID esperado `2858df7a-0072-5cb4-ae70-cf73997832a8` | https://doi.org/10.83263/rank-k271 redirige a `https://nlsp.nasa.gov/explore/data/details/2858df7a-0072-5cb4-ae70-cf73997832a8?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |
| Neuroendocrine and Cardiovascular Response to Tilt (Flight Analog) | DOI nombrado; GUID esperado `09bd2406-b323-5f7c-b0ac-d4585f0015ff` | https://doi.org/10.83263/gz1q-a824 redirige a `https://nlsp.nasa.gov/explore/data/details/09bd2406-b323-5f7c-b0ac-d4585f0015ff?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |
| Bed Rest Standard Measures: Cardiovascular Function | DOI nombrado; GUID esperado `9af6f9ba-3730-54ab-a82a-1a32798667ae` | https://doi.org/10.83263/kw2c-zj80 redirige a `https://nlsp.nasa.gov/explore/data/details/9af6f9ba-3730-54ab-a82a-1a32798667ae?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |
| Bed Rest Standard Measures: Plasma Volume | DOI nombrado; GUID esperado `adf51ad3-4370-545b-8d48-fbd33d73e796` | https://doi.org/10.83263/4dzb-2267 redirige a `https://nlsp.nasa.gov/explore/data/details/adf51ad3-4370-545b-8d48-fbd33d73e796?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |
| Aerobic Capacity (Flight Analog) | DOI nombrado; GUID esperado `07f12dd0-6725-582c-a4d2-618ed8b8c452` | https://doi.org/10.83263/w056-8t76 redirige a `https://nlsp.nasa.gov/explore/data/details/07f12dd0-6725-582c-a4d2-618ed8b8c452?dataType=EXPERIMENTS` (HTTP 200) | OK | El DOI resuelve a la misma ficha que el `__doi` vivo |

## 5. Re-descargas NLSP: comparación de archivos

Método: página `https://nlsp.nasa.gov/explore/data/details/<GUID>?dataType=EXPERIMENTS` en Playwright (Chromium, contexto nuevo sin sesión), clic en el botón `aria-label` que contiene el nombre del dataset, `waitForEvent("download")`. Secuencial, con 2 s entre descargas. Cada ZIP se extrajo con verificación de rutas (sin `..` ni rutas absolutas) en un directorio nuevo. Se comparó cada archivo extraído con la copia local en `nlsp-raw/downloads/x/<dataset>/` y se verificó cada línea de los manifiestos `.md5sum` que trae el ZIP.

| dataset (GUID) | ZIP local (bytes) | ZIP nuevo (bytes) | md5 ZIP local / nuevo | archivos (local = nuevo) | md5 de archivos idénticos | manifiesto .md5sum | estado |
|---|---|---|---|---|---|---|---|
| CRF_CFT70_VITALS (`eeb9bd34-bdd4-5115-b139-adf2c9927962`) | 6244 | 6244 | `1df73c87c9803987e43dbc213ec4d2c2` / `00efc3162f48d02c5a58eff28bc19719` | 4 | 4 de 4 (sin diferencias) | 3/3 líneas OK, 0 malas, 0 ausentes | OK |
| MR010G_Campaign_3_Clinical_Laboratory_Assessment (`2858df7a-0072-5cb4-ae70-cf73997832a8`) | 156425 | 156425 | `a4b74cdf9d68a269dc4fbfce85c860ca` / `fc44d1168df46029d50b57d6f45dac92` | 40 | 40 de 40 (sin diferencias) | 39/39 líneas OK, 0 malas, 0 ausentes | OK |
| MR001G_Campaign_3_Tilt (`09bd2406-b323-5f7c-b0ac-d4585f0015ff`) | 76035 | 76035 | `58ba584f861ef3cbc3f166cf7ce9829e` / `e007e3859989d33046e07658ee5696c5` | 81 | 81 de 81 (sin diferencias) | 80/80 líneas OK, 0 malas, 0 ausentes | OK |
| BRSMACT_Campaign_1_Actigraphy (`cd8a4a16-fcfd-5c32-a61f-22c590a10b35`) | 6237 | 6237 | `33e5fe7ea6e6fc87a8e6f339dadaaa56` / `9c5f34ce60c1619968fd2a36057162cc` | 4 | 4 de 4 (sin diferencias) | 3/3 líneas OK, 0 malas, 0 ausentes | OK |
| MR085G_Campaign_3_WinSCAT (`80ee3231-7c42-5be4-b6c2-b8c788feeb50`) | 18965 | 18965 | `bb254eef7f4f756d5192ff8c8a8e48a1` / `11695087da3001ebc2330d5aa770c20f` | 27 | 27 de 27 (sin diferencias) | 26/26 líneas OK, 0 malas, 0 ausentes | OK |
| BRSMPV_Campaign_3_Plasma_Volume (`adf51ad3-4370-545b-8d48-fbd33d73e796`) | 18151 | 18151 | `50f77d9a615012d2f8b4f19c404b537e` / `7bd4c80c319fbd8a6feb03118d3f509a` | 29 | 29 de 29 (sin diferencias) | 28/28 líneas OK, 0 malas, 0 ausentes | OK |
| BRSMCF_CFT70 (ZIP local `BRSMCF_1793850934927.zip`) (`9af6f9ba-3730-54ab-a82a-1a32798667ae`) | 25690 | 25690 | `3db5f174b91aabbc52fbf10a652c7e3a` / `825e20c0b924bb39ac09bc04b7ddcbab` | 4 | 4 de 4 (contrastado con `downloads/brsmcf_cft70/`) | 3/3 líneas OK | OK |

Notas de la comparación:

- Los md5 de los ZIP en sí difieren en las siete descargas. Las entradas internas tienen fecha de descarga distinta. Los CRC y los md5 de los archivos internos coinciden en todos los casos.
- Los siete ZIP se extrajeron a un directorio nuevo y se verificaron. Ningún archivo fue ajeno al ZIP.
- Los 79 nombres de dataset del catálogo `utmb-datasets.jsonl` existen en las fichas vivas. Los datasets de los demás ZIP locales (CRF Campaign 1/3, MR035G, MR085G Campaign 1, MR001G Campaign 1, BRSMPV CFT70, CRF CFT70 SYMPTOMS) se verificaron sólo a nivel de manifiesto interno y de coincidencia con `x/`. No se re-descargaron.

## 6. OSDR: archivos y metadatos

### 6.1 Metadatos de estudio

| elemento | local | fuente en vivo | estado | nota |
|---|---|---|---|---|
| OSD-569 título | ISA `s_`/`i_` y `osd-569-meta.json`: "Whole Blood Measurements from the SpaceX Inspiration4 Mission (RNA-seq, epitranscriptome, WGS, clonal hematopoiesis, CBC)" | API y página: mismo título | OK |  |
| OSD-569 misión y organismo | Inspiration4; Homo sapiens | API: `mission` = SpaceX Inspiration4 (9/16/21–9/18/21); `organism` = Homo sapiens | OK |  |
| OSD-569 fecha pública | ISA: 14-May-2024 | API: 1715644800 = 2024-05-14T00:00:00Z; página: "Initial Release Date: 14-May-2024" | OK |  |
| OSD-569 DOI | ISA: 10.26030/e0rx-sh52 | Página y cita: 10.26030/e0rx-sh52 | OK |  |
| OSD-575 título | ISA: "SpaceX Inspiration4 Blood Serum Metabolic Panel and Immune/Cardiac Cytokine Arrays (Comprehensive Metabolic Panel and Multiplex)" | API y página: mismo título | OK |  |
| OSD-575 misión y organismo | Inspiration4; Homo sapiens | API: Inspiration4; Homo sapiens | OK |  |
| OSD-575 DOI | ISA: 10.26030/mc5d-p710 | Página y cita: 10.26030/mc5d-p710 | OK |  |
| OSD-569 y OSD-575 ALSDA IDs | OSD-569 = LSDS-7; OSD-575 = LSDS-8 | Página: "ALSDA ID: LSDS-7" / "LSDS-8" | OK |  |

### 6.2 Archivos

| archivo local | nombre y tamaño en vivo | md5 local | md5 descargado | estado | nota |
|---|---|---|---|---|---|
| `osd-569/LSDS-7_Complete_Blood_Count_CBC.upload_SUBMITTED.csv` | LSDS-7_Complete_Blood_Count_CBC.upload_SUBMITTED.csv, 26138 B | `4fa4c2196e0a0324ad84f9cda5e68647` | `4fa4c2196e0a0324ad84f9cda5e68647` | Byte-idéntico | Tamaño y md5 coinciden |
| `osd-569/LSDS-7_Complete_Blood_Count_CBC_TRANSFORMED.csv` | LSDS-7_Complete_Blood_Count_CBC_TRANSFORMED.csv, 9317 B | `06f3919e07b697119891ed0a777f8ee8` | `06f3919e07b697119891ed0a777f8ee8` | Byte-idéntico | Tamaño y md5 coinciden |
| `osd-569/OSD-569_metadata_OSD-569-ISA.zip` | OSD-569_metadata_OSD-569-ISA.zip, 123512 B | `b391305c6ea78a1d9dff78b6a73a5437` | `b391305c6ea78a1d9dff78b6a73a5437` | Byte-idéntico | Tamaño y md5 coinciden |
| `osd-575/CMP.csv` | LSDS-8_Comprehensive_Metabolic_Panel_CMP.upload_SUBMITTED.csv, 25275 B | `d65cf24ec5a382be5ac842c1782a8c75` | `d65cf24ec5a382be5ac842c1782a8c75` | Byte-idéntico (renombrado) | Tamaño y md5 coinciden |
| `osd-575/cardio_eve.csv` | LSDS-8_Multiplex_serum.cardiovascular.EvePanel_SUBMITTED.csv, 15241 B | `73b1e806d5a289002287ad209c0bbb8d` | `73b1e806d5a289002287ad209c0bbb8d` | Byte-idéntico (renombrado) | Tamaño y md5 coinciden |
| `(no local) OSD-575_metadata_OSD-575-ISA.zip` | OSD-575_metadata_OSD-575-ISA.zip, 71702 B | - | `5b29f50d6068120be2734f2a94357425` | NO VERIFICABLE (no hay copia local) | Sin comparación local |

Archivos de OSDR no descargados (sólo verificados por listado de tamaño): 569 tiene 8 archivos más, incluidos dos xlsx de 93 MB y 123 MB. 575 tiene 6 más, incluido un xlsx de 322 799 B. Esos no están en el proyecto y no se descargaron.

### 6.3 Contenido del ISA

- `i_Investigation.txt` contiene los campos de estudio, publicaciones, contactos y ontologías. Los campos de título y descripción de investigación están vacíos, así que la información está en el nivel de estudio.
- Agradecimientos (`Comment[Acknowledgments]`), igual en ambos: "Thanks to the WorldQuant Foundation, NASA, the National Institutes of Health (R01MH117406, P01CA214274 R01CA249054), the LLS (MCL7001-18, LLS 9238-16), and the GI Research Foundation (GIRF)."
- Consentimiento (`Study Protocol Description`): "All crew members have consented for data and sample sharing." El protocolo indica IRB de Weill Cornell Medicine, protocolo 21-05023569.
- Publicaciones de estudio: 10.1038/s41586-024-07639-y (común), 10.1038/s41467-024-48929-3 y 10.1038/s41467-024-48806-z, 10.1093/pcmedi/pbae007, 10.17504/protocols.io.6qpvr33yovmk/v1 (en 569); 10.1038/s41467-024-48806-z y 10.17504/protocols.io.81wgbxxo1lpk/v1 (en 575). El PMID de OSD-569 es 38634106.
- **No hay ningún campo `License`, `Licence`, `Terms` ni `Citation` en ninguno de los dos ISA.** Búsqueda con `licen`, `cite`, `terms`, `copyright`, `reuse`, `attribution` y `creative commons` sobre todos los `.txt` de ambos ZIP: sin resultados de licencia.

## 7. Licencia y condiciones de uso (citas literales)

### 7.1 OSDR (OSD-569 y OSD-575)

- Página del estudio OSD-569 y OSD-575, campo `License`: **"License: CC0-1.0"**, con enlace a `https://spdx.org/licenses/CC0-1.0.html`.
- Panel "Cite this Study", OSD-569: "Mason CE, Overbey EG, Grigorev K, Nelson TM, Garcia Medina J. "Whole Blood Measurements from the SpaceX Inspiration4 Mission (RNA-seq, epitranscriptome, WGS, clonal hematopoiesis, CBC)", NASA Open Science Data Repository, Version 4, http://doi.org/10.26030/e0rx-sh52". Descarga en BibTeX y RIS.
- Panel "Cite this Study", OSD-575: "Mason CE, Overbey EG, Grigorev K, Nelson TM. "SpaceX Inspiration4 Blood Serum Metabolic Panel and Immune/Cardiac Cytokine Arrays (Comprehensive Metabolic Panel and Multiplex)", NASA Open Science Data Repository, Version 3, http://doi.org/10.26030/mc5d-p710".
- Términos del repositorio (`https://www.nasa.gov/reference/osdr-help-terms-and-conditions/`, redirige a `science.nasa.gov`), sección "Citing NASA OSDR Data Sets": "These data are provided under NASA's open access policy. To acknowledge the scientists who have provided data, we request that you include a bibliographic citation to all OSDR-provided data that you use in your publications. Such citations will help others find the products and see how they have been used."
- Mismo documento, "Data Redistribution": "NASA OSDR data and products acquired through the OSDR website are distributed under NASA Science Mission Directorate's Science Information Policy at https://science.nasa.gov/researchers/science-data/science-information-policy".
- Mismo documento, "Acknowledgement": "A general statement crediting NASA OSDR for data, assistance, and/or review." Ejemplo: "GeneLab data are courtesy of the NASA GeneLab Data Repository ( Repository )."
- Mismo documento, "Liability": "For data available from this server, the U.S. Government does not warrant or assume any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed."
- Página OSD-569 (no OSD-575): "Requests and access to restricted files have been temporarily disabled. Data files will not be available for requests at this time." Afecta a archivos restringidos, no a los abiertos usados aquí.

Lectura: CC0-1.0 es una dedicación al dominio público y no exige atribución. El repositorio sí pide cita ("we request"), y la cita es parte de sus términos. Es una lectura de textos publicados, no asesoría legal.

### 7.2 NLSP (LSDA / LSAH)

- Pie de las fichas de experimento y de las páginas de solicitud (no aparece en la portada): **"© 2026 NASA Life Sciences Portal. All rights reserved."**
- Ficha de experimento, sección "Open-Access Data": **"Data preservation is complete. All datasets are publicly available."** (28 experimentos), y **"Data preservation is complete. Privacy-protected datasets are available via data request. Remaining datasets are publicly available."** (2 experimentos).
- Ficha restringida (ejemplo `f48b517c-…`, AD ASTRA): **"Data preservation is complete. All datasets are privacy-protected. Data is available via data request."** y "To request restricted-access data, select your desired variables below and click Request Restricted-Access Data."
- Guía "Data Request Guidelines", apartado "Use of Human Data for Research": **"Be aware that each request for human data must be evaluated and approved through the appropriate NASA review boards prior to the release of any human data."**
- Guía, "Research Data Repository (LSDA)": **"LSDA supports release of astronaut and flight analog subject data to support the research community. Both de-identified and possibly attributable (identifiable) data may be available for internal and external-to-NASA peer-reviewed research studies following a thorough review and approval process and NASA IRB approval."**
- Guía, "Data Request Process": incluye la etapa "Data Use Agreement" (2–3 meses) y "LSAH Advisory Board review before any publication or dissemination" (ongoing).
- Guía, categorías de datos: "Pooled ... Many pooled data from research studies are publicly available on this site."
- Guía, marco legal: "Privacy Act of 1974 (as amended)", "45 CFR Part 46 – Protection of Human Subjects", "HIPAA Minimum Necessary Requirement", "OMB M-06-16".
- **No hay ninguna licencia** (ni CC, ni SPDX, ni "public domain") ni texto de "términos de uso" para los datos abiertos de NLSP. Tampoco hay una frase de cómo citar un dataset de NLSP. Sólo hay listas de citas de publicaciones relacionadas en cada ficha ("Publications" / "Citation"), que son citas de artículos y no del dataset.
- Ninguno de los 18 ZIP locales de NLSP contiene texto de licencia ni de términos (búsqueda sobre todos sus archivos, incluidos los ReadMe y los manifiestos).

Conclusión: los datos abiertos de NLSP se publican bajo la etiqueta "Open-Access Data" de NASA, pero la página no declara licencia ni condiciones de reutilización. La afirmación del proyecto "Licencia: datos de NASA marcados como open access" (08, línea 57) es correcta sólo en el sentido de la etiqueta. El proyecto no debe presentar esos datos como CC0 o como abiertos sin condiciones.

## 8. Discrepancias y notas

1. **Misiones del catálogo local incompletas.** 24 de 48 experimentos tienen "UTMB Campaign 5" en la ficha viva y no en `utmb-experimentos.json`. Ninguna otra diferencia de campo en 48 fichas. Lista en la sección 3.
2. **El texto de `08-nlsp-utmb-datos-abiertos.md` (línea 3): "30 experimentos de reposo en cama marcados "All datasets are publicly available"" es inexacto** (también en `FUENTES.md`, línea 109). Sólo 28 tienen esa frase exacta. Los otros 2 (`950b2ce4-5f5b-5f00-a870-1f24e2897771`, "Human Cerebral Cortex Plasticity…", y `26a8b51f-df92-5a52-9fc0-b8b77067246a`, "Retention of Skeletal, Musculature, and Postural Status…") son parciales. El flag `public: true` en el catálogo también los incluye como públicos.
3. **La licencia de OSDR no está en el ISA.** `00-RESUMEN.md` (pendiente "Licencia de los datos de OSDR (ver `i_Investigation.txt`…)") y `03-osdr-datos-humanos.md` §4 esperaban encontrarla allí. La licencia real es CC0-1.0, indicada en la página del estudio. Cambiar esas notas por la referencia a la página.
4. **NLSP sin licencia declarada.** `08-nlsp-utmb-datos-abiertos.md` (línea 57) dice "Licencia: datos de NASA marcados como open access". La etiqueta existe, pero no hay licencia ni términos. Registrar como NO VERIFICABLE hasta que NASA publique una licencia.
5. **Nombres locales de OSD-575 distintos de OSDR** (`CMP.csv` y `cardio_eve.csv`). El contenido es idéntico. Para citar, usar el nombre oficial.
6. **Falta el ISA de OSD-575 en local.** Se descargó para esta verificación; no se guardó en el proyecto.
7. **Los md5 de los ZIP de NLSP no coinciden con los nuevos.** Es un efecto de marcas de tiempo internas. Para verificación, usar el md5 de los archivos internos o el manifiesto `.md5sum`, no el md5 del ZIP.
8. **Observación de privacidad (fuera de procedencia):** algunos archivos abiertos de NLSP contienen texto libre con nombres de personal, por ejemplo `CRF_Campaign_3_Symptom_Complaint` (ZIP local, línea de C3G 5814): "C. Flores, Licensed Massage Therapist, reported the subject had complaint of lumbar soreness…". Revisar antes de publicar cualquier extracto.
9. **Nota de OSDR:** la página de OSD-569 dice que "Requests and access to restricted files have been temporarily disabled". No afecta a los archivos abiertos usados, pero conviene recordarlo si se piden archivos restringidos.

## 9. Límites de la verificación

- No se re-descargaron todos los ZIP de NLSP ni todos los archivos de OSDR. La muestra es de 7 ZIP de NLSP (de 18 locales), los 5 archivos de OSDR que hay en local y el ISA de OSD-575. Los demás se marcan como NO VERIFICABLE a nivel de contenido.
- El campo `public` del catálogo no existe en la API viva. Se contrastó con `archive_status`, que es el campo que la propia ficha usa.
- La cobertura de experimentos UTMB es la del catálogo local (48). No se buscó si existen experimentos UTMB adicionales fuera de él.
- No se verificó el endpoint de descarga masiva `POST /api/v1/files/bulk-download` que menciona `08`.
- Interpretación de licencias: texto literal citado. No es asesoría legal.

## 10. Archivos de trabajo

- Fichas vivas NLSP: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/live/exp/*.json`; misiones: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/live/mis/*.json`.
- Resolución DOI: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/doi_results.tsv`.
- Descargas NLSP: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/dl/`, `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/dl2/`; extracciones: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/ex-new/`.
- Descargas OSDR: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/osdr-dl/`; ISA extraídos: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/isa-569/`, `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/isa-575/`.
- Páginas renderizadas: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/pages/`; cita OSDR: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/pages/osdr_cite_569.txt`, `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-prov/pages/osdr_cite_575.txt`.

