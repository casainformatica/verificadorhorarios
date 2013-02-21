"""
Crawler de fechas de finales. Verifica que no haya materias con varias fechas
de final en la misma semana.

Utiliza las librerias pyquery y requests.

Modo de uso:
>> verificar("<usuario>", "<password>")
"""
import requests
from pyquery import PyQuery as pq
import datetime

LOGIN_URL = "http://finales.fi.uba.ar/login.php"
DATA_URL = "http://finales.fi.uba.ar/"


cuatrimestre = None


def get_cuatrimestre(session):

    # Hacer el request una sola vez por corrida
    global cuatrimestre
    if cuatrimestre:
        return cuatrimestre

    r = session.post(DATA_URL)
    d = pq(r.text)
    cuatrimestre = d("[name='id_cuatrimestre'] option:eq(2)").val()

    return cuatrimestre


def get_pagina(session, departamento=None, materia=None, curso=None):
    """
    Obtiene el contenido de la pagina de finales, con los parametros
    especificados.
    """

    data = {"id_cuatrimestre": get_cuatrimestre(session)}
    if departamento:
        data["id_departamento"] = departamento
    if materia:
        data["id_materia"] = materia
    if curso:
        data["id_curso"] = curso

    r = session.post(DATA_URL, data=data)
    return r.text


def get_departamentos(session):
    """ Devuelve la lista de departamentos disponibles. """

    departamentos = []
    d = pq(get_pagina(session))

    for option in d("[name='id_departamento'] option"):
        val = pq(option).val()
        if val != '-1':
            departamentos.append(val)

    return departamentos


def get_materias(session, id_departamento):
    """
    Devuelve una lista de tuplas (id, nombre) para las materias disponibles
    del departamento especificado.
    """

    materias = []
    d = pq(get_pagina(session, departamento=id_departamento))

    for option in d("[name='id_materia'] option"):
        pq_materia = pq(option)
        val = pq_materia.val()
        nombre = pq_materia.text()
        if val != '-1':
            materias.append((val, nombre))

    return materias


def get_cursos(session, id_departamento, id_materia):
    """
    Devuelve una lista de tuplas (id, nombre) para los cursos disponibles de
    la materia especificada.
    """

    cursos = []
    d = pq(get_pagina(session, departamento=id_departamento,
                       materia=id_materia))

    for option in d("[name='id_curso'] option"):
        pq_curso = pq(option)
        val = pq_curso.val()
        nombre = pq_curso.text()
        if val != '-1':
            cursos.append((val, nombre))

    return cursos


def get_fechas(session, id_departamento, id_materia, id_curso):
    """
    Devuelve la lista de fechas de final publicadas para la materia
    especificada.
    """

    d = pq(get_pagina(session, departamento=id_departamento,
                       materia=id_materia, curso=id_curso))

    fechas = d("[name='id_final']").parent().next().text()
    return fechas.split() if fechas else []


def verificar_fechas(fechas):
    """
    Devuelve True si la lista de fechas de final pasada contiene mas de un
    final por semana.
    """

    # obtiene el numero de semana de cada fecha
    semanas = [datetime.datetime.strptime(f, "%d/%m/%Y"
                                          ).date().isocalendar()[1]
                                          for f in fechas]

    # Si alguna semana esta repetida devuelve true
    if len(semanas) != len(set(semanas)):
        return True

    return False


def verificar(user, password):
    """
    Usando los datos de acceso provistos, recorre las fechas publicadas para
    cada curso, verificando que no haya dos en la misma semana.
    """

    s = requests.Session()
    s.post(LOGIN_URL, data={"usuario": user, "password": password,
                        "Login": "Iniciar Sesion"})

    # Chequeo login
    if not get_cuatrimestre(s):
        print "Los datos de acceso son incorrectos."

    else:

        for id_departamento in get_departamentos(s):

            print "Analizando departamento", id_departamento
            for id_materia, nombre_materia in get_materias(s, id_departamento):

                for id_curso, nombre_curso in get_cursos(s, id_departamento,
                                                          id_materia):

                    fechas = get_fechas(s, id_departamento, id_materia,
                                         id_curso)
                    if verificar_fechas(fechas):
                        print ("\t El curso {c} de {m} tiene mas de una " +
                               "fecha por semana. Fechas: ".format(
                                    c=nombre_curso, m=nombre_materia),
                                    ', '.join(fechas))
