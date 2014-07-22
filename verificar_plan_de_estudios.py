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
from materia import Materia
from curso import Curso
from horarioDeCursada import HorarioDeCursada, TIPOS as TIPOS_HORARIO_CURSADA
import gestion


""" CRAWLER """

URL_MATERIA = 'http://intra.fi.uba.ar/insc/consultas/consulta_cursos.jsp?\
materia={materia}'


def get_info_horario_cursada(pq_curso):
    clases = pq_curso('.tablaitem:eq(4)').text().split()

    horarios = []

    # la separacion de los campos no es consistente, hay que chequear cada fila
    for i in range(len(clases)):
        if clases[i] in TIPOS_HORARIO_CURSADA:
            horarios.append(HorarioDeCursada(clases[i + 1], clases[i + 2], clases[i + 3]))

    return horarios


def get_info_materia(codigo):
    """
    Extrae de info academica los horarios de los cursos de la materia
    especificada.
    """

    # Si la materia es del departamento de Gestión está hardcodeada.
    if codigo[:2] == '71':
        return gestion.obtener_materia(codigo[2:])

    materia = Materia()

    codigo = codigo.replace('.', '')
    d = pq(requests.get(URL_MATERIA.format(materia=codigo)).text)
    materia.nombre = d('#principal h3').text().replace('Cursos de la materia ', '')\
            .replace('''IMPORTANTE: LOS ALUMNOS DEBERAN INSCRIBIRSE UNICAMENTE \
A LAS ASIGNATURAS CORRESPONDIENTES AL PLAN DE ESTUDIOS EN \
EL QUE ESTAN INSCRIPTOS ''', '')

    for tr in d('#principal tr'):
        pq_curso = pq(tr)
        profesor = pq_curso('.tablaitem:eq(2)').text()

        if profesor:
            curso = Curso()
            curso.docentes = profesor
            curso.horarios = get_info_horario_cursada(pq_curso)
            materia.agregar_curso(curso)

    return materia


def cursos_son_compatibles(cursos, nuevo_curso):
    """ Devuelve True si se puede cursar el curso con la lista de cursos anterior.
    """
    if len(cursos) == 0:
        return True

    for curso in cursos:
        if not curso.es_compatible_con(nuevo_curso):
            return False

    return True


def hay_superposicion_de_materias(materias):
    """ Devuelve True si hay al menos una combinacion de cursos disponible para
    cursar simultaneamente la lista de materias indicada.
    """

    combinaciones = []
    for materia in materias:

        nuevas = []
        for curso_actual in materia.cursos:

            for combinacion in combinaciones:
                if cursos_son_compatibles(combinacion, curso_actual):
                    nuevas.append(combinacion + [curso_actual])

            # cuando no hay combinaciones agregar el curso directamente
            if len(combinaciones) == 0:
                nuevas.append([curso_actual])

        combinaciones = nuevas

    return len(combinaciones) == 0


def verificar_plan_de_estudios(archivo_plan_estudios):
    archivo = open(archivo_plan_estudios)
    plan_de_estudios = json.load(archivo)
    archivo.close()

    for cuatrimestre in plan_de_estudios:

        materias = []
        for materia in plan_de_estudios[cuatrimestre]:
            materia = get_info_materia(materia.replace('.', ''))

            if not materia.se_dicta():
                print ("La materia {m} de {c} no tiene cursos publicados.")\
                .format(m=materia.nombre, c=cuatrimestre)
            else:
                materias.append(materia)
                if not materia.compatible_con_horario_laboral():
                    print ("La materia {m} de {c} no tiene horarios " +
                           "compatibles con jornada laboral.").format(
                            m=materia.nombre.encode('utf-8'), c=cuatrimestre)

        if len(materias) > 0 and hay_superposicion_de_materias(materias):
            print ("Las materias de {c} no se pueden hacer simultaneamente.")\
            .format(c=cuatrimestre)


if __name__ == "__main__":
    print "Verificando plan de informática..."
    verificar_plan_de_estudios('informatica.json')
    
    print "Verificando plan de sistemas..."
    verificar_plan_de_estudios('sistemas.json')
