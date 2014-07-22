
TIPOS = ['CP', 'CPO', 'DC', 'EP', 'EPO', 'LO', 'P', 'PO', 'T', 'TO',
               'TP', 'TPO', 'VT', 'SP']


class HorarioDeCursada:

    def __init__(self, dia_de_la_semana, hora_desde, hora_hasta):
        self.dia_de_la_semana = dia_de_la_semana
        self.hora_desde = hora_desde
        self.hora_hasta = hora_hasta

    def es_compatible_con_horario_laboral(self):
        """ Devuelve True si es compatible para alumnos que trabajan
        (lunes a viernes a partir de las 18:00 y sabados).
        """
        return self.dia_de_la_semana == 'sabado' or self.hora_desde >= '18:00'

    def es_compatible_con(self, otro):
        """ Devuelve True si ambos horarios son compatibles,
        False en caso contrario.
        """
        if self.dia_de_la_semana != otro.dia_de_la_semana:
            return True

        return self.hora_hasta <= otro.hora_desde or \
               self.hora_desde >= otro.hora_hasta
