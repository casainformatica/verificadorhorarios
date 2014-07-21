
from unittest import TestCase
from horarioDeCursada import HorarioDeCursada

class TestHorarioDeCursada(TestCase):

    def test_sabados_es_siempre_compatible_horario_laboral(self):
        horario_sabados_1 = HorarioDeCursada("sabado", "10:00", "13:00")
        self.assertTrue(horario_sabados_1.compatible_horario_laboral())

        horario_sabados_2 = HorarioDeCursada("sabado", "13:00", "17:00")
        self.assertTrue(horario_sabados_2.compatible_horario_laboral())

        horario_sabados_3 = HorarioDeCursada("sabado", "18:00", "22:00")
        self.assertTrue(horario_sabados_3.compatible_horario_laboral())

    def test_manana_semana_no_compatible_horario_laboral(self):
        horario_manana = HorarioDeCursada("martes", "10:00", "13:00")
        self.assertFalse(horario_manana.compatible_horario_laboral())

    def test_tarde_semana_no_compatible_horario_laboral(self):
        horario_tarde = HorarioDeCursada("martes", "13:00", "17:00")
        self.assertFalse(horario_tarde.compatible_horario_laboral())

    def test_noche_semana_no_compatible_horario_laboral(self):
        horario_noche = HorarioDeCursada("martes", "19:00", "21:00")
        self.assertTrue(horario_noche.compatible_horario_laboral())