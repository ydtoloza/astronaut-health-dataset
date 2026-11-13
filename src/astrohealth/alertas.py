"""Motor de alertas: convierte el diario y los síntomas reportados en alertas verde/amarillo/rojo.

Dos capas:
1. Umbral absoluto (seguridad clínica): "avisar al médico de vuelo".
2. Desvío de la línea base personal (z-score): "algo cambió en ti".

Las reglas son datos (REGLAS, SINTOMAS): se editan sin tocar el código. Cada regla lleva su fuente y
si la cifra se verificó en la auditoría (`verificado=True`) o es una guía clínica general / decisión de
diseño del equipo que hay que citar antes de presentar (`verificado=False`). Detalle en docs/alertas.md.

No es un dispositivo médico.
"""
import pandas as pd

ORDEN = {"verde": 0, "amarillo": 1, "rojo": 2}
LIMITE_CARRERA_MSV = 600  # NASA HRP, radiation_cancer_2026.pdf p43 (verificado)

# --- Reglas numéricas -------------------------------------------------------------------------------
# tipo: "mayor" (valor >= umbral), "menor" (valor <= umbral), "z_abs" (|z| >= umbral),
#       "z_menor" (z <= -umbral), "perdida_pct" (pérdida % frente a la línea base >= umbral),
#       "pct_limite" (% del límite de carrera >= umbral).
REGLAS = [
    # Cardiovascular
    dict(id="pa_alta", condicion="cardiovascular", columna="pas_mmhg", tipo="mayor", amarillo=140, rojo=180,
         accion="Repetir en reposo en 5 min; si sigue, avisar al médico de vuelo",
         fuente="AHA/ACC 2017 (guía clínica)", verificado=False),
    dict(id="pad_alta", condicion="cardiovascular", columna="pad_mmhg", tipo="mayor", amarillo=90, rojo=120,
         accion="Repetir en reposo en 5 min; si sigue, avisar al médico de vuelo",
         fuente="AHA/ACC 2017 (guía clínica)", verificado=False),
    dict(id="pa_baja", condicion="cardiovascular", columna="pas_mmhg", tipo="menor", amarillo=90, rojo=None,
         accion="Hidratarse; si hay mareo o desmayo, avisar al médico de vuelo",
         fuente="Criterio clínico general", verificado=False),
    dict(id="pulso_alto", condicion="cardiovascular", columna="pulso_lpm", tipo="mayor", amarillo=100, rojo=120,
         accion="Medir de nuevo tras 5 min sentado; si hay dolor de pecho, avisar ya",
         fuente="Criterio clínico general (taquicardia)", verificado=False),
    dict(id="pulso_bajo", condicion="cardiovascular", columna="pulso_lpm", tipo="menor", amarillo=50, rojo=40,
         accion="Normal en personas entrenadas; avisar si hay mareo o fatiga",
         fuente="Criterio clínico general (bradicardia)", verificado=False),
    # Inmune / infección
    dict(id="fiebre", condicion="inmune", columna="temp_c", tipo="mayor", amarillo=37.8, rojo=38.0,
         accion="Registrar síntomas, hidratarse y avisar al médico de vuelo si llega a 38 °C",
         fuente="Criterio clínico general (fiebre ≥ 38,0 °C)", verificado=False),
    dict(id="hipotermia", condicion="inmune", columna="temp_c", tipo="menor", amarillo=None, rojo=34.9,
         accion="Avisar al médico de vuelo", fuente="Criterio clínico general", verificado=False),
    dict(id="resp_alta", condicion="inmune", columna="resp_rpm", tipo="mayor", amarillo=21, rojo=24,
         accion="Medir SpO₂; si hay falta de aire, avisar al médico de vuelo",
         fuente="Criterio clínico general (FR > 20)", verificado=False),
    dict(id="spo2_baja", condicion="inmune", columna="spo2_pct_sim", tipo="menor", amarillo=94, rojo=91,
         accion="Revisar el sensor y repetir; si sigue baja, avisar al médico de vuelo",
         fuente="Criterio clínico general (SpO₂ < 95 % / < 92 %)", verificado=False),
    # Desvío personal (las 4 vitales del semáforo)
    *[dict(id=f"desvio_{c}", condicion="personal", columna=f"z_{c}", tipo="z_abs", amarillo=2, rojo=3,
           accion="Valor fuera de tu rango habitual: repetir la medición y revisar síntomas",
           fuente="Diseño del equipo: z frente a la línea base personal", verificado=False)
      for c in ("pulso_lpm", "pas_mmhg", "pad_mmhg", "temp_c")],
    # Nutrición
    dict(id="perdida_peso", condicion="nutricion", columna="peso_kg", tipo="perdida_pct", amarillo=3, rojo=5,
         accion="Revisar ingesta frente a lo prescrito; avisar al médico de vuelo si pasa del 5 %",
         fuente="Criterio clínico general (pérdida > 5 %, GLIM)", verificado=False),
    # Conductual y sueño
    dict(id="sueno_corto", condicion="conductual", columna="sueno_h_media7", tipo="menor", amarillo=6.0, rojo=5.5,
         accion="Proteger el horario de sueño; evitar tareas críticas sin descanso",
         fuente="Barger 2014 (ISS 6,09 h/noche); cortes = decisión del equipo", verificado=True),
    dict(id="animo_bajo", condicion="conductual", columna="z_animo_0a10_sim", tipo="z_menor", amarillo=2, rojo=None,
         accion="Completar PHQ-9 y hablar con el equipo de apoyo psicológico",
         fuente="Diseño del equipo (ánimo simulado)", verificado=False),
    # Radiación
    dict(id="radiacion_acumulada", condicion="radiacion", columna="radiacion_msv_acum_sim", tipo="pct_limite",
         amarillo=50, rojo=100,
         accion="Revisar dosis con el equipo de radiación; refugiarse si hay aviso de evento solar",
         fuente="Límite de carrera 600 mSv (NASA HRP, radiation_cancer_2026 p43); cortes = decisión del equipo",
         verificado=True),
]

