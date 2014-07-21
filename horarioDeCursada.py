
import calendar


TIPOS = ['CP', 'CPO', 'DC', 'EP', 'EPO', 'LO', 'P', 'PO', 'T', 'TO',
               'TP', 'TPO', 'VT', 'SP']

class HorarioDeCursada:

    def __init__(self, dia_de_la_semana, hora_desde, hora_hasta):
        self.dia_de_la_semana = dia_de_la_semana
        self.hora_desde = hora_desde
        self.hora_hasta = hora_hasta