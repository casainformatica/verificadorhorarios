# -*- coding: latin-1 -*-

""" Provee información sobre las materias del departamento de gestión,
cuya información no está disponible desde el sistema de información
académica.
"""

from curso import Curso
from materia import Materia
from horariodecursada import HorarioDeCursada

_materias = {}


def cargar_materias():
    # 71.12
    materia_12 = Materia()
    materia_12.nombre = '7112 ESTRUCTURA DE LAS ORGANIZACIONES'
    curso_12 = Curso()
    curso_12.docentes = 'REYES'
    curso_12.horarios = [HorarioDeCursada('miercoles', '18:00', '23:00')]
    materia_12.agregar_curso(curso_12)
    _materias['12'] = materia_12

    # 71.13
    materia_13 = Materia()
    materia_13.nombre = '7113 INFORMACION EN LAS ORGANIZACIONES'
    curso_13 = Curso()
    curso_13.docentes = 'MARKDORF'
    curso_13.horarios = [HorarioDeCursada('martes', '18:00', '22:00')]
    materia_13.agregar_curso(curso_13)
    _materias['13'] = materia_13

    # 71.15
    materia_15 = Materia()
    materia_15.nombre = '7115 MODELOS Y OPTIMIZACION II'
    curso_15 = Curso()
    curso_15.docentes = 'MARKDORF'
    curso_15.horarios = [HorarioDeCursada('miercoles', '19:00', '21:00'),
                         HorarioDeCursada('jueves', '19:00', '23:00')]
    materia_15.agregar_curso(curso_15)
    _materias['15'] = materia_15

    # 71.16
    materia_16 = Materia()
    materia_16.nombre = '7116 ADMINISTRACION DE PROYECTOS'
    curso_16 = Curso()
    curso_16.docentes = 'BILELLO'
    curso_16.horarios = [HorarioDeCursada('martes', '19:30', '22:30'),
                         HorarioDeCursada('viernes', '19:30', '22:30')]
    materia_16.agregar_curso(curso_16)
    _materias['16'] = materia_16

    # 71.40
    materia_40 = Materia()
    materia_40.nombre = '7140 LEG Y EJ PROFESIONAL DE ING EN INFORMATICA'
    curso_40 = Curso()
    curso_40.docentes = 'NOREMBERG'
    curso_40.horarios = [HorarioDeCursada('viernes', '19:00', '23:00')]
    materia_40.agregar_curso(curso_40)
    _materias['40'] = materia_40

    # 71.14
    materia_14 = Materia()
    materia_14.nombre = 'MODELOS Y OPTIMIZACION I'
    curso_14_1 = Curso()
    curso_14_1.docentes = 'RAMONET-NAVARRO'
    curso_14_1.horarios = [HorarioDeCursada('lunes', '19:00', '22:00'),
                           HorarioDeCursada('jueves', '9:00', '11:30')]
    materia_14.agregar_curso(curso_14_1)
    curso_14_2 = Curso()
    curso_14_2.docentes = 'RAMONET-OITANA'
    curso_14_2.horarios = [HorarioDeCursada('martes', '19:00', '22:00'),
                           HorarioDeCursada('jueves', '9:00', '11:30')]
    materia_14.agregar_curso(curso_14_2)
    curso_14_3 = Curso()
    curso_14_3.docentes = 'RAMONET-ECHEVARRIA'
    curso_14_3.horarios = [HorarioDeCursada('martes', '9:00', '12:00'),
                           HorarioDeCursada('jueves', '9:00', '11:30')]
    materia_14.agregar_curso(curso_14_3)
    curso_14_4 = Curso()
    curso_14_4.docentes = 'RAMONET-COLOMBO'
    curso_14_4.horarios = [HorarioDeCursada('sabados', '10:00', '13:00'),
                           HorarioDeCursada('jueves', '9:00', '11:30')]
    materia_14.agregar_curso(curso_14_4)
    curso_14_5 = Curso()
    curso_14_5.docentes = 'RAMONET-ROMANO'
    curso_14_5.horarios = [HorarioDeCursada('jueves', '19:00', '22:00'),
                           HorarioDeCursada('jueves', '9:00', '11:30')]
    materia_14.agregar_curso(curso_14_5)
    curso_14_6 = Curso()
    curso_14_6.docentes = 'RAMOS-NAVARRO'
    curso_14_6.horarios = [HorarioDeCursada('lunes', '19:00', '22:00'),
                           HorarioDeCursada('miercoles', '18:00', '21:30')]
    materia_14.agregar_curso(curso_14_6)
    curso_14_7 = Curso()
    curso_14_7.docentes = 'RAMOS-OITANA'
    curso_14_7.horarios = [HorarioDeCursada('martes', '19:00', '22:00'),
                           HorarioDeCursada('miercoles', '18:00', '21:30')]
    materia_14.agregar_curso(curso_14_7)
    curso_14_8 = Curso()
    curso_14_8.docentes = 'RAMOS-ECHEVARRIA'
    curso_14_8.horarios = [HorarioDeCursada('martes', '9:00', '12:00'),
                           HorarioDeCursada('miercoles', '18:00', '21:30')]
    materia_14.agregar_curso(curso_14_8)
    curso_14_9 = Curso()
    curso_14_9.docentes = 'RAMOS-COLOMBO'
    curso_14_9.horarios = [HorarioDeCursada('sabado', '10:00', '13:00'),
                           HorarioDeCursada('miercoles', '18:00', '21:30')]
    materia_14.agregar_curso(curso_14_9)
    curso_14_10 = Curso()
    curso_14_10.docentes = 'RAMOS-ROMANO'
    curso_14_10.horarios = [HorarioDeCursada('jueves', '19:00', '22:00'),
                            HorarioDeCursada('miercoles', '18:00', '21:30')]
    materia_14.agregar_curso(curso_14_10)

    _materias['14'] = materia_14


def obtener_materia(codigo):
    return _materias[codigo]


cargar_materias()
