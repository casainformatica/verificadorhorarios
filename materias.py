# -*- coding: latin-1 -*-

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
import materia
import curso
import horarioDeCursada
import gestion


""" CRAWLER """

URL_MATERIA = 'http://intra.fi.uba.ar/insc/consultas/consulta_cursos.jsp?\
materia={materia}'


def get_info_horario_cursada(pq_curso):
    clases = pq_curso('.tablaitem:eq(4)').text().split()

    horarios = []

    # la separacion de los campos no es consistente, hay que chequear cada fila
    for i in range(len(clases)):
        if clases[i] in horarioDeCursada.TIPOS:
            horarios.append(horarioDeCursada.HorarioDeCursada(clases[i + 1], clases[i + 2], clases[i + 3]))

    return horarios


def get_info_materia(codigo):
    """
    Extrae de info academica los horarios de los cursos de la materia
    especificada.
    """

    # Si la materia es del departamento de Gestión está hardcodeada.
    if codigo[:2] == '71':
        return gestion.obtener_materia(codigo[2:])

    materia_actual = materia.Materia()

    codigo = codigo.replace('.', '')
    d = pq(requests.get(URL_MATERIA.format(materia=codigo)).text)
    materia_actual.nombre = d('#principal h3').text().replace('Cursos de la materia ', '')\
            .replace('''IMPORTANTE: LOS ALUMNOS DEBERAN INSCRIBIRSE UNICAMENTE \
A LAS ASIGNATURAS CORRESPONDIENTES AL PLAN DE ESTUDIOS EN \
EL QUE ESTAN INSCRIPTOS ''', '')

    for tr in d('#principal tr'):
        pq_curso = pq(tr)
        profesor = pq_curso('.tablaitem:eq(2)').text()

        if profesor:
            curso_actual = curso.Curso()
            curso_actual.docentes = profesor
            curso_actual.horarios = get_info_horario_cursada(pq_curso)
            materia_actual.agregar_curso(curso_actual)

    return materia_actual


""" ANALIZADOR """


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
        for materia_actual in programa[cuatrimestre]:
            materia_actual = get_info_materia(materia_actual.replace('.', ''))

            if not materia_actual.se_dicta():
                print ("La materia {m} de {c} no tiene cursos publicados.")\
                .format(m=materia_actual.nombre, c=cuatrimestre)
            else:
                materias.append(materia_actual)
                if not materia_actual.compatible_horario_laboral():
                    print ("La materia {m} de {c} no tiene horarios " +
                           "compatibles con jornada laboral.").format(
                            m=materia_actual.nombre.encode('utf-8'), c=cuatrimestre)

        if len(materias) > 0 and not superposiciones(materias):
            print ("Las materias de {c} no se pueden hacer simultaneamente.")\
            .format(c=cuatrimestre)


if __name__ == "__main__":
    print "Verificando plan de informática..."
    verificar_programa()
    
    print "Verificando plan de sistemas..."
    verificar_programa('sistemas.json')
