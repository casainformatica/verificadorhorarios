"""
Crawler de fechas de finales. Verifica que no haya materias con varias fechas
de final en la misma semana.

Utiliza las librerias pyquery y requests.
"""
import requests
from pyquery import PyQuery as pq

USUARIO = ""
PASSWORD = ""

LOGIN_URL = "http://finales.fi.uba.ar/login.php"
DATA_URL = "http://finales.fi.uba.ar/"


def _get_cuatrimestre(session):
    r = session.post(DATA_URL)
    d = pq(r.text)
    return d("[name='id_cuatrimestre'] option:eq(2)").val()


def _get_pagina(session, departamento=None, materia=None, curso=None):
    """
    Obtiene el contenido de la pagina de finales, con los parametros
    especificados.
    """

    data = {"id_cuatrimestre": _get_cuatrimestre(session)}
    if departamento:
        data["id_departamento"] = departamento
    if materia:
        data["id_materia"] = materia
    if curso:
        data["id_curso"] = curso

    r = session.post(DATA_URL, data=data)
    return r.text


def _get_departamentos(session):
    """ Devuelve la lista de departamentos disponibles. """

    departamentos = []
    d = pq(_get_pagina(session))

    for option in d("[name='id_departamento'] option"):
        departamentos.append(pq(option).val())

    return departamentos


def _get_materias(session, id_departamento):
    """
    Devuelve la lista de materias disponibles para el departamento
    especificado.
    """

    materias = []
    d = pq(_get_pagina(session, departamento=id_departamento))

    for option in d("[name='id_materia'] option"):
        materias.append(pq(option).val())

    return materias


def _get_fechas(session, id_materia):
    """
    Devuelve la lista de fechas de final publicadas para la materia
    especificada.
    """
    #TODO
    pass


def _verificar_fechas(fechas):
    """
    Verifica que la lista de fechas de final pasada no contenga más de un
    final por semana.
    """
    #TODO
    pass


def verificar():
    s = requests.Session()
    s.post(LOGIN_URL, data={"usuario": USUARIO, "password": PASSWORD,
                        "Login": "Iniciar Sesion"})

    for id_departamento in _get_departamentos(s):
        for id_materia in _get_materias(s, id_departamento):
            fechas = _get_fechas(s, id_materia)
            _verificar_fechas(fechas)
