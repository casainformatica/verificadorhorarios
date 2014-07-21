
class Curso:

    def __init__(self):
        self.docentes = ""
        self.horarios = []

    def compatible_horario_laboral(self):
        """ Devuelve True si hay al menos un curso publicado con horario para alumnos
        que trabajan (lunes a viernes a partir de las 18:00 y sabados).
        """
        return self.horarios.all(horario.compatible_horario_laboral() for horario in self.horarios)