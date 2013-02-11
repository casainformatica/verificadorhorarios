"""
Crawler de fechas de finales. Verifica que no haya materias con varias fechas
de final en la misma semana.

Utiliza las librerias pyquery y requests.
"""
import requests

USUARIO = ""
PASSWORD = ""

LOGIN_URL = "http://finales.fi.uba.ar/login.php"
DATA_URL = "http://finales.fi.uba.ar/"


#r = s.post(DATA_URL, data={"id_cuatrimestre": "57", "id_departamento": "64",
#                           "id_materia": "375", "id_curso": "1021"})
#r.text


def _get_departamentos(session):
    """ Devuelve la lista de departamentos disponibles. """

    pass


def _get_materias(session, id_departamento):
    """
    Devuelve la lista de materias disponibles para el departamento
    especificado.
    """

    pass


def _get_fechas(session, id_materia):
    """
    Devuelve la lista de fechas de final publicadas para la materia
    especificada.
    """

    pass


def _verificar_fechas(fechas):
    """
    Verifica que la lista de fechas de final pasada no contenga más de un
    final por semana.
    """

    pass


def verificar():
    s = requests.Session()
    s.post(LOGIN_URL, data={"usuario": USUARIO, "password": PASSWORD,
                        "Login": "Iniciar Sesion"})

    for id_departamento in _get_departamentos(s):
        for id_materia in _get_materias(s, id_departamento):
            fechas = _get_fechas(s, id_materia)
            _verificar_fechas(fechas)
