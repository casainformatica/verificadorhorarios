
TIPOS = ['CP', 'CPO', 'DC', 'EP', 'EPO', 'LO', 'P', 'PO', 'T', 'TO',
               'TP', 'TPO', 'VT', 'SP']

class HorarioDeCursada:

    def __init__(self, dia_de_la_semana, hora_desde, hora_hasta):
        self.dia_de_la_semana = dia_de_la_semana
        self.hora_desde = hora_desde
        self.hora_hasta = hora_hasta

    def compatible_horario_laboral(self):
        """ Devuelve True si es compatible para alumnos que trabajan
        (lunes a viernes a partir de las 18:00 y sabados).
        """
        return self.dia_de_la_semana == 'sabado' or self.hora_desde >= '18:00'