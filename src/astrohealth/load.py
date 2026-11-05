"""Funciones de carga con tipos correctos. Úsalas en notebooks y scripts en lugar de leer los CSV a mano."""
import pandas as pd

from astrohealth.config import COLUMNAS_SIMULADAS, FASES, PROCESSED

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
