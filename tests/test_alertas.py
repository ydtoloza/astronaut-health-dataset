"""Tests del motor de alertas (src/astrohealth/alertas.py)."""
import pandas as pd
import pytest

from astrohealth.alertas import (LIMITE_CARRERA_MSV, REGLAS, SINTOMAS, _nivel, dosis_radiacion, estado_del_dia,
                                 evaluar, evaluar_sintoma)
from astrohealth.load import cargar_diario, cargar_lineas_base

REGLA = {r["id"]: r for r in REGLAS}


@pytest.fixture(scope="module")
def alertas():
    return evaluar(cargar_diario(), cargar_lineas_base())


@pytest.mark.parametrize("regla,valor,esperado", [
    ("pa_alta", 120, "verde"), ("pa_alta", 140, "amarillo"), ("pa_alta", 185, "rojo"),
    ("fiebre", 37.0, "verde"), ("fiebre", 37.8, "amarillo"), ("fiebre", 38.0, "rojo"),
    ("pulso_bajo", 55, "verde"), ("pulso_bajo", 48, "amarillo"), ("pulso_bajo", 38, "rojo"),
    ("desvio_pulso_lpm", -2.5, "amarillo"), ("desvio_pulso_lpm", 3.1, "rojo"),
    ("radiacion_acumulada", 49, "verde"), ("radiacion_acumulada", 50, "amarillo"), ("radiacion_acumulada", 100, "rojo"),
])
def test_umbrales(regla, valor, esperado):
    assert _nivel(valor, REGLA[regla]) == esperado


def test_sin_dato_no_alerta():
    assert _nivel(float("nan"), REGLA["pa_alta"]) is None


def test_reglas_bien_formadas():
    ids = [r["id"] for r in REGLAS]
    assert len(ids) == len(set(ids))
    for r in REGLAS:
        assert r["fuente"] and r["accion"] and isinstance(r["verificado"], bool), r["id"]
        assert r["amarillo"] is not None or r["rojo"] is not None, r["id"]


def test_ajustes_recursos_oficiales():
    # Reactivación viral (NASA HRP Immune Biomarkers)
    for s in ("herpes_labial", "zoster", "sarpullido"):
        assert evaluar_sintoma(s)["condicion"] == "inmune"
        assert "Immune Biomarkers" in evaluar_sintoma(s)["fuente"]
    # Posible trombosis venosa → rojo (NASA HRP Venous Haemostasis)
    t = evaluar_sintoma("hinchazon_cuello_cara_brazo")
    assert t["nivel"] == "rojo" and "Venous Haemostasis" in t["fuente"]
    # Radiación frente al límite de carrera de 600 mSv
    assert LIMITE_CARRERA_MSV == 600
    assert dosis_radiacion(300)["pct_limite"] == 50.0 and dosis_radiacion(300)["nivel"] == "amarillo"
    assert "30 %" in dosis_radiacion(10)["nota"]


def test_sintoma_desconocido():
    with pytest.raises(KeyError):
        evaluar_sintoma("no_existe")


def test_catalogo_sintomas_niveles_validos():
    assert all(v[1] in {"verde", "amarillo", "rojo"} for v in SINTOMAS.values())


def test_alertas_sobre_dataset(alertas):
    assert len(alertas) > 0
    assert set(alertas["nivel"]) <= {"amarillo", "rojo"}
    assert not alertas.duplicated(["astronauta_id", "fecha", "regla"]).any()
    # Radiación simulada (máx. ~37 mSv) no llega al 50 % del límite
    assert "radiacion_acumulada" not in set(alertas["regla"])


def test_estado_del_dia_un_nivel_por_condicion(alertas):
    e = estado_del_dia(alertas)
    assert not e.duplicated(["astronauta_id", "fecha", "condicion"]).any()


def test_imm_datos():
    from astrohealth.load import cargar_imm_probabilidades, cargar_imm_resultados
    p = cargar_imm_probabilidades()
    assert p["condicion"].nunique() == 98 and len(p) == 98 * 12
    assert p["prob_al_menos_un_evento"].between(0, 1).all()
    r = cargar_imm_resultados()
    trat = r[r["escenario"] == "Tratado"].set_index("drm_dias")
    assert trat.loc[1195, "chi_media"] == pytest.approx(86.87)          # Tabla 5 del PDF
    assert trat.loc[[42, 365, 730, 1195], "p_locl"].is_monotonic_increasing   # 4 tripulantes: crece con la duración


def test_imm_mapeo_y_probabilidades():
    from astrohealth.alertas import IMM_CONDICION, probabilidad_imm
    from astrohealth.load import cargar_imm_probabilidades
    nombres = set(cargar_imm_probabilidades()["condicion"])
    assert set(IMM_CONDICION.values()) <= nombres
    assert set(IMM_CONDICION) <= set(SINTOMAS)
    assert probabilidad_imm("dificultad_dormir") == pytest.approx(0.912)        # PDF, Tabla 2
    assert probabilidad_imm("ardor_orina", sexo="F") == pytest.approx(0.490)
    assert probabilidad_imm("zoster", "Planetaria", 36) > probabilidad_imm("zoster")
    assert probabilidad_imm("ideas_danarse") is None
