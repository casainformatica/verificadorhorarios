
class Curso:

    def __init__(self):
        self.docentes = ""
        self.horarios = []

    def compatible_horario_laboral(self):
        """ Devuelve True si todos los horarios del curso
        son compatibles con el horario laboral.
        """
        print self.horarios
        return all(horario.compatible_horario_laboral() for horario in self.horarios)