"""Rutas del proyecto. Todo el código usa estas constantes; nada depende del directorio actual."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RAW = DATA / "raw"            # archivos originales de NASA, nunca se modifican
RAW_NLSP = RAW / "nlsp"       # UTMB (NASA Life Sciences Portal)
RAW_OSDR = RAW / "osdr"       # Inspiration4 (NASA OSDR)
INTERIM = DATA / "interim"    # tablas limpias por fuente (generadas)
PROCESSED = DATA / "processed"  # dataset unificado para análisis y la app (generado)
FIGURES = ROOT / "reports" / "figures"

# Fases y su orden lógico
FASES = ["pre", "mision", "post"]

# Columnas simuladas: NO son datos reales
COLUMNAS_SIMULADAS = ["animo_0a10_sim", "hrv_rmssd_ms_sim", "spo2_pct_sim",
                      "radiacion_msv_dia_sim", "radiacion_msv_acum_sim"]

# Rangos fisiológicos plausibles usados en la limpieza
RANGOS_PLAUSIBLES = {"pulso_lpm": (30, 200), "pas_mmhg": (70, 220), "pad_mmhg": (35, 140),
                     "resp_rpm": (6, 40), "temp_c": (34.0, 40.5), "peso_kg": (30, 200)}

# Entradas de sangre de PhenoAge (Levine et al. 2018); falta la edad
PHENOAGE_ANALITOS = ["albumina", "creatinina", "glucosa", "pcr", "linfocitos_pct", "vcm", "rdw",
                     "fosfatasa_alcalina", "leucocitos"]