# --- Síntomas reportados por el astronauta -------------------------------------------------------------
SINTOMAS = {
    # Cardiovascular
    "dolor_pecho": ("cardiovascular", "rojo", "Dolor u opresión en el pecho", "Avisar ya al médico de vuelo",
                    "Criterio clínico general"),
    "desmayo": ("cardiovascular", "rojo", "Desmayo o casi desmayo", "Acostarse, avisar al médico de vuelo",
                "Criterio clínico general; intolerancia ortostática (HRP cardio_2023 p25)"),
    "palpitaciones": ("cardiovascular", "amarillo", "Palpitaciones o pulso irregular", "Medir pulso y PA; registrar",
                      "Criterio clínico general"),
    "hinchazon_cuello_cara_brazo": ("cardiovascular", "rojo",
                                    "Hinchazón o dolor en el cuello, la cara o un brazo (posible trombosis venosa)",
                                    "Avisar ya al médico de vuelo; ecografía guiada si está disponible",
                                    "Riesgo: NASA HRP Venous Haemostasis; síntomas: criterio clínico general"),
    # Inmune: reactivación viral
    "herpes_labial": ("inmune", "amarillo", "Ampollas o llagas en el labio (reactivación viral)",
                      "Registrar y avisar en el próximo contacto médico",
                      "NASA HRP Immune Biomarkers (reactivación de virus latentes)"),
    "zoster": ("inmune", "amarillo", "Erupción dolorosa en franja de un lado del cuerpo (posible zóster)",
               "Avisar al médico de vuelo en el día",
               "NASA HRP Immune Biomarkers (virus del zóster)"),
    "sarpullido": ("inmune", "amarillo", "Sarpullido o erupción en la piel", "Registrar con foto; avisar si se extiende",
                   "NASA HRP Immune Biomarkers; criterio clínico general"),
    "fiebre_escalofrios": ("inmune", "amarillo", "Escalofríos o sensación de fiebre", "Medir temperatura",
                           "Criterio clínico general"),
    # SANS (ojo)
    "vision_borrosa": ("sans", "amarillo", "Visión borrosa de cerca o de lejos", "Hacer la autoevaluación de visión",
                       "NASA HRP SANS (~70 % con algún signo, sans_2022 p7)"),
    "presion_ojos": ("sans", "amarillo", "Presión detrás de los ojos", "Hacer la autoevaluación de visión",
                     "NASA HRP SANS"),
    "perdida_vision": ("sans", "rojo", "Pérdida o cambio brusco de la visión", "Avisar ya al médico de vuelo",
                       "NASA HRP SANS"),
    # Renal, óseo, conductual
    "dolor_flanco": ("renal", "rojo", "Dolor en el costado o la espalda baja que va hacia la ingle",
                     "Avisar al médico de vuelo; aumentar agua",
                     "NASA HRP renal_2024 (sobresaturación +115–150 %)"),
    "sangre_orina": ("renal", "rojo", "Sangre en la orina", "Avisar al médico de vuelo", "NASA HRP renal_2024"),
    "dolor_oseo_impacto": ("oseo", "rojo", "Dolor en un hueso después de un golpe o carga",
                           "Inmovilizar y avisar al médico de vuelo",
                           "NASA HRP bone_fracture_2024 (pérdida 1–1,5 %/mes)"),
    "ideas_danarse": ("conductual", "rojo", "Pensamientos de hacerse daño", "Hablar ya con el médico o el psicólogo",
                      "PHQ-9 pregunta 9 (criterio clínico general)"),
    # Frecuentes en UTMB (registro; amarillo si persisten)
    "dolor_cabeza": ("comun", "verde", "Dolor de cabeza", "Registrar intensidad 0–10", "UTMB: 231 eventos"),
    "dificultad_dormir": ("conductual", "verde", "Dificultad para dormir", "Registrar", "UTMB: 86 eventos"),
    "estrenimiento": ("nutricion", "verde", "Estreñimiento", "Más agua y fibra", "UTMB: 41 eventos"),
    "dolor_espalda": ("comun", "verde", "Dolor de espalda", "Estiramientos; registrar", "UTMB: 29 eventos"),
    "mareo": ("comun", "amarillo", "Mareo", "Sentarse; medir PA y pulso", "UTMB: 20 eventos"),
}


