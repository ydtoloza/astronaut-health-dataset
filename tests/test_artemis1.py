"""Cifras de la dosimetría de Artemis I contrastadas con George et al. 2024 (Nature)."""
import pytest

from astrohealth.load import cargar_artemis1_cad, cargar_artemis1_dosis


def test_artemis1_totales_y_picos():
    d = cargar_artemis1_dosis()
    tot = d.assign(mgy=d["tasa_ugy_min"] * d["paso_min"] / 1000).groupby("sensor")["mgy"].sum()
    assert tot["HERA HSU2"] == pytest.approx(13.47, abs=0.01)        # "up to 13.47 mGy for HSU2"
    pico = d.groupby("sensor")["tasa_ugy_min"].max()
    assert pico["M42 SN127"] == pytest.approx(69, abs=0.5)            # 69 µGy/min (más blindado)
    assert pico["EAD MU01"] == pytest.approx(240, abs=0.5)            # 240 µGy/min (menos blindado)
    assert (d["tasa_ugy_min"] >= 0).all()


def test_artemis1_cad():
    c = cargar_artemis1_cad()
    assert c["dosis_acumulada_mgy"].is_monotonic_increasing
    assert c["dosis_acumulada_mgy"].iloc[-1] == pytest.approx(12.18, abs=0.01)
