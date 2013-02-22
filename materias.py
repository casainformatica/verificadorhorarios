"""
Crawler de Informacion academica. Detecta las siguientes irregularidades:

    - Materias obligatorias que no se dictan en el cuatrimestre.
    - Materias del mismo cuatrimestre (segun programa) que no tienen horarios
    compatibles entre si.
    - Materias que no tienen horarios compatibles con jornada laboral.

Utiliza las librerias pyquery y requests.

Modo de uso:
>> verificar_programa(path)

path es la ruta a un archivo json con el programa que se quiere verificar.
"""

import json
from pyquery import PyQuery as pq
import requests


""" CRAWLER """

URL_MATERIA = 'http://intra.fi.uba.ar/insc/consultas/consulta_cursos.jsp?\
materia={materia}'
TIPOS_CURSO = ['CP', 'CPO', 'DC', 'EP', 'EPO', 'LO', 'P', 'PO', 'T', 'TO',
               'TP', 'TPO', 'VT', 'SP']


def _get_clases(pq_curso):
    clases = pq_curso('.tablaitem:eq(4)').text().split()

    resultado = []

    # la separacion de los campos no es consistente, hay que chequear cada fila
    for i in range(len(clases)):
        if clases[i] in TIPOS_CURSO:
            resultado.append({'dia': clases[i + 1],
                              'comienzo': clases[i + 2],
                              'fin': clases[i + 3]})

    return resultado


def get_info_materia(codigo):
    """
    Extrae de info academica los horarios de los cursos de la materia
    especificada.
    """

    materia = {}

    codigo = codigo.replace('.', '')
    d = pq(requests.get(URL_MATERIA.format(materia=codigo)).text)
    materia['nombre'] = d('#principal h3').text().replace(
                                                'Cursos de la materia ', '')

    materia['cursos'] = []
    for tr in d('#principal tr'):
        pq_curso = pq(tr)
        profesor = pq_curso('.tablaitem:eq(2)').text()

        if profesor:
            materia['cursos'].append({'profesor': profesor,
                                      'clases': _get_clases(pq_curso)})

    return materia


""" ANALIZADOR """


# Chequeos:
def se_dicta(materia):
    """ Devuelve True si hay al menos un curso publicado de la materia. """
    return len(materia['cursos']) > 0


def horario_laboral(materia):
    """
    Devuelve True si hay al menos un curso publicado con horario para alumnos
    que trabajan (lunes a viernes a partir de las 19:00 y sabados).
    """

    for curso in materia['cursos']:

        compatible = True
        for clase in curso['clases']:

            if clase['dia'] != 'sabado' and clase['comienzo'] < '19:00':
                compatible = False
                break

        if compatible:
            return True

    return False


def _clases_compatibles(c1, c2):
    if c1['dia'] == c2['dia']:
        return c1['fin'] <= c2['comienzo'] or c1['comienzo'] >= c2['fin']

    return True


def _cursos_compatibles(cursos, nuevo_curso):
    """
    Devuelve True si se puede cursar el curso con la lista de cursos anterior.
    """

    if not cursos:
        return True

    for curso in cursos:
        for clase in curso['clases']:

            for nueva_clase in nuevo_curso['clases']:
                if not _clases_compatibles(clase, nueva_clase):
                    return False

    return True


def superposiciones(materias):
    """
    Devuelve True si hay al menos una combinacion de cursos disponible para
    cursar simultaneamente la lista de materias indicada.
    """

    combinaciones = []
    for materia in materias:

        nuevas = []
        for curso in materia['cursos']:

            for combinacion in combinaciones:
                if _cursos_compatibles(combinacion, curso):
                    nuevas.append(combinacion + [curso])

            # cuando no hay combinaciones agregar el curso directamente
            if not combinaciones:
                nuevas.append([curso])

        combinaciones = nuevas

    return combinaciones


def verificar_programa(path='informatica.json'):
    archivo = open(path)
    programa = json.load(archivo)
    archivo.close()

    for cuatrimestre in programa:

        materias = []
        for materia in programa[cuatrimestre]:
            materia = get_info_materia(materia.replace('.', ''))

            if not se_dicta(materia):
                print "La materia {m} de {c} no tiene cursos publicados."\
                .format(m=materia['nombre'], c=cuatrimestre)
            else:
                materias.append(materia)
                if not horario_laboral(materia):
                    print ("La materia {m} de {c} no tiene horarios " +
                           "compatibles con jornada laboral.").format(
                            m=materia['nombre'], c=cuatrimestre)

        if len(materias) and not superposiciones(materias):
            print "Las materias de {c} no se pueden hacer simultaneamente."\
            .format(c=cuatrimestre)
