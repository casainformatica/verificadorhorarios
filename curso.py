
class Curso:

    def __init__(self):
        self.docentes = ""
        self.horarios = []

    def compatible_con_horario_laboral(self):
        """ Devuelve True si todos los horarios del curso
        son compatibles con el horario laboral.
        """
        print self.horarios
        return all(horario.compatible_con_horario_laboral() for horario in self.horarios)

    def es_compatible_con(self, otro):
        for horario in self.horarios:
            for nuevo_horario in otro.horarios:
                if not horario.es_compatible_con(nuevo_horario):
                    return False
        return True