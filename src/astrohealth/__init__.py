"""astrohealth: carga, validación y reconstrucción del dataset de salud de astronautas."""
from astrohealth.load import (cargar_astronautas, cargar_diario, cargar_eventos, cargar_laboratorio,
                              cargar_lineas_base, cargar_todo, serie_astronauta)

__all__ = ["cargar_astronautas", "cargar_diario", "cargar_eventos", "cargar_laboratorio",
           "cargar_lineas_base", "cargar_todo", "serie_astronauta",
           "evaluar", "estado_del_dia", "evaluar_sintoma", "dosis_radiacion"]


def __getattr__(nombre):
    # Import diferido: permite `python -m astrohealth.alertas` sin importar el módulo dos veces.
    if nombre in ("evaluar", "estado_del_dia", "evaluar_sintoma", "dosis_radiacion"):
        from astrohealth import alertas
        return getattr(alertas, nombre)
    raise AttributeError(nombre)
