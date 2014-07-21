from unittest import TestCase

from horarioDeCursada import HorarioDeCursada
from curso import Curso

class TestCurso(TestCase):

    def test_curso_es_compatible(self):
        curso_compatible = Curso()
        curso_compatible.horarios = [HorarioDeCursada("lunes", "19:00", "23:00"),
                                     HorarioDeCursada("miercoles", "19:00", "23:00")]

        self.assertTrue(curso_compatible.compatible_horario_laboral())


    def test_curso_no_es_compatible(self):
        curso_no_compatible = Curso()
        curso_no_compatible.horarios = [HorarioDeCursada("martes", "09:00", "13:00")]

        self.assertFalse(curso_no_compatible.compatible_horario_laboral())