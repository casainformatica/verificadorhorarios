# -*- coding: latin-1 -*-

from pyquery import PyQuery
import requests
from materia import Materia
from curso import Curso
from horarioDeCursada import HorarioDeCursada, TIPOS as TIPOS_HORARIO_CURSADA
import materiasgestion

URL_MATERIA = 'http://intra.fi.uba.ar/insc/consultas/consulta_cursos.jsp?\
materia={materia}'


def obtener_horarios(pq_curso):
    clases = pq_curso('.tablaitem:eq(4)').text().split()

    horarios = []

    # la separacion de los campos no es consistente, hay que chequear cada fila
    for i in range(len(clases)):
        if clases[i] in TIPOS_HORARIO_CURSADA:
            horarios.append(HorarioDeCursada(clases[i + 1],
                                             clases[i + 2],
                                             clases[i + 3]))

    return horarios


def obtener_materia(codigo):
    """ Extrae de info academica los horarios de los cursos de la materia
    especificada.
    """

    # Si la materia es del departamento de Gestión se obtiene la información
    # de un módulo aparte.
    if codigo[:2] == '71':
        return materiasgestion.obtener_materia(codigo[2:])

    materia = Materia()

    codigo = codigo.replace('.', '')
    d = PyQuery(requests.get(URL_MATERIA.format(materia=codigo)).text)
    materia.nombre = d('#principal h3').text()\
        .replace('Cursos de la materia ', '')\
        .replace('''IMPORTANTE: LOS ALUMNOS DEBERAN INSCRIBIRSE UNICAMENTE \
A LAS ASIGNATURAS CORRESPONDIENTES AL PLAN DE ESTUDIOS EN \
EL QUE ESTAN INSCRIPTOS ''', '')

    for tr in d('#principal tr'):
        pq_curso = PyQuery(tr)
        profesor = pq_curso('.tablaitem:eq(2)').text()

        if profesor:
            curso = Curso()
            curso.docentes = profesor
            curso.horarios = obtener_horarios(pq_curso)
            materia.agregar_curso(curso)

    return materia
