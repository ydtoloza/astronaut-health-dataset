# Inspiration4: panel metabólico (OSD-575) y viabilidad de PhenoAge — verificado por el coordinador

## Datos descargados
- `osdr-raw/osd-575/CMP.csv`: panel metabólico completo (CMP) de los 4 tripulantes de Inspiration4, con 7 tomas entre 92 días antes del vuelo y 194 días después. Son 531 filas con su rango de referencia.
  Fuente: NASA OSDR, OSD-575 (https://osdr.nasa.gov/bio/repo/data/studies/OSD-575). Descarga directa vía `https://osdr.nasa.gov/geode-py/ws/studies/OSD-575/download?source=datamanager&file=LSDS-8_Comprehensive_Metabolic_Panel_CMP.upload_SUBMITTED.csv`, con `curl -L` porque redirige a S3.
- `osdr-raw/osd-575/cardio_eve.csv`: panel cardiovascular sérico (Eve Technologies), que **incluye PCR (CRP)**.
- Analitos del CMP: glucosa, albúmina, creatinina, fosfatasa alcalina, BUN, calcio, sodio, potasio, cloro, CO₂, ALT, AST, bilirrubina, proteínas totales, globulina y TFGe.

## Resultados (n=4; 3 días antes del vuelo → día siguiente al aterrizaje)
| Analito | Antes | Después | Nota |
|---|---|---|---|
| Glucosa (mg/dL) | 69,5 (56–78) | **93,3 (83–103)** | Sube en los 4 tripulantes |
| Creatinina (mg/dL) | 1,14 | 1,03 | |
| Fosfatasa alcalina (U/L) | 49,8 | 56,5 | Sube en los 4 |
| Calcio (mg/dL) | 9,65 | 9,53 | |
| Albúmina (g/dL) | 4,2–4,9 | 4,2–4,9 | Estable. El archivo también trae el cociente albúmina/globulina; no confundirlos |

⚠️ En la toma de 45 días después, 3 de las 4 glucosas son 36–44 mg/dL. Es probable que sea un artefacto de la muestra (glucólisis por demora en procesarla) y no hipoglucemia real. No usar sin revisar.

## PhenoAge (Levine 2018): entradas disponibles
| Entrada | UTMB (reposo en cama, 31 sujetos; 98 de 105 sujeto-fechas con las 9) | Inspiration4 (vuelo real, 4 sujetos; 23 de 28 sujeto-fechas con las 9) |
|---|---|---|
| Albúmina | ✅ | ✅ OSD-575 CMP |
| Creatinina | ✅ | ✅ OSD-575 CMP |
| Glucosa | ✅ | ✅ OSD-575 CMP |
| PCR | ✅ | ✅ OSD-575, panel cardiovascular Eve (origen en **pg/ml**; mg/dL = pg/ml ÷ 10⁷. Corregido: antes decía ng/ml, lo que habría dado un error de 1.000 veces) |
| % de linfocitos | ✅ (relative %) | ✅ OSD-569 CBC |
| VCM | ✅ | ✅ OSD-569 CBC |
| RDW | ✅ | ✅ OSD-569 CBC |
| Fosfatasa alcalina | ✅ | ✅ OSD-575 CMP |
| Leucocitos | ✅ | ✅ OSD-569 CBC |
| **Edad** | ❌ no está en los archivos públicos | ❌ IDs anonimizados |

**Conclusión:** PhenoAge se puede calcular en **ambas** fuentes si se usa una edad supuesta, por ejemplo la media de la cohorte. En la app conviene mostrar el **cambio de edad fenotípica** respecto de la línea base personal, no el valor absoluto. Antes de programar la fórmula, copiar los coeficientes del artículo original (Levine et al. 2018, *Aging*, doi:10.18632/aging.101414). **Verificación (verificacion/05-literatura.md):** los pesos de las 9 variables y de la edad están en la Tabla 1 del artículo, pero el intercepto y los parámetros de Gompertz están solo en el Suplemento 2, Tabla S6, que no se pudo consultar. No programar la fórmula con constantes de memoria.
