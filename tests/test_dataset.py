"""Tests de integridad del dataset. Ejecutar con `make test`.

Fijan las cifras verificadas en la auditoría (docs/verificacion/): si un cambio en el pipeline
las altera, el test falla y obliga a revisar.
"""
import pandas as pd
import pytest

from astrohealth.config import PHENOAGE_ANALITOS, RANGOS_PLAUSIBLES
from astrohealth.load import (cargar_astronautas, cargar_diario, cargar_eventos, cargar_laboratorio,
                              laboratorio_ancho)
from astrohealth.validate import revisar


@pytest.fixture(scope="module")
def diario():
    return cargar_diario()


@pytest.fixture(scope="module")
def lab():
    return cargar_laboratorio(excluir_atipicos=False)


def test_reglas_de_validacion():
    fallas = [(r, det) for r, ok, det in revisar() if not ok]
    assert not fallas, fallas


def test_tamanos(diario, lab):
    assert len(cargar_astronautas()) == 44
    assert diario["astronauta_id"].nunique() == 40
    assert diario["pulso_lpm"].notna().sum() >= 2900
    assert len(cargar_eventos()) == 1053
    assert lab["fuente"].str.startswith("UTMB").sum() == 8036


def test_rangos_plausibles(diario):
    for col, (lo, hi) in RANGOS_PLAUSIBLES.items():
        s = diario[col].dropna()
        assert s.between(lo, hi).all(), col


def test_cifras_verificadas(diario):
    pulso = diario.groupby("fase", observed=True)["pulso_lpm"].mean().round(1)
    assert pulso["post"] == pytest.approx(76.1, abs=0.1)
    no_verde = 1 - diario.groupby("fase", observed=True)["estado_vitales"].apply(lambda s: (s.dropna() == "verde").mean())
    assert no_verde["post"] == pytest.approx(0.36, abs=0.01)


def test_inspiration4_leucocitos_bajan(lab):
    i4 = lab[lab["fuente"].str.startswith("Inspiration4") & (lab["analito"] == "leucocitos") & lab["atipico"].isna()]
    antes = i4[i4["dia_relativo"] == -3]["valor"].mean()
    despues = i4[(i4["fase"] == "post") & (i4["dia_relativo"] == 1)]["valor"].mean()
    assert despues / antes - 1 == pytest.approx(-0.26, abs=0.01)


def test_phenoage_entradas_presentes(lab):
    ancho = laboratorio_ancho(lab[lab["atipico"].isna()], PHENOAGE_ANALITOS)
    completas = ancho.dropna(subset=PHENOAGE_ANALITOS)
    assert (completas["origen"] == "UTMB").sum() >= 100
    assert (completas["origen"] == "Inspiration4").sum() >= 20
