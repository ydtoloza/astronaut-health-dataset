"""Funciones de carga con tipos correctos. Úsalas en notebooks y scripts en lugar de leer los CSV a mano."""
import pandas as pd

from astrohealth.config import COLUMNAS_SIMULADAS, EXTERNAL_HERA, EXTERNAL_IMM, FASES, PROCESSED

_FASE = pd.CategoricalDtype(FASES, ordered=True)


def _leer(nombre, **kw):
    ruta = PROCESSED / nombre
    if not ruta.exists():
        raise FileNotFoundError(f"No existe {ruta}. Ejecuta `make data` para generarlo.")
    return pd.read_csv(ruta, **kw)


def cargar_astronautas() -> pd.DataFrame:
    """Un perfil por astronauta (40 UTMB + 4 Inspiration4) con los tipos de datos disponibles."""
    return _leer("demo_astronautas.csv")


def cargar_diario(incluir_simulados: bool = True) -> pd.DataFrame:
    """Una fila por astronauta y día (solo UTMB). `incluir_simulados=False` quita las columnas *_sim."""
    d = _leer("demo_diario.csv", parse_dates=["fecha"])
    d["fase"] = d["fase"].astype(_FASE)
    d["estado_vitales"] = d["estado_vitales"].astype(
        pd.CategoricalDtype(["verde", "amarillo", "rojo"], ordered=True))
    if not incluir_simulados:
        d = d.drop(columns=[c for c in COLUMNAS_SIMULADAS if c in d.columns])
    return d


def cargar_laboratorio(excluir_atipicos: bool = True) -> pd.DataFrame:
    """Análisis de sangre y orina de UTMB e Inspiration4 en formato largo (una fila por valor)."""
    lab = _leer("demo_laboratorio.csv", parse_dates=["fecha"], low_memory=False)
    lab["fase"] = lab["fase"].astype(_FASE)
    if excluir_atipicos:
        lab = lab[lab["atipico"].isna()]
    return lab


def cargar_eventos() -> pd.DataFrame:
    """Síntomas reportados con acción, intervención y resultado (UTMB)."""
    e = _leer("demo_eventos.csv", parse_dates=["fecha"])
    e["fase"] = e["fase"].astype(_FASE)
    return e


def cargar_lineas_base() -> pd.DataFrame:
    """Media y desviación de la línea base personal de cada astronauta UTMB."""
    return _leer("demo_lineas_base.csv")


def cargar_todo() -> dict:
    """Todas las tablas en un diccionario."""
    return {"astronautas": cargar_astronautas(), "diario": cargar_diario(), "laboratorio": cargar_laboratorio(),
            "eventos": cargar_eventos(), "lineas_base": cargar_lineas_base()}


def serie_astronauta(astronauta_id: str, columnas=None) -> pd.DataFrame:
    """Serie diaria de un astronauta ordenada por día de misión."""
    d = cargar_diario()
    d = d[d["astronauta_id"] == astronauta_id].sort_values("dia_mision")
    base = ["astronauta_id", "fecha", "fase", "dia_mision"]
    return d[base + list(columnas)] if columnas else d


def laboratorio_ancho(lab: pd.DataFrame, analitos) -> pd.DataFrame:
    """Pasa el laboratorio a formato ancho: una fila por astronauta y toma, una columna por analito."""
    sub = lab[lab["analito"].isin(analitos)].copy()
    # toma = fecha real (UTMB) o día relativo al vuelo (Inspiration4, sin fechas)
    sub["toma"] = sub["fecha"].dt.strftime("%Y-%m-%d").fillna("dia " + sub["dia_relativo"].astype("Int64").astype(str))
    sub["origen"] = sub["fuente"].str.split().str[0]   # UTMB | Inspiration4 (une OSD-569 y OSD-575)
    return (sub.pivot_table(index=["origen", "astronauta_id", "fase", "toma"], columns="analito",
                            values="valor", aggfunc="mean", observed=True)
            .reset_index())


def cargar_imm_probabilidades() -> pd.DataFrame:
    """IMM (NASA): probabilidad de al menos un evento por condición (98), misión de referencia y sexo.

    Fuente: "Ranking of Medical Conditions by Probability" (iMED v5.0, 2015), data/external/imm/.
    `prob_es_cota_inferior=True` significa que el PDF dice ">9.99E-01".
    """
    return pd.read_csv(EXTERNAL_IMM / "imm_probabilidades.csv")


def cargar_imm_resultados() -> pd.DataFrame:
    """IMM (NASA): eventos totales (TME), Crew Health Index (CHI), P(evacuación) y P(muerte) por duración.

    Fuente: "Medical Risk Based on Mission Duration" (S-20180531-405, 2018), data/external/imm/.
    """
    return pd.read_csv(EXTERNAL_IMM / "imm_resultados_por_duracion.csv")


def cargar_artemis1_dosis() -> pd.DataFrame:
    """Artemis I: tasa de dosis absorbida (µGy/min) por sensor (HERA HSU1/HSU2 cada 1 min, M-42 y EAD cada 5 min).

    Fuente: George et al. 2024, Nature 634:48 (CC BY 4.0), data/external/hera_artemis1/.
    """
    return pd.read_csv(EXTERNAL_HERA / "artemis1_tasa_dosis.csv.gz", parse_dates=["tiempo_utc"])


def cargar_artemis1_cad() -> pd.DataFrame:
    """Artemis I: dosis acumulada (mGy) del Crew Active Dosimeter CAD SN82."""
    return pd.read_csv(EXTERNAL_HERA / "artemis1_cad_acumulada.csv", parse_dates=["tiempo_utc"])
