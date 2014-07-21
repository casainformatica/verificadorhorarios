
class Materia(object):

    def __init__(self):
        self.nombre = ""
        self.cursos = []
        
    def agregar_curso(self, curso):
        self.cursos.append(curso)