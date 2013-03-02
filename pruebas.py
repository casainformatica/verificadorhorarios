from materias import superposiciones, get_info_materia, se_dicta, \
    horario_laboral

# Incompatibles
materias1 = [{'nombre': '6301 QUIMICA 1', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]},
    {'nombre': '6302 QUIMICA 2', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]},
    {'nombre': '6303 QUIMICA 3', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]},
    {'nombre': '6304 QUIMICA 4', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]}]

# una sola compatible consigo misma
materias2 = [{'nombre': '6301 QUIMICA 1', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]}]

# dos compatibles
materias3 = [{'nombre': '6301 QUIMICA 1', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}]}]},
    {'nombre': '6302 QUIMICA 2', 'cursos': [{'profesor': 'GRANDE-CABANI2', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]}]

# dos compatibles en algunos cursos
materias4 = [{'nombre': '6301 QUIMICA 1', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}]},
                                                     {'profesor': 'ARTIGAS', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]},
    {'nombre': '6302 QUIMICA 2', 'cursos': [{'profesor': 'CHICHILO', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]},
                                            {'profesor': 'ALABASTRO', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'lunes'}]}]}]

# igual que antes pero menos
materias5 = [{'nombre': '6301 QUIMICA 1', 'cursos': [{'profesor': 'GRANDE-CABANI', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}, {'comienzo': '17:00', 'fin': '21:00', 'dia': 'miercoles'}]},
                                                     {'profesor': 'ARTIGAS', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]}]},
    {'nombre': '6302 QUIMICA 2', 'cursos': [{'profesor': 'CHICHILO', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'jueves'}]},
                                            {'profesor': 'ALABASTRO', 'clases': [{'comienzo': '17:00', 'fin': '21:00', 'dia': 'martes'}]}]}]


# superposiciones:
def limpiar_lista(materias):
    resultado = []
    for l in materias:
        resultado.append([m['profesor'] for m in l])

    return resultado

print limpiar_lista(superposiciones(materias4))

# se dicta, horario laboral:
quimica = get_info_materia("6301")
print se_dicta(quimica), horario_laboral(quimica)

economia = get_info_materia("7101")
print se_dicta(economia), horario_laboral(economia)