def _nivel(valor, regla):
    """Nivel ("verde"/"amarillo"/"rojo") de un valor según una regla. NaN → None (sin dato)."""
    if valor is None or pd.isna(valor):
        return None
    t, am, ro = regla["tipo"], regla["amarillo"], regla["rojo"]
    if t in ("mayor", "perdida_pct", "pct_limite"):
        cmp = lambda u: u is not None and valor >= u
    elif t == "menor":
        cmp = lambda u: u is not None and valor <= u
    elif t == "z_abs":
        cmp = lambda u: u is not None and abs(valor) >= u
    elif t == "z_menor":
        cmp = lambda u: u is not None and valor <= -u
    else:
        raise ValueError(f"tipo de regla desconocido: {t}")
    return "rojo" if cmp(ro) else ("amarillo" if cmp(am) else "verde")


def preparar(diario: pd.DataFrame, lineas_base: pd.DataFrame) -> pd.DataFrame:
    """Agrega las columnas derivadas que usan las reglas (media de sueño, pérdida de peso, % del límite...)."""
    d = diario.sort_values(["astronauta_id", "fecha"]).copy()
    d["sueno_h_media7"] = (d.groupby("astronauta_id")["sueno_h"]
                           .transform(lambda s: s.rolling(7, min_periods=4).mean()))
    base = lineas_base.set_index("astronauta_id")["peso_kg_media"]
    d["peso_kg_perdida_pct"] = (1 - d["peso_kg"] / d["astronauta_id"].map(base)) * 100
    d["radiacion_pct_limite"] = d["radiacion_msv_acum_sim"] / LIMITE_CARRERA_MSV * 100
    if "animo_0a10_sim" in d.columns:
        pre = d[d["fase"] == "pre"].groupby("astronauta_id")["animo_0a10_sim"].agg(["mean", "std"])
        m, s = d["astronauta_id"].map(pre["mean"]), d["astronauta_id"].map(pre["std"].clip(lower=0.5))
        d["z_animo_0a10_sim"] = (d["animo_0a10_sim"] - m) / s
    return d


