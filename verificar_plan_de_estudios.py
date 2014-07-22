# -*- coding: latin-1 -*-

"""
Crawler de Información Académica. Detecta las siguientes irregularidades:

    - Materias obligatorias que no se dictan en el cuatrimestre.
    - Materias del mismo cuatrimestre del plan de estudios que no tienen
    horarios compatibles entre sí.
    - Materias que no tienen horarios compatibles con jornada laboral.

Utiliza las librerías pyquery y requests.

Modo de uso:
>> verificar_programa(archivo_plan_estudios)

archivo_plan_estudios es la ruta a un archivo json con el plan de estudios
que se quiere verificar.
"""

import json
import informacionmaterias


def cursos_son_compatibles(cursos, nuevo_curso):
    """ Devuelve True si los horarios del nuevo curso son compatibles con los
    de los otros.
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
            codigo_materia = materia.replace('.', '')
            materia = informacionmaterias.obtener_materia(codigo_materia)

            if not materia.se_dicta():
                print ("La materia {m} de {c} no tiene cursos publicados.")\
                .format(m=materia.nombre, c=cuatrimestre)
            else:
                materias.append(materia)
                if not materia.es_compatible_con_horario_laboral():
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
