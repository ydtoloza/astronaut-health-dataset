"""Revisión rápida de integridad del dataset procesado. Uso: `make validate`.

Imprime un reporte y termina con código 1 si alguna regla falla.
"""
import sys

import pandas as pd

from astrohealth.config import COLUMNAS_SIMULADAS, PHENOAGE_ANALITOS, RANGOS_PLAUSIBLES
from astrohealth.load import cargar_astronautas, cargar_diario, cargar_eventos, cargar_laboratorio


def revisar() -> list:
    """Devuelve una lista de (regla, ok, detalle)."""
    res = []
    d, lab = cargar_diario(), cargar_laboratorio(excluir_atipicos=False)
    ev, perf = cargar_eventos(), cargar_astronautas()

    res.append(("Sin días duplicados por astronauta",
                not d.duplicated(["astronauta_id", "fecha"]).any(),
                f"{d.duplicated(['astronauta_id', 'fecha']).sum()} duplicados"))
    for col, (lo, hi) in RANGOS_PLAUSIBLES.items():
        fuera = d[col].dropna().pipe(lambda s: ((s < lo) | (s > hi)).sum())
        res.append((f"{col} dentro de [{lo}, {hi}]", fuera == 0, f"{fuera} fuera de rango"))
    res.append(("Fases válidas", d["fase"].notna().all(), f"{d['fase'].isna().sum()} sin fase"))
    mis = d[(d["fase"] == "mision") & d["br_day"].notna()]
    desfase = ((mis["br_day"] - mis["dia_mision"]).abs() > 1).sum()
    res.append(("dia_mision coherente con BR_Day (≤ 4 errores conocidos del origen)", desfase <= 4,
                f"{desfase} filas"))
    res.append(("Columnas simuladas presentes y marcadas", all(c in d.columns for c in COLUMNAS_SIMULADAS),
                ", ".join(COLUMNAS_SIMULADAS)))
    rad_pre = d.loc[d["fase"] == "pre", "radiacion_msv_acum_sim"].fillna(0).abs().sum()
    res.append(("Radiación simulada = 0 antes de la misión", rad_pre == 0, f"suma pre = {rad_pre}"))
    res.append(("Semáforo con 3 estados", set(d["estado_vitales"].dropna().unique()) <= {"verde", "amarillo", "rojo"},
                d["estado_vitales"].value_counts(normalize=True).round(3).to_dict()))
    res.append(("Astronautas del diario existen en perfiles",
                set(d["astronauta_id"]) <= set(perf["astronauta_id"]), f"{d['astronauta_id'].nunique()} astronautas"))
    for fuente in ("UTMB", "Inspiration4"):
        sub = lab[lab["fuente"].str.startswith(fuente) & lab["atipico"].isna() & lab["analito"].isin(PHENOAGE_ANALITOS)]
        clave = sub["fecha"].dt.strftime("%Y-%m-%d").fillna("dia " + sub["dia_relativo"].astype("Int64").astype(str))
        tomas = sub.groupby([sub["astronauta_id"], clave])["analito"].nunique()
        res.append((f"PhenoAge: tomas completas en {fuente}", (tomas == 9).sum() > 0,
                    f"{(tomas == 9).sum()} de {len(tomas)} tomas con las 9 entradas"))
    res.append(("Laboratorio sin valores vacíos", lab["valor"].notna().all(), f"{len(lab)} valores"))
    res.append(("Eventos con categoría", ev["categoria"].notna().all(), f"{len(ev)} eventos"))
    return res


def main():
    res = revisar()
    ancho = max(len(r[0]) for r in res)
    for regla, ok, detalle in res:
        print(f"{'OK   ' if ok else 'FALLA'}  {regla:<{ancho}}  {detalle}")
    fallas = sum(not ok for _, ok, _ in res)
    print(f"\n{len(res) - fallas}/{len(res)} reglas OK")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
