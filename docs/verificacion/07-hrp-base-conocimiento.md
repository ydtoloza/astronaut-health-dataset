# Verificación de la base de conocimiento HRP (NASA)

Archivo verificado: `/home/user/hackathon-data/04-hrp-base-conocimiento.json`
Fecha de la comprobación: 2026-11-05
Método: descarga en vivo de las 22 páginas (17 riesgos + 5 peligros) con User-Agent de navegador, de forma secuencial y con 2 s de pausa entre peticiones. Texto principal extraído con Python. Las citas se compararon con el texto en vivo tras normalizar espacios, comillas y guiones. Los 22 enlaces de evidencia se comprobaron por HTTP (con seguimiento de redirecciones) y, en los 15 `risk.aspx`, se leyó el título de la página. Los textos locales de `hrp-raw/` no se usaron como fuente de verdad.

## Resumen

- JSON válido (`python3 -m json.tool`). 17 `id`, 17 URL y 17 `nombre_en` únicos. Sin campos obligatorios vacíos. Los `peligros_relacionados` usan solo los 5 peligros definidos.
- Las 22 páginas de NASA responden 200 y los 22 enlaces de evidencia responden 200.
- Citas (`cita_textual`) de riesgos: 12/12 aparecen literalmente. Citas de peligros: 1/2 literal; la de gravedad falta la palabra "of".
- Efectos soportados por el texto de NASA: 63/70. Contramedidas soportadas: 44/46.
- Hay 4 nombres en inglés que no coinciden con el título actual de la página (R08, R10, R12; R12 es el más claro).
- Un peligro asignado sin soporte (R12 "Radiación espacial") y dos enlaces de evidencia que apuntan a otro riesgo (R04 y R06).
- Dos indicadores marcados mal respecto de la página (R11 y R17) y un indicador dudoso (R10).
- La gravedad de Marte: NASA dice "aproximadamente un tercio" de la gravedad terrestre. El valor físico es ≈0,38 g (≈3/8). Ninguna página consultada dice 3/8.

## 1. Riesgos: tabla por riesgo

Leyenda: "x/y" = número de ítems SOPORTADO sobre el total. Los ítems "parcial" no cuentan como soportados. "Citas x/y" cuenta solo las `cifras`. "—" significa que no hay cifras.