def _columna_valor(regla):
    return {"perdida_pct": "peso_kg_perdida_pct", "pct_limite": "radiacion_pct_limite"}.get(regla["tipo"],
                                                                                             regla["columna"])


def evaluar(diario: pd.DataFrame, lineas_base: pd.DataFrame, reglas=REGLAS) -> pd.DataFrame:
    """Una fila por alerta (amarillo o rojo) con astronauta, fecha, regla, valor, nivel, acción y fuente."""
    d = preparar(diario, lineas_base)
    filas = []
    for r in reglas:
        col = _columna_valor(r)
        if col not in d.columns:
            continue
        niv = d[col].map(lambda v: _nivel(v, r))
        hit = d[niv.isin(["amarillo", "rojo"])]
        for (_, x), n in zip(hit.iterrows(), niv[hit.index]):
            filas.append(dict(astronauta_id=x["astronauta_id"], fecha=x["fecha"], fase=x["fase"],
                              dia_mision=x.get("dia_mision"), regla=r["id"], condicion=r["condicion"],
                              valor=round(float(x[col]), 2), nivel=n, accion=r["accion"], fuente=r["fuente"],
                              verificado=r["verificado"]))
    cols = ["astronauta_id", "fecha", "fase", "dia_mision", "regla", "condicion", "valor", "nivel", "accion",
            "fuente", "verificado"]
    return pd.DataFrame(filas, columns=cols).sort_values(["astronauta_id", "fecha", "regla"], ignore_index=True)


def estado_del_dia(alertas: pd.DataFrame) -> pd.DataFrame:
    """Peor nivel por astronauta, día y condición (para colorear la figura humana)."""
    if alertas.empty:
        return alertas
    a = alertas.assign(_o=alertas["nivel"].map(ORDEN))
    return (a.sort_values("_o").groupby(["astronauta_id", "fecha", "condicion"], as_index=False).last()
            .drop(columns="_o"))


def evaluar_sintoma(clave: str) -> dict:
    """Nivel, condición, acción y fuente de un síntoma del catálogo SINTOMAS."""
    if clave not in SINTOMAS:
        raise KeyError(f"Síntoma desconocido: {clave}. Opciones: {', '.join(SINTOMAS)}")
    condicion, nivel, texto, accion, fuente = SINTOMAS[clave]
    return dict(sintoma=clave, texto=texto, condicion=condicion, nivel=nivel, accion=accion, fuente=fuente)


def dosis_radiacion(acumulada_msv: float) -> dict:
    """Dosis acumulada frente al límite de carrera de NASA (600 mSv)."""
    pct = acumulada_msv / LIMITE_CARRERA_MSV * 100
    regla = next(r for r in REGLAS if r["id"] == "radiacion_acumulada")
    return dict(acumulada_msv=acumulada_msv, limite_msv=LIMITE_CARRERA_MSV, pct_limite=round(pct, 1),
                nivel=_nivel(pct, regla),
                nota="Dato educativo: los neutrones aportan ~30 % de la radiación total en la ISS (CSA, 2026).")


def main():
    from astrohealth.load import cargar_diario, cargar_lineas_base
    a = evaluar(cargar_diario(), cargar_lineas_base())
    print(f"{len(a)} alertas en {a['astronauta_id'].nunique()} astronautas\n")
    print(a.groupby(["condicion", "regla", "nivel"]).size().unstack(fill_value=0).to_string())


if __name__ == "__main__":
    main()
