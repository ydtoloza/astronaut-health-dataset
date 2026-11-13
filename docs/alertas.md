# Motor de alertas (`src/astrohealth/alertas.py`)

Convierte el diario y los síntomas reportados en alertas **verde / amarillo / rojo**, con la acción sugerida y la fuente de cada umbral. **No es un dispositivo médico**: los umbrales son una propuesta de diseño para el hackathon.

## Dos capas
1. **Umbral absoluto** (seguridad clínica) → "avisar al médico de vuelo".
2. **Desvío de la línea base personal** (|z| ≥ 2 amarillo, ≥ 3 rojo) → "algo cambió en ti".

Hacen falta las dos: en UTMB hay 109 días con pulso < 50 lpm en personas sanas. Un umbral fijo solo genera falsas alarmas; el desvío personal las filtra.

## Uso
```python
from astrohealth import cargar_diario, cargar_lineas_base, evaluar, estado_del_dia, evaluar_sintoma, dosis_radiacion
a = evaluar(cargar_diario(), cargar_lineas_base())   # una fila por alerta
estado_del_dia(a)                                     # peor nivel por condición: colorea la figura humana
evaluar_sintoma("zoster")                             # síntoma elegido por el astronauta
dosis_radiacion(28)                                   # % del límite de carrera de 600 mSv
```
Resumen en consola: `make alertas` (Windows: `$env:PYTHONPATH="src"; python -m astrohealth.alertas`).

## Reglas numéricas

| Condición | Regla | 🟡 | 🔴 | Fuente | Verificada |
|---|---|---|---|---|---|
| Cardiovascular | PA sistólica | ≥ 140 | ≥ 180 | AHA/ACC 2017 | No (guía) |
| | PA diastólica | ≥ 90 | ≥ 120 | AHA/ACC 2017 | No (guía) |
| | PA sistólica baja | ≤ 90 | — | Criterio clínico | No |
| | Pulso alto | ≥ 100 | ≥ 120 | Criterio clínico | No |
| | Pulso bajo | ≤ 50 | ≤ 40 | Criterio clínico | No |
| Inmune | Temperatura | ≥ 37,8 °C | ≥ 38,0 °C | Criterio clínico | No |
| | Hipotermia | — | < 35 °C | Criterio clínico | No |
| | Frecuencia respiratoria | > 20 | ≥ 24 | Criterio clínico | No |
| | SpO₂ (simulada) | < 95 % | < 92 % | Criterio clínico | No |
| Personal | z de pulso, PAS, PAD, temperatura | \|z\| ≥ 2 | \|z\| ≥ 3 | Diseño del equipo | — |
| Nutrición | Pérdida de peso frente a la línea base | ≥ 3 % | ≥ 5 % | GLIM (criterio clínico) | No |
| Conductual | Sueño, media de 7 noches | < 6,0 h | < 5,5 h | Barger 2014 (ISS 6,09 h); cortes del equipo | Sí (la cifra) |
| | Ánimo (simulado), z frente a la fase previa | ≤ −2 | — | Diseño del equipo | — |
| **Radiación** | **Dosis acumulada / límite de carrera 600 mSv** | ≥ 50 % | ≥ 100 % | NASA HRP radiation_cancer_2026 p43; cortes del equipo | Sí (600 mSv) |

## Síntomas (catálogo `SINTOMAS`)

| Condición | Síntoma | Nivel | Fuente |
|---|---|---|---|
| Cardiovascular | Dolor de pecho, desmayo | 🔴 | Criterio clínico; intolerancia ortostática (HRP) |
| | Palpitaciones | 🟡 | Criterio clínico |
| | **Hinchazón o dolor en el cuello, la cara o un brazo (posible trombosis venosa)** | 🔴 | [NASA HRP Venous Haemostasis](https://www.nasa.gov/reference/venous-haemostasis/) |
| **Inmune (reactivación viral)** | **Herpes labial, zóster, sarpullido** | 🟡 | [NASA HRP Immune Biomarkers](https://www.nasa.gov/reference/immune-biomarkers/) |
| | Escalofríos | 🟡 | Criterio clínico |
| SANS | Visión borrosa, presión detrás de los ojos | 🟡 | HRP SANS (~70 % con algún signo) |
| | Pérdida brusca de visión | 🔴 | HRP SANS |
| Renal | Dolor de flanco, sangre en la orina | 🔴 | HRP renal_2024 |
| Óseo | Dolor óseo tras un golpe o carga | 🔴 | HRP bone_fracture_2024 |
| Conductual | Pensamientos de hacerse daño | 🔴 | PHQ-9 pregunta 9 |
| Comunes en UTMB | Dolor de cabeza, insomnio, estreñimiento, dolor de espalda | 🟢 registro | UTMB (eventos) |
| | Mareo | 🟡 | UTMB (eventos) |

En la pantalla de radiación se muestra como dato educativo que los neutrones aportan ~30 % de la radiación total en la ISS ([CSA, 2026](https://www.asc-csa.gc.ca/eng/news/articles/2026/2026-02-26-monitoring-radiation-astronaut-health.asp)).

## Resultado sobre el dataset (`make alertas`)
1.920 alertas en 30 astronautas. Las más frecuentes son de desvío personal y de pérdida de peso, que es esperable en reposo en cama. La radiación simulada (máx. 36,8 mSv) no llega al 50 % del límite, y ninguna media de sueño baja de 6 h.

## Antes de presentar
- Citar las guías marcadas "No (guía)": AHA/ACC 2017, ADA, GLIM, PHQ-9. No se verificaron en la auditoría.
- Los cortes amarillos son decisiones de diseño, no cifras de una fuente.
- Pendiente: medir cuántos de los 1.053 síntomas reales de UTMB anticipan las alertas (notebook `02-alertas`).