| Riesgo | URL ok | Nombre en inglés | Citas x/y | Efectos x/y | Contramedidas x/y | Problemas |
|---|---|---|---|---|---|---|
| HRP-R01 Altered Immune System Responses (Inmunológico) | 200 | Coincide | — | 5/5 | 1/1 | Ninguno relevante. Indicador de muestras en vuelo (inferido:false) confirmado en la página. |
| HRP-R02 Altered Sensorimotor and Vestibular Function | 200 | Coincide | 1/1 | 5/5 (3 de ellos solo en la página del peligro Campos gravitatorios) | 1/2 | La contramedida "dispositivo giratorio de la Marina de EE. UU." no aparece. La página dice que la Marina prueba movimientos de cabeza para aliviar el mareo al salir de un simulador de vuelo. |
| HRP-R03 Cardiovascular Adaptations | 200 | Coincide | — | 5/5 | 4/4 | Ninguno. "Corazón más esférico" viene de "Did you know". |
| HRP-R04 Decompression Sickness | 200 | Coincide | — | 3/3 | 5/5 | Enlace de evidencia `risk.aspx?i=179` es el riesgo **Cardiovascular**, no descompresión. La propia página de NASA enlaza ese ID. "Hábitats a menor presión" en la página dice "spacecraft" (naves para espacio profundo). |
| HRP-R05 Host-Microorganism Interactions | 200 | Coincide | — | 4/4 | 2/2 | Ninguno. "Transmisión más fácil entre tripulantes" viene de la página del peligro Entornos cerrados. |
| HRP-R06 Hypoxia | 200 | Coincide | — | 4/4 | 3/3 | Enlace de evidencia `risk.aspx?i=85` es el riesgo **Inmunológico**. La propia página de NASA enlaza ese ID. |
| HRP-R07 Inadequate Food and Nutrition | 200 | Coincide | 1/1 | 2/4 | 4/4 | "Menor apetito": NO SOPORTADO. "Pérdida de valor nutricional" y "Desequilibrios nutricionales a largo plazo": INFERIDOS, no marcados. "Impacto en salud física y mental" solo parcial ("crew illness", "performance decrement"). "Fatiga de menú" sí aparece (como riesgo a evitar). |
| HRP-R08 Injury and Compromised Performance from EVA | 200 | **No coincide**: la página se titula "...from Spacewalks" | 1/1 | 2/4 | 3/3 | Nombre. "Pérdida de destreza" y "Fatiga por el peso del traje" solo parciales (la página habla de destreza como requisito de diseño y del peso del traje en superficie). Descripción dice "flexibles": no aparece (la página dice "durable and safe ... dexterity"). |
| HRP-R09 Reduced Cardiorespiratory and Musculoskeletal Fitness | 200 | Coincide | 3/3 | 5/5 | 1/1 | Descripción dice "entrenamiento aeróbico diario"; la página dice "6 a 7 días por semana". |
| HRP-R10 Spaceflight-Associated Neuro-ocular Syndrome (SANS) | 200 | Diferencia menor (guion y "Associated" en el título de la página) | 1/1 | 4/5 | 3/3 | "Alteraciones visuales" no aparece como efecto; la página solo dice cambios en el nervio óptico, pliegues en la retina, aplanamiento del ojo e inflamación cerebral. Indicador "Fondo de ojo" marcado inferido:true, pero la página muestra un fundoscopio para examinar la retina. |
| HRP-R11 Spaceflight-Induced Bone Changes | 200 | Coincide | 2/2 | 4/4 | 2/2 | Indicador "Densidad ... mediante escaneo óseo" marcado inferido:true, pero la página dice que los astronautas se hacen "routine bone scans"; solo "DXA" es inferencia. Falta la contramedida de bisfosfonatos que menciona la página. |
| HRP-R12 Behavioral Conditions and Psychiatric Disorders | 200 | **No coincide**: la página se titula "Risk of Behavioral Changes and Psychiatric Disorders" | 1/1 | 5/5 | 4/4 | Peligro "Radiación espacial" NO SOPORTADO: la página solo habla de aislamiento y de retrasos de comunicación en una misión de varios años a Marte. "Ventanas" viene de "Did you know" (válido, pero contexto). |
| HRP-R13 Inadequate Teamwork | 200 | Coincide | — | 3/4 | 3/3 | "Pérdida de eficacia en la resolución de problemas": no declarado (solo se menciona "problem solving" como tarea). |
| HRP-R14 Inadequate Sleep and Irregular Schedules | 200 | Coincide | 1/1 | 4/4 | 2/2 | Falta la contramedida de "tiempos designados para relajación y autocuidado" (la página la menciona). |
| HRP-R15 Inadequate Systems Operations Support | 200 | Coincide | 1/1 | 2/3 | 2/2 | "Errores en procedimientos sin apoyo de tierra": INFERIDO, no declarado. Descripción dice "con retrasos de comunicación": la página dice "más largas y lejanas", sin mencionar retrasos. |
| HRP-R16 Injury from Dynamic Loads | 200 | Coincide | — | 3/3 | 2/2 | Ninguno. La desorientación aparece como "possible" factor. |
| HRP-R17 Radiation-Induced Cancers | 200 | Coincide | — | 3/3 | 2/3 | "Protección que proporciona la magnetosfera" NO es contramedida: es contexto ("Did you know"). Indicador "Dosimetría personal" marcado inferido:false, pero la página solo dice que hay instrumentos de medición de radiación a bordo de la ISS. |

Totales: citas de riesgos 12/12 literales. Efectos 63/70. Contramedidas 44/46. Indicadores con `inferido` incorrecto: R11 (escaneo óseo), R17 (dosimetría) y R10 (fondo de ojo, optativo).

### 1.1 Detalle de citas de riesgos (todas literales)

| Riesgo | Cita | Resultado |
|---|---|---|
| R02 | "The majority of astronauts experience motion sickness during spaceflight." | Literal |
| R07 | "More than 200 foods and beverages are available aboard the space station." | Literal |
| R08 | "It lasted 8 hours and 56 minutes." | Literal |
| R09 | "Six to seven days a week, ... for 1.5 hours per day" | Literal |
| R09 | "average losses to strength and aerobic fitness are 10-12% of pre-mission levels" | Literal |
| R09 | "between 12-38% of space station crew members lose more than 20% of their pre-mission fitness" | Literal |
| R10 | "Approximately 70 percent of astronauts aboard the International Space Station experience some swelling in the back of their eyes." | Literal |
| R11 | "on average, bones lose between 1% and 1.5% of their density each month during four-to-six-month missions" | Literal |
| R11 | "the height of crew members can increase as much as 3% in space." | Literal |
| R12 | "Future deep space exploration will require crews to live together in a confined environment roughly the size of a studio apartment for multiple years" | Literal |
| R14 | "Astronauts witness 16 sunrises and sunsets per day aboard the space station" | Literal |
| R15 | "NASA astronauts train, on average, 300 hours in simulators before launch" | Literal |

## 2. Peligros: tabla de comprobación

| Peligro | URL / título | Descripción | Cifras | Problemas |
|---|---|---|---|---|
| Radiación espacial | 200. "Hazard: Space Radiation" | OK. "Daña el sistema nervioso central" aparece en la página. | 0 | Ninguno. |
| Aislamiento y confinamiento | 200. "Hazard: Isolation and Confinement" | OK. | 0 | La página incluye HERA (650 pies²; 45 días) y CHAPEA (1.700 pies²; año). No están en `cifras`. Opcional añadirlas. |
| Distancia a la Tierra | 200. "Hazard: Distance From Earth" | OK. | 1/1 literal ("Mars is, on average, 140 million miles from Earth.") | Falta el dato de hasta 20 min de retraso (ver tabla 3). La página también dice "roughly three years" para el viaje. Cuidado: la página dice "five minutes each way" para HERA (simulado). No confundirlo. |
| Campos gravitatorios | 200. "Hazard: Gravity Fields" | "Un tercio de la gravedad terrestre" refleja lo que dice NASA. | 0/1 literal: falta "of" | Ver tabla 3 sobre la gravedad de Marte. Corregir la cita. |
| Entornos hostiles/cerrados | 200. "Hazard: Hostile/Closed Environments" | OK. | 0 | "650-square-foot habitat" (HERA) aparece en la página, no en `cifras`. |

## 3. Afirmaciones específicas

| Afirmación | Qué dice la página de NASA | Estado |
|---|---|---|
| Marte a ~140 millones de millas en promedio | Página "Hazard: Distance From Earth": "Mars is, on average, 140 million miles from Earth." | Verificada (literal) |
| Retraso de comunicación de hasta 20 min en un sentido | Página "Hazard: Distance From Earth": "Facing a communication delay of up to 20 minutes one way". | Verificada. No está en el JSON. Añadir como cifra. |
| HERA: 650 pies² (≈60 m²), misiones de 45 días | Página "Hazard: Hostile/Closed" (650-square-foot, dos pisos y altillo); Página "Hazard: Isolation": "650-square-foot habitat ... live inside this habitat for 45 days at a time". | Verificada. Nota: "650 sq ft" es el dato de NASA; 650 pies² = 60,4 m², el cálculo está bien. |
| CHAPEA: 1.700 pies², 4 tripulantes, un año | Página "Hazard: Isolation": "year-long stays", "four crew members", "1,700-square-foot habitat" (Mars Dune Alpha). | Verificada. |
| Gravedad de Marte | Única página: "Hazard: Gravity Fields": "crews will be in approximately one-third of Earth's gravity". No aparece "three-eighths" ni "0.38" en ninguna página consultada. | Discrepancia con el valor físico. La gravedad superficial de Marte es ≈3,71 m/s² ≈ 0,38 g, cercana a 3/8 (0,375). "Un tercio" (0,333) es una aproximación de NASA, un 13 % por debajo. Recomendación: atribuir "un tercio" a NASA y añadir el valor ≈0,38 g. |

