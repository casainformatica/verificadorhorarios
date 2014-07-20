# -*- coding: latin-1 -*-

# Poco poético, es lo que hay por ahora.

materia = { 
	'12' : { 
		'nombre': '7112 ESTRUCTURA DE LAS ORGANIZACIONES', 
                'cursos': [{
			'profesor': 'REYES', 
			'clases': [{ 
				'comienzo': '18:00', 
				'fin': '23:00', 
				'dia': 'miercoles'
			}]
		}]
	},
	'13' : { 
		'nombre': '7113 INFORMACION EN LAS ORGANIZACIONES', 
                'cursos': [{
			'profesor': 'MARKDORF', 
			'clases': [{ 
				'comienzo': '18:00', 
				'fin': '22:00', 
				'dia': 'martes'
			}]
		}]
	},
	'15' : { 
		'nombre': '7115 MODELOS Y OPTIMIZACION II', 
                'cursos': [{
			'profesor': 'MARKDORF', 
			'clases': [{ 
				'comienzo': '19:00', 
				'fin': '21:00', 
				'dia': 'miercoles'
			},{
				'comienzo': '19:00', 
				'fin': '23:00', 
				'dia': 'jueves'			
			}]
		}]
	},
	'16' : { 
		'nombre': '7116 ADMINISTRACION DE PROYECTOS', 
                'cursos': [{
			'profesor': 'BILELLO', 
			'clases': [{ 
				'comienzo': '19:30', 
				'fin': '22:30', 
				'dia': 'martes'
			},{
				'comienzo': '19:30', 
				'fin': '22:30', 
				'dia': 'viernes'			
			}]
		}]
	},
	'40' : { 
		'nombre': '7140 LEGISLACION Y EJ PROFESIONAL DE ING EN INFORMATICA', 
                'cursos': [{
			'profesor': 'NOREMBERG', 
			'clases': [{ 
				'comienzo': '19:00', 
				'fin': '23:00', 
				'dia': 'viernes'
			}]
		}]
	},
	'14' : {
		'nombre': '7114 MODELOS Y OPTIMIZACION I',
		'cursos': [{
			'profesor': 'RAMONET-NAVARRO',  
			'clases': [{
				'comienzo': '9:00', 'fin': '11:30', 'dia': 'jueves'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'lunes'
			}]},{
			'profesor': 'RAMOS-NAVARRO', 
			'clases': [{
				'comienzo': '18:30', 'fin': '21:30', 'dia': 'miercoles'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'lunes'
			}]},{
			'profesor': 'RAMONET-OITANA',
			'clases': [{
				'comienzo': '9:00', 'fin': '11:30', 'dia': 'jueves'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'martes'
			}]},{
			'profesor': 'RAMOS-OITANA', 
			'clases': [{
				'comienzo': '18:30', 'fin': '21:30', 'dia': 'miercoles'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'martes'
			}]},{
			'profesor': 'RAMONET-ECHEVARRIA', 
			'clases': [{
				'comienzo': '9:00', 'fin': '11:30', 'dia': 'jueves'
			},{
				'comienzo': '9:00', 'fin': '12:00', 'dia': 'martes'
			}]},{
			'profesor': 'RAMOS-ECHEVARRIA', 
			'clases': [{
				'comienzo': '18:30', 'fin': '21:30', 'dia': 'miercoles'
			 },{
				'comienzo': '9:00', 'fin': '12:00', 'dia': 'martes'
			}]}, {
			'profesor': 'RAMONET-COLOMBO', 
			'clases': [{
				'comienzo': '9:00', 'fin': '11:30', 'dia': 'jueves'
			},{
				'comienzo': '10:00', 'fin': '13:00', 'dia': 'sabado'
			}]},{
			'profesor': 'RAMOS-COLOMBO',
			'clases': [{
				'comienzo': '18:30', 'fin': '21:30', 'dia': 'miercoles'
			},{
				'comienzo': '10:00', 'fin': '13:00', 'dia': 'sabado'
			}]},{
			'profesor': 'RAMONET-ROMANO', 
			'clases': [{
				'comienzo': '9:00', 'fin': '11:30', 'dia': 'jueves'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'jueves'
			}]}, {
			'profesor': 'RAMOS-ROMANO', 
			'clases': [{
				'comienzo': '18:30', 'fin': '21:30', 'dia': 'miercoles'
			},{
				'comienzo': '19:00', 'fin': '22:00', 'dia': 'jueves'
			}]
		}]
	}
}
                                   
default = { 'nombre': '', 'cursos': [ ] }

def obtener_materia(codigo):
    return materia[codigo]
    # return materia[codigo] if codigo in materia else default
