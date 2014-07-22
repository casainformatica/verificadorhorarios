

class Materia(object):

    def __init__(self):
        self.nombre = ""
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def se_dicta(self):
        return len(self.cursos) > 0

    def es_compatible_con_horario_laboral(self):
        """ Devuelve True si hay al menos un curso publicado con horario para
        alumnos que trabajan (lunes a viernes a partir de las 18:00 y sabados).
        """
        return any(curso.es_compatible_con_horario_laboral() for curso
                   in self.cursos)