## 4. Enlaces de evidencia

Las 22 URL únicas responden 200. Cada `risk.aspx` se comprobó por su título de HRR.

| ID HRR | Título en HRR | Riesgo del JSON | Coherencia |
|---|---|---|---|
| i=85 | Altered Immune Response | R01 | Correcto |
| i=85 | Altered Immune Response | R06 Hypoxia | **Incorrecto**: la página de hipoxia enlaza este ID, pero es el riesgo inmunológico |
| i=88 | Altered Sensorimotor/Vestibular | R02 | Correcto |
| i=179 | Cardiovascular Adaptations | R03 | Correcto |
| i=179 | Cardiovascular Adaptations | R04 Decompression Sickness | **Incorrecto**: enlace de NASA a otro riesgo |
| i=80 | Host-Microorganism Interactions | R05 | Correcto |
| i=176 | Performance Decrement and Crew Illness due to Food | R07 | Correcto |
| i=84 | Injury/Performance EVA | R08 | Correcto |
| i=180 | Reduced Cardiorespiratory/Musculoskeletal Fitness | R09 | Correcto |
| i=105 | SANS | R10 | Correcto |
| i=77 | Bone Fracture | R11 | Correcto |
| i=99 | Cognitive/Behavioral and Psychiatric | R12 | Correcto |
| i=101 | Team Cooperation/Coordination | R13 | Correcto |
| i=100 | Sleep Loss, Circadian Desynchronization | R14 | Correcto |
| i=175 | Earth-Independent Human-Systems Operations | R15 | Correcto |
| i=167 | Dynamic Loads | R16 | Correcto |
| i=96 | Radiation Carcinogenesis | R17 | Correcto |

Otros enlaces (PDF y `/evidence/`), todos 200 y relevantes: Cardio Risk EB 2022 (R03); Nutrition ER 2020 (R07); ochmo-tb-030-bone-loss (R11); whatisyourspaceheight (R11); 160410 space training fact sheet (R15); Degen.pdf (R17). El índice `/evidence/` aparece en todos los riesgos y está bien.

## 5. Correcciones concretas para el JSON

