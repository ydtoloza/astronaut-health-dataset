# Verificación de datos de laboratorio (UTMB e Inspiration4)

**Fecha:** 2026-11-05. **Alcance:** comprobar que `utmb/utmb_laboratorio.csv`, `osdr-inspiration4-clinico.csv`, `demo/demo_laboratorio.csv` y las cifras de `12-inspiration4-cmp-phenoage.md` y `03-osdr-datos-humanos.md` son fieles a los archivos originales.

**Método:** scripts Python escritos desde cero y ejecutados con `python3 -I`, sin reutilizar `scripts/*`. Ningún archivo existente fue modificado; este informe es el único archivo escrito en el proyecto.
- Scripts y salidas intermedias: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/audit/` (`a1_raw_utmb.py` … `a12_final_sens.py`).
- Descargas independientes de OSDR: `/tmp/claude-0/-home-user/2282e4a3-bc4d-5a83-85c9-edd865fb4843/scratchpad/verif-labs/` (tratadas como datos no confiables).

---

## 0. Resumen

- **Las descargas de OSDR son idénticas a los archivos locales** (CBC OSD-569, CMP OSD-575 y panel Eve OSD-575, comparados por SHA-256). El material de Inspiration4 está bien copiado: `demo_laboratorio.csv` reproduce sus 1.090 valores de Inspiration4 sin diferencias.
- **Las afirmaciones de Inspiration4 (a, b) se reproducen**, salvo redondeos de una décima o de un punto porcentual. La conversión de CRP (÷10^7) es correcta. Los valores de CRP son altos para sujetos sanos y no se pueden verificar sin una referencia externa.
- **Problema crítico en UTMB: faltan 21 de los 31 sujetos con laboratorio.** Los archivos de 21 sujetos usan la cabecera `ParameterName` en lugar de `Parameter Name`. El derivado contiene exactamente los 10 sujetos que sí tienen la cabecera esperada. Se pierden 6.762 filas.
- **Problema crítico en UTMB: se eliminan todos los valores con marca de laboratorio.** Son 280 valores numéricos en los 10 sujetos incluidos, con sufijos como `(H)`, `(L)`, `A` o `B`. Son justo los valores fuera de rango, así que los resúmenes quedan sesgados.
- **La "hemoglobina 131" no es un problema de unidades.** Es un error de coma decimal en el origen; el valor correcto es **13,1 g/dL**. La "hemoglobina 182" que citan el resumen por fase y `08` **no existe** en los datos.
- **El resumen por fase (`utmb_resumen_por_fase.csv`) reproduce medias, DE y n desde el derivado**, pero **23 de 24 percentiles p5/p95 no se pueden reproducir**. Algunos caen fuera del rango de los datos (p95 de hemoglobina 182,34 con máximo 131).
- **Armonización:** hay analitos con magnitudes distintas bajo el mismo código (alfa-1, beta y gamma en g/dL y en %), ALT duplicada y BSAP mezclada en U/L y µg/L.
- **Conteos:** la suma de `demo_laboratorio` (3.100) es correcta, pero el 2.010 de UTMB es un subconjunto del origen, no el total disponible.

**Conteo de estados (tabla principal, 49 filas):** OK = 30 · DISCREPANCIA = 15 · NO VERIFICABLE = 4.

---

## 1. Tabla de verificación

| # | Afirmación | Declarado | Recalculado | Estado | Nota |
|---|---|---|---|---|---|
| a1 | Inspiration4, WBC L-3 → R+1 (n=4) | 8,65 → 6,40 (−26 %); baja en 4/4 | 8,65 → 6,40 (−26,0 %); baja en 4/4 (C001 7,0→5,0; C002 7,2→5,5; C003 9,8→7,0; C004 10,6→8,1) | OK | Fuente: `cbc_569` (OSD-569) |
| a2 | Linfocitos absolutos | 2911 → 1855 (−36 %) | 2910,75 → 1855,25 (−36,3 %) | OK | cél/µL |
| a3 | Neutrófilos absolutos | 4845 → 3657 (−25 %) | 4845,25 → 3657,25 (−24,5 %) | OK | Redondeo; baja en 4/4 |
| a4 | Hemoglobina | 14,1 → 14,2 | 14,075 → 14,200 (n=4) | OK | C003 en R+1 está como `HEMOGLOBIN (FEMALE)`; fusionarla es correcto (sexo F) |
| a5 | Plaquetas | 290 → 270 | 290,25 → 269,5 (−7,1 %) | OK | |
| a6 | VCM | 93,6 → 89,1 | 93,625 → 89,075 (−4,9 %); baja en 4/4 | OK | |
| a7 | Rangos de referencia de la tabla 03 | p. ej. WBC 3,8–10,8; Hb 13,2–17,1 | Son los de C001 (varón). Para mujeres, Hb 11,7–15,5 | OK | Un solo rango para una cohorte de 2 sexos: aclarar en la tabla |
| b1 | Glucosa L-3 → R+1 | 69,5 (56–78) → 93,3 (83–103); sube en 4/4 | 69,5 (56–78) → 93,25 (83–103); sube en 4/4 | OK | mg/dL |
| b2 | Fosfatasa alcalina | 49,8 → 56,5; sube en 4/4 | 49,75 → 56,5; sube en 4/4 | OK | U/L |
| b3 | Creatinina | 1,14 → 1,03 | 1,135 → 1,028 (baja en 3/4; C004 sube 1,13 → 1,15) | OK | La media sí; "baja en todos" no se afirma |
| b4 | Calcio | 9,65 → 9,53 | 9,65 → 9,525 | OK | |
| b5 | Albúmina estable | 4,2–4,9 | 4,2–4,9 en L-3 y en R+1 | OK | En toda la serie va de 4,2 a 5,1 |
| b6 | R+45: 3 de 4 glucosas entre 36 y 44 | 36 (C003), 43 (C004), 44 (C002) | Correcto. C001 = 84 | OK | Las tres están marcadas como atípicas |
| b7 | Causa: "probable glucólisis por demora" | Artefacto de muestra | No hay datos de manejo de muestra | NO VERIFICABLE | Es una hipótesis; el documento lo presenta como probable |
| c1 | Conversión CRP pg/ml → mg/dL = ÷10^7 | ÷10^7 | 1 pg/mL = 10^-7 mg/dL (análisis dimensional). Ej.: 18.385.000 pg/mL → 1,8385 mg/dL. El TRANSFORMED de OSDR también está en pg/mL (28/28 coinciden) | OK | |
| c2 | Valores de CRP "plausibles" | Plausibles | 1,3–83,6 mg/L (0,13–8,4 mg/dL); mediana 12,3 mg/L; 16 de 28 > 10 mg/L. C001: 18,4 (L-92), 2,2 (L-44), 5,1 (L-3) mg/L | NO VERIFICABLE | Son valores altos para adultos sanos y con una oscilación de 8× en 48 días. Pedir referencia al laboratorio |
| c3 | Unidad de origen de la CRP | "revisar unidades: ng/ml → mg/dL" (doc 12) | El archivo y el TRANSFORMED dicen **pg/ml** | DISCREPANCIA | Aplicar ÷10^4 (ng/ml) daría valores 1.000 veces mayores. El derivado usa pg/ml, que es correcto |
| d1 | UTMB glucosa por fase: 84,7 / 79,9 ± 4,9 / 81,3 ± 7,2 | Como en resumen | Desde `utmb_laboratorio.csv`: 84,67 (n=3) / 79,88 ± 4,91 (n=8) / 81,29 ± 7,20 (n=7) | OK | Solo aritmética sobre el derivado |
| d2 | Representatividad de d1 | Medias de la cohorte | Con los 31 sujetos sin marcas: 83,8 (n=24) / 82,9 (n=37) / 84,7 (n=38). Con marcas: 81,4 / 81,3 / 82,9 | DISCREPANCIA | El derivado tiene 10 sujetos y ha eliminado los valores bajos marcados (63 (L), 68 (L), 66 (L)…) |
| d3 | WBC por fase: 6,18 / 6,11 / 7,35 | Como en resumen | 6,18 / 6,11 / 7,35 (n=10/15/11) | OK | Solo aritmética |
| d4 | WBC: representatividad | — | 31 sujetos sin marcas: 6,16 / 6,15 / 6,64. El POST baja de 7,35 a 6,64 | DISCREPANCIA | Mismo motivo que d2 |
| d5 | Sodio, potasio, calcio, creatinina por fase | Como en resumen | Media, DE y n reproducibles en todas las filas. Con 31 sujetos: Ca 9,38 / 9,37 / 9,29 (resumen: 9,13 / 9,06 / 8,99); Cr 0,95 / 0,92 / 0,92 (resumen: 0,92 / 0,84 / 0,86) | DISCREPANCIA | Aritmética correcta; representatividad y sesgo no |
| d6 | Percentiles p5/p95 del resumen | Valores publicados | 23 de 24 filas no reproducibles. Algunas caen fuera del rango de los datos: p95 glucosa PRE 87,6 (máx. 86,0); p95 Hb POST 182,34 (máx. 131,0); p5 Hb POST 11,91 (mín. 12,0); p5 WBC POST 3,24 (mín. 4,0) | DISCREPANCIA | Un percentil no puede quedar fuera del rango de sus datos. El método o los datos del resumen no coinciden con el derivado |
| d7 | "Hemoglobina de 182" (resumen por fase y `08`, l. 54) | 182 | No hay ninguna hemoglobina de 182. El dato es **131** (UTMB-36). El único 182 sin marca en el derivado es LDH (UTMB-04, POST, 182,0) | DISCREPANCIA | Ver §3.3 |
| e1 | Las 9 entradas de PhenoAge existen en Inspiration4 | Presentes | 27 de 28 combinaciones sujeto × tiempo tienen las 9 (falta MCV en C002 R+194). Por sujeto: C001 7/7, C002 6/7, C003 7/7, C004 7/7 | OK | Ver §5 |
| e2 | Las 9 entradas existen en UTMB (origen) | Presentes en ambas fuentes | 31 de 31 sujetos. 114 de 117 fechas con las 9 (PCR mg/L convertida ÷10) | OK | Existencia en el origen |
| e3 | Las 9 entradas existen en UTMB (derivado / demo) | Presentes en ambas fuentes | Solo 11 de 36 fechas con las 9; 4 de 10 sujetos tienen alguna. 5814 no tiene PCR: sus 4 valores están en mg/L y se omiten | DISCREPANCIA | El derivado no refleja el origen (§3.1 a §3.5) |
| f1 | `ALBUMIN/GLOBULIN RATIO` no se mapea a `albumina` | No mapeada | → `albumin_globulin_ratio` | OK | |
| f2 | `Alkaline phosphatase, bone specific` no se mapea a `fosfatasa_alcalina` | No mapeada | → `alkaline_phosphatase_bone_specific_*` | OK | |
| f3 | Variantes i-STAT | Tratadas | Se mantienen separadas de los analitos de laboratorio. `i-STAT pH`/`i-STAT ph` e `I-STAT Potassium`/`i-STAT Potassium` están unificadas | OK | Tratamiento deliberado; criterio razonable |
| f4 | Una unidad por analito | Consistente | `alpha_1`, `alpha_2`, `beta`, `gamma`: G/DL y % bajo el mismo código (magnitudes distintas). BSAP: U/L y µg/L bajo el mismo código. `thyroxine_free_t4`: ng/cL (32) y ng/dL (4) | DISCREPANCIA | Las mezclas de alfa/beta/gamma son errores reales; ng/cL es una errata (ver §5) |
| f5 | Un nombre de origen = un código | Consistente | ALT en `alt` (20 filas) y `alanine_aminotransferase_alt` (15 filas), misma prueba y misma unidad. `creatinine_urinec` vs `creatinine_urine_c` y `n_telopeptide_urinec` vs `n_telopeptide_urine_c` | DISCREPANCIA | Menor. `albumin` (% SPE) y `albumina` (g/dL) se distinguen bien, pero el nombre se presta a confusión |
| f6 | Los 6 valores atípicos existen en el origen | 6 | 6 de 6: Hb 131 (992, 6/1/2005), PLT 12,9 y neutrófilos abs. 10,1 (C003 L-92), glucosa 44 (C002), 43 (C004), 36 (C003) en R+45 | OK | |
| f7 | Hemoglobina 131: ¿unidades (g/L) o error? | Unidad o error | **Error de coma decimal**: el valor correcto es **13,1 g/dL**. Hb = MCHC × Hct / 100 = 33 × 39,8 / 100 = 13,1. Hb = MCH × RBC / 10 = 29 × 4,55 / 10 = 13,2 | DISCREPANCIA | Dato erróneo en el origen. Si se leyera como g/L también daría 13,1 g/dL; el número 131 en g/dL no es válido |
| f8 | Lista de atípicos completa | 6 | Faltan anomalías en la misma toma C003 L-92 (§4.2). El criterio de `atipico` no está documentado | DISCREPANCIA | |
| f9 | `03`: "probable error de transcripción" en C003 L-92 | Un error puntual | Patrón de desplazamiento de columnas en el bloque entero (§4.2) | DISCREPANCIA | La interpretación es incompleta |
| g1 | `demo_laboratorio` = 3.100 filas | 3.100 | 3.100 = 2.010 + 553 + 509 + 28 | OK | |
| g2 | UTMB = 2.010 filas | 2.010 | Es el derivado (2.010 sin marcas de los 10 sujetos). El origen tiene 6.851 filas sin marcas con los mismos analitos, de los 31 sujetos | DISCREPANCIA | Completitud (§3.1, §3.2). Doc `08` dice "10 sujetos" en la descripción del derivado |
| g3 | OSD-569 = 553 | 553 | 553 (CBC completo) | OK | |
| g4 | OSD-575 = 509 | 509 | 531 − 22 `NA` (21 `BUN/CREATININE RATIO` y 1 `BILIRUBIN; TOTAL`) = 509 | OK | |
| g5 | Eve CRP = 28 | 28 | 28 (7 tiempos × 4 sujetos) | OK | |
| x1 | Descargas OSDR idénticas a los locales | — | SHA-256 iguales: CBC OSD-569, CMP OSD-575 y Eve OSD-575 (3/3) | OK | |
| x2 | Valores de Inspiration4 en `demo_laboratorio` | — | 1.090 valores, 0 diferencias (tolerancia 5×10^-5 en CRP por redondeo a 4 decimales) | OK | |
| x3 | Atribución del CBC a Quest Diagnostics (`03`) | Quest | ISA de OSD-569: `complete-blood-count_hematology-analyzer_Quest Diagnostics` | OK | |
| x4 | `03`: "23 analitos tras fusionar variantes" | 23 | 20 tras fusionar (23 nombres en bruto) | DISCREPANCIA | Menor |
| x5 | `demo/LEEME.md`: "Junta todos los datos reales"; "los otros 11 solo tienen cognición o laboratorio" | — | Hay laboratorio en el origen para 31 sujetos. `demo_astronautas.laboratorio = no` para 21 | DISCREPANCIA | |
| x6 | `dia_relativo` de UTMB (ancla por mediana de fecha − BR_Day) | Método documentado | Reproducible con el método. No verificable contra las fechas oficiales de inicio. Los PRE tienen BR_Day positivo (7–18) | NO VERIFICABLE | |
| x7 | Unidades y rangos de Inspiration4 en `demo` | — | 0 diferencias frente al origen | OK | |
| x8 | Unidad de la CRP de UTMB (mg/dL en 9 sujetos, mg/L en 22) | Conversión implícita | Escalas distintas: mediana 0,74 mg/dL en el grupo mg/dL frente a 1,22 mg/L en el grupo mg/L (≈ 6×). El origen no documenta la unidad | NO VERIFICABLE | No se puede decidir qué grupo está mal etiquetado sin la documentación de la campaña |

---

## 2. Descargas independientes de OSDR

| Archivo | Local (`osdr-raw/`) | Descargado (`verif-labs/`) | Resultado |
|---|---|---|---|
| CBC OSD-569 `LSDS-7_Complete_Blood_Count_CBC.upload_SUBMITTED.csv` | 26.138 B | 26.138 B · `10a878b0…9457d3` | Idéntico |
| CMP OSD-575 `CMP.csv` (`LSDS-8_Comprehensive_Metabolic_Panel_CMP.upload_SUBMITTED.csv`) | 25.275 B | 25.275 B · `dab247eb…4192a0` | Idéntico |
| Eve cardiovascular OSD-575 `cardio_eve.csv` | 15.241 B | 15.241 B · `a6422f9b…5e96c` | Idéntico |
| Eve TRANSFORMED (`crp_concentration_picogram_per_milliliter`) | — | 28 valores | Coinciden con el SUBMITTED (28/28) |

El listado `files569.json` y `files575.json` confirma los nombres y tamaños. Las descargas se hicieron con `curl -sSL` contra `geode-py/ws/studies/.../download`.

---

## 3. Hallazgos en UTMB

### 3.1 Archivos omitidos por la variante de cabecera

Los 31 archivos de laboratorio (campaña 3, `MR010G`) tienen dos cabeceras: `Parameter Name` (10 archivos) y `ParameterName` (21 archivos). El derivado solo contiene los 10 primeros. `demo_astronautas.csv` marca `laboratorio = si` exactamente para esos 10.

| Cabecera | Sujetos | Filas en origen | Presentes en el derivado |
|---|---|---|---|
| `Parameter Name` | 224, 3768, 4023, 5788, 5814, 6345, 7127, 7352, 7772, 992 (10) | 2.772 | Sí (2.010 filas sin marca) |
| `ParameterName` | 3985, 5165, 5580, 5683, 5705, 5907, 6043, 6607, 6858, 7961, 7984, 8454, 8615, 8779, 8881, 9016, 9032, 9139, 9314, 9485, 9947 (21) | 6.762 | **No** |

Dentro de los 21 omitidos hay 5.700 valores numéricos (4.841 sin marca con los analitos que usa el derivado). Incluyen 81 PCR en mg/L (ver §3.5).

Con las mismas reglas de nombre y sin marca, el origen completo produce **6.851** filas. El derivado tiene **2.010**, es decir, el 29 %.

### 3.2 Valores marcados eliminados

Los archivos de UTMB añaden a algunos valores una marca de laboratorio: `(H)`, `(L)`, `A`, `B`, `C`, `D`, `E`, `F`. El derivado descarta todos esos valores: en los 10 sujetos incluidos son **280 valores numéricos**, sin ninguna excepción (`derived ⊂ raw sin marca`, 0 filas extra). Ejemplos:

- Glucosa `63  (L)`, sujeto 224, 6/5/2005 (POST). Glucosa `68  (L)`, sujeto 992, 6/1/2005.
- Calcio `8,5  (L)`, sujeto 992. Sodio `136  (L)`, sujeto 992.
- LDH `182  (H)`, sujeto 992 (IN_TEST). Creatina quinasa `342  (H)`, sujeto 224 (PRE).
- Hemoglobina `17,7  (H)` y `17,8 (H)`, sujeto 6345.

Consecuencias: las medias por fase, la lista de atípicos y el cálculo de PhenoAge quedan sesgados hacia los valores normales.

### 3.3 Hemoglobina 131 y la "hemoglobina 182"

- Fila de origen: sujeto 992 (UTMB-36), 6/1/2005, POST_TEST, BR_Day 0, panel L-45/30. `Hemoglobin = 131`, unidad `g/dL`, rango `13,5–17,0`.
- En la misma toma: `Hematocrit = 39,8 %`, `MCHC = 33`, `MCH = 29`, `RBC = 4,55`, `MCV = 87`.
- Cálculo: Hb = MCHC × Hct / 100 = 13,1 g/dL; Hb = MCH × RBC / 10 = 13,2 g/dL. Los índices confirman **13,1 g/dL**. El 131 es un desplazamiento de la coma decimal, no una unidad g/L.
- Efecto en el resumen: la media POST de hemoglobina (25,62) y su DE (37,07) están contaminadas por ese valor. Sin el 131, la media es **13,91** (n=9).
- **"182"**: ningún valor de hemoglobina vale 182. En el resumen aparece como p95 de la hemoglobina POST (182,34), que es imposible con un máximo de 131. Doc `08` (l. 54) dice "hemoglobina de 182 … error de captura": es un error de cita. El único "182" del laboratorio es LDH (UTMB-04, POST, 182,0, sin marca; y 992 IN_TEST, `182 (H)`, descartado).

### 3.4 Resumen por fase (`utmb_resumen_por_fase.csv`)

- **n, media y DE** de las 24 filas de laboratorio se reproducen desde el derivado. Esto es aritmética correcta, pero sobre un subconjunto de 10 sujetos y sin valores marcados.
- **p5/p95** no se reproducen en 23 de 24 filas. Ejemplos (publicado / calculado sobre el derivado / rango de datos):

| Analito y fase | p5 publicado | p95 publicado | Rango de datos | Problema |
|---|---|---|---|---|
| Hemoglobina POST | 11,91 | **182,34** | 12,0 – 131,0 | p95 fuera del rango; p5 bajo el mínimo |
| Glucosa PRE | 84,0 | **87,6** | 84,0 – 86,0 | p95 fuera del rango |
| Creatinina PRE | 0,70 | **1,35** | 0,7 – 1,3 | p95 fuera del rango |
| WBC POST | **3,24** | 9,4 | 4,0 – 9,2 | p5 bajo el mínimo |
| i-STAT Hemoglobina PRE | **10,38** | 16,49 | 12,2 – 16,3 | p5 bajo el mínimo |

Un método estándar (interpolación lineal o rango más cercano) no reproduce estos valores. Hay que volver a calcularlos con un método declarado.

### 3.5 PCR en UTMB: mg/L sin convertir

- En el origen, `C-reactive protein` aparece en **mg/dL** (32 filas, 9 sujetos: 224, 3768, 4023, 5788, 6345, 7127, 7352, 7772, 992) y en **mg/L**: 81 filas de `C-reactive protein` en los 21 sujetos omitidos, y 4 filas de `C-reactive protein, HS` en 5814 (todas con marca `(H)`). En total hay 85 filas en mg/L.
- El derivado solo conserva las 32 filas en mg/dL. Las 85 en mg/L no se convierten ni se incluyen (la conversión correcta sería ÷10). Por eso 5814 no tiene PCR en el derivado, aunque es uno de los 10 sujetos incluidos.
- Escalas: la mediana del grupo en mg/dL es 0,74 mg/dL (7,4 mg/L), y la del grupo en mg/L es 1,22 mg/L. Un cambio de unidad de la campaña es plausible, pero **no se puede verificar** sin la documentación de la campaña (x8). Antes de convertir, hay que confirmar la unidad de cada grupo.

---

## 4. Hallazgos en Inspiration4

### 4.1 Reproducción de las cifras de a1–a6 y b1–b6

Todas las cifras son reproducibles desde los archivos originales (ver tabla §1). Las diferencias son de redondeo:

- Neutrófilos: −24,5 % (el documento dice −25 %).
- Creatinina: la media baja de 1,135 a 1,028, pero C004 sube (1,13 → 1,15).
- Hemoglobina: la media 14,1 → 14,2 **requiere** incluir a C003 (sexo F, `HEMOGLOBIN (FEMALE)` en R+1). Sin esa fila, n=3 y la cifra cambia.

### 4.2 CBC de C003 en L-92: bloque internamente incoherente

Además de plaquetas 12,9 y neutrófilos absolutos 10,1 (marcados en la demo), la misma toma tiene:

| Campo | Valor | Comprobación | Lectura |
|---|---|---|---|
| Linfocitos absolutos | 6826 | = Neutrófilos % (71,1) × WBC (9,6) | Desplazado una categoría |
| Monocitos absolutos | 1997 | = Linfocitos % (20,8) × WBC (9,6) | Desplazado |
| Eosinófilos absolutos | 614 | = Monocitos % (6,4) × WBC (9,6) | Desplazado |
| Basófilos absolutos | 125 | = Eosinófilos % (1,3) × WBC (9,6) | Desplazado |
| Neutrófilos absolutos | 10,1 | No coincide con ningún porcentaje | Desplazado o erróneo |
| MPV | 330 fL | Fuera de rango (7,5–12,5) | Probablemente intercambiado con plaquetas |
| Plaquetas | 12,9 K/µL | Vs. 345 y 367 en L-44 y L-3 | Probablemente 330 (intercambio con MPV) |
| MCHC | 29,6 | = MCH calculada (Hb 13,2 / RBC 4,46 × 10) | El campo tiene el valor de MCH |
| RDW | 32,4 % | Fuera de rango (11–15) | Sospechoso |

El patrón indica que el bloque tiene el texto de columnas desplazado, no un error de transcripción aislado. **Recomendación:** no usar la toma C003 L-92 hasta confirmarla con Quest Diagnostics. Esta toma no afecta a a1–a6 (que usan L-3 y R+1).

### 4.3 CRP (c1–c3)

- Conversión: 1 pg/mL = 10^-7 mg/dL; por eso **÷10^7** es correcto. Ejemplo: C001 L-92, 18.385.000 pg/mL → 1,8385 mg/dL (18,4 mg/L).
- Unidad en origen: `pg/ml` en el SUBMITTED y en el TRANSFORMED. El documento 12 escribe `ng/ml` y propone "revisar"; hay que corregirlo.
- Plausibilidad: **no verificable**. Los valores van de 1,3 a 83,6 mg/L (mediana 12,3). Para adultos sanos son altos. C003 pasa de 42,8 (L-3) a 83,6 (R+1) y C001 de 18,4 (L-92) a 2,2 (L-44). Una oscilación así es poco compatible con un estado de salud estable y merece revisión.

### 4.4 Atípicos de la demo (f6, f8)

Los 6 marcados son reales. Pero la lista es incompleta: el bloque C003 L-92 (§4.2) tiene otras anomalías, y el criterio de marcado no está documentado (p. ej., glucosas de 56 (C004 L-3), 62 (C003 L-44) y 100 (C004 L-92) están fuera del rango 65–99 y no están marcadas).

---

## 5. Armonización de analitos (f)

| Grupo | Problema | Propuesta |
|---|---|---|
| Alfa-1, alfa-2, beta, gamma | Bajo el mismo código hay fracciones en g/dL y en % del total de proteínas | Separar en `alfa1_gdl` y `alfa1_pct`, etc. |
| ALT | `alt` (20) y `alanine_aminotransferase_alt` (15) | Unificar en `alt` (U/L) |
| BSAP | U/L y µg/L bajo el mismo código | Separar por unidad o convertir según el método (la nota de la campaña indica µg/L) |
| Tiroxina libre (T4) | `ng/cL` (32) y `ng/dL` (4). Las medianas son 1,25 y 1,28: misma magnitud | Corregir la unidad a `ng/dL` (ng/cL es una errata) |
| Creatinina y N-telopéptido en orina | `*_urinec` y `*_urine_c` son la misma prueba | Unificar |
| `albumin` (% SPE) vs `albumina` (g/dL) | Correctamente separados, pero con nombres muy parecidos | Renombrar `albumin` a `albumina_pct_spe` |

Unidades que sí son equivalentes (no son errores): `thou/mm3` = `Thousand/uL`; `mil/mm3` = `Million/uL`; `relative %` = `%`; `G/DL` = `g/dL`; `uIU/mL` = `ulU/mL` (errata); `mU/L` = `uIU/mL`.

---

## 6. Cobertura de PhenoAge en el derivado (e1–e3)

Fechas (sujeto, día) con las 9 entradas, por sujeto en `utmb_laboratorio.csv`:

| Sujeto (UTMB) | Fechas con las 9 / total | Entradas que faltan en alguna fecha |
|---|---|---|
| 224 (UTMB-01) | 0 / 4 | glucosa (4), albúmina (1) |
| 992 (UTMB-36) | 0 / 4 | glucosa (4), RDW (1), albúmina (1) |
| 3768 (UTMB-02) | 0 / 3 | glucosa (2), linfocitos % (3), RDW (3) |
| 4023 (UTMB-04) | 0 / 3 | glucosa (3), linfocitos % (2) |
| 5788 (UTMB-12) | 0 / 4 | glucosa (3), albúmina (1) |
| 5814 (UTMB-13) | 0 / 4 | **PCR (4)**, creatinina (1) |
| 6345 (UTMB-16) | 2 / 3 | glucosa (1) |
| 7127 (UTMB-19) | 2 / 3 | glucosa (1) |
| 7352 (UTMB-20) | 4 / 4 | — |
| 7772 (UTMB-21) | 3 / 4 | linfocitos % (1), RDW (1) |

Total: **11 de 36** fechas. Con el origen completo y la PCR en mg/L convertida, hay **114 de 117** fechas con las 9 entradas, en los 31 sujetos. La glucosa es la entrada que más falla en el derivado por el efecto de las marcas (§3.2).

Inspiration4: **27 de 28** combinaciones sujeto × tiempo tienen las 9 entradas (C002 R+194 sin MCV). Por tiempo: L-92 4/4, L-44 4/4, L-3 4/4, R+1 4/4, R+45 4/4, R+82 4/4, R+194 3/4.

---

## 7. Recomendaciones (no aplicadas; el auditor no modifica archivos)

1. Corregir el lector de cabeceras para aceptar `Parameter Name` y `ParameterName`, y regenerar `utmb_laboratorio.csv`. Esperar unas 6.800 filas sin marca, no 2.010.
2. Conservar los valores marcados con una columna de marca (`H`, `L`, `A`…) en lugar de descartarlos. Mantenerlos en los resúmenes con un indicador.
3. Corregir la hemoglobina 131 a 13,1 (g/dL) con una marca de corrección y recalcular el resumen. Corregir en `08` (l. 54) "182" por "131 (13,1 g/dL)".
4. Recalcular los percentiles con un método declarado. Mientras tanto, no publicar p5/p95.
5. Convertir la PCR de UTMB en mg/L ÷10 y conservar la unidad original. Confirmar antes la unidad de cada campaña.
6. Corregir la unidad de CRP en `12` (`ng/ml` → `pg/ml`) y revisar la plausibilidad con el laboratorio.
7. Corregir la armonización de §5: alfa/beta/gamma, ALT, BSAP, tiroxina y nombres de orina.
8. Corregir `03` (l. "23 analitos" → 20) y la interpretación del C003 L-92. Excluir esa toma hasta confirmarla.
9. Corregir `demo/LEEME.md`: "Junta todos los datos reales" y la cobertura de laboratorio (31 sujetos en el origen).
10. Documentar el criterio de `atipico`.

---

## 8. Código de comprobación (fragmentos)

Detección de la variante de cabecera y del conjunto de sujetos:

```python
rows = [r for f in files for r in csv.DictReader(open(f, newline="", encoding="utf-8-sig"))]
name = r.get("Parameter Name", r.get("ParameterName"))   # 21 archivos usan la segunda variante
```

Valores marcados (solo números puros pasan el filtro del derivado):

```python
PURE = re.compile(r"^\s*[-+]?\d+(\.\d+)?\s*$")
flagged = [r for r in rows if re.match(r"^\s*[-+]?\d+(\.\d+)?", r["Measured_Value"]) and not PURE.match(r["Measured_Value"])]
# 280 en los 10 sujetos incluidos, p. ej. "63  (L)", "182  (H)"
```

Conversión CRP y comprobación de hemoglobina:

```python
mgdl = pg_per_ml / 1e7            # 1 pg/mL = 1e-7 mg/dL
hb_from_mchc = mchc * hct / 100   # 33 * 39.8 / 100 = 13.1 g/dL
hb_from_mch  = mch * rbc / 10     # 29 * 4.55 / 10  = 13.2 g/dL
```

Reconciliación de Inspiration4 (CBC, CMP, Eve), por tipo de prueba: 1.112 filas de origen → 1.090 en la demo + 22 `NA` omitidos; 0 diferencias en valores.

---

## 9. Limitaciones

- No se tiene acceso a la documentación de la campaña de UTMB (unidades de CRP, criterios de marca, método de fechas de inicio). Por eso c2, x6 y x8 son **NO VERIFICABLE**.
- Las cifras de cambio de Inspiration4 son de n=4 (3 con la hemoglobina de C003 incluida).
- Los rangos de referencia son los del origen (no se han comparado con otras referencias).
- Los documentos `10` y `08` (descripción de la cobertura) se citan solo donde afectan a las cifras verificadas. Doc `10` indica que el CBC de Inspiration4 no tiene las 9 entradas: es correcto para `osdr-inspiration4-clinico.csv`, pero la demo sí las tiene con el CMP y la PCR (ver e1).