1. **R12 `nombre_en`**: cambiar a "Risk of Behavioral Changes and Psychiatric Disorders" (título actual de la página).
2. **R12 `peligros_relacionados`**: quitar "Radiación espacial" y añadir "Distancia a la Tierra" (la página habla de retrasos de comunicación en una misión multianual a Marte).
3. **R08 `nombre_en`**: usar "Risk of Injury and Compromised Performance from Spacewalks" o anotar que el nombre "EVA" es el de la URL.
4. **R08 `descripcion_es`**: quitar "flexibles". La página dice "duraderos y seguros, con destreza y monitorización biomédica".
5. **R08 `efectos_salud`**: reformular "Pérdida de destreza y rendimiento" y "Fatiga por el peso del traje en superficie planetaria" como carga física y mental y peso del traje (o marcarlos como parciales).
6. **R10 `nombre_en`**: "Risk of Spaceflight Associated Neuro-ocular Syndrome (SANS)" (sin guion).
7. **R10 `efectos_salud`**: quitar "Alteraciones visuales" o marcarlo como no declarado.
8. **R10 indicador "Fondo de ojo y agudeza visual"**: la página muestra un fundoscopio para examinar la retina. Puede pasar a inferido:false para "fondo de ojo" (agudeza visual sigue siendo inferencia).
9. **R02 `contramedidas`**: sustituir "Estudios de desorientación en simulación terrestre (p. ej., dispositivo giratorio de la Marina de EE. UU.)" por "Pruebas con la Marina de EE. UU. sobre movimientos de cabeza para aliviar el mareo al salir de un simulador de vuelo".
10. **R04 `enlaces_evidencia`**: el ID `i=179` es riesgo cardiovascular. Quitar `risk.aspx?i=179` o anotar en `nota` que es un enlace de NASA a otro riesgo.
11. **R06 `enlaces_evidencia`**: el ID `i=85` es riesgo inmunológico. Igual que el punto 10.
12. **R04 `contramedidas`**: "Hábitats diseñados a menor presión" pasa a "Naves para espacio profundo diseñadas a menor presión" (así lo dice la página).
13. **R07 `efectos_salud`**: quitar "Menor apetito" (no soportado). Marcar o quitar "Pérdida de valor nutricional de la dieta" y "Desequilibrios nutricionales a largo plazo" (inferidos).
14. **R11 indicador "Densidad mineral ósea mediante escaneo óseo (p. ej., DXA)"**: inferido pasa a false y el texto a "Densidad ósea mediante escaneos antes y después del vuelo". "DXA" se deja como ejemplo inferido.
15. **R11 `contramedidas`**: añadir "Medicamentos tipo bisfosfonato (estudios de la NASA sugieren que mitigan parte de la pérdida ósea)".
16. **R13 `efectos_salud`**: "Pérdida de eficacia en la resolución de problemas" pasa a "Problemas de coordinación, cooperación y comunicación" (lo que dice la página), o se marca inferido.
17. **R14 `contramedidas`**: añadir "Tiempos designados para relajación y autocuidado".
18. **R15 `efectos_salud`**: "Errores en procedimientos sin apoyo de tierra" pasa a inferido o se quita.
19. **R15 `descripcion_es`**: quitar "con retrasos de comunicación" o indicar que es contexto de Marte.
20. **R09 `descripcion_es`**: "entrenamiento ... diario" pasa a "6 a 7 días por semana".
21. **R17 `contramedidas`**: quitar "Protección que proporciona la magnetosfera en misiones cercanas (contexto)". Es contexto, no contramedida.
22. **R17 indicador "Dosimetría personal de radiación de la tripulación"**: el texto no lo dice. Cambiar a "Instrumentos de medición de radiación a bordo de la ISS" con inferido:false, o marcar inferido:true.
23. **Peligro Campos gravitatorios `cifras[0].cita_textual`**: pasa a "weight-bearing bones lose on average 1% to 1.5% of mineral density per month during spaceflight" (falta "of").
24. **Peligro Campos gravitatorios `descripcion_es`**: añadir la atribución: "un tercio de la gravedad terrestre (según NASA; el valor real en Marte es ≈0,38 g, cercano a 3/8)".
25. **Peligro Distancia a la Tierra**: añadir cifra "Hasta 20 minutos de retraso de comunicación en un sentido" con cita "Facing a communication delay of up to 20 minutes one way", y "Viaje de unos tres años" con "roughly three years".
26. **Peligro Aislamiento**: añadir cifras HERA ("650 pies²; 45 días por estancia", cita "is a unique 650-square-foot habitat ..." y "Crews of volunteers live inside this habitat for 45 days at a time") y CHAPEA ("1.700 pies²; 4 tripulantes; estancias de un año", cita "an isolated 1,700-square-foot habitat" y "year-long stays").
27. **Peligro Entornos hostiles**: añadir cifra "650 pies²" (HERA) con cita "650-square-foot habitat split among two floors and a loft".
28. **Nota de nivel superior**: indicar que la verificación se hizo el 2026-11-05 contra páginas en vivo, y que los `inferido:true` son estándar salvo los corregidos en los puntos 8, 14 y 22.

## 6. Notas

- Los peligros asignados (`peligros_relacionados`) son plausibles en 16 de 17 casos. El caso R12 no lo es (punto 2). Como indica la `nota`, no es una lista oficial de NASA, y ninguna página la declara.
- Todas las comprobaciones usan el texto en vivo, no `hrp-raw/`. No se comparó `hrp-raw/` con la página en vivo.
- Los cambios de esta verificación no tocan los archivos existentes. Solo se escribió este informe.
