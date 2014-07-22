# Verificador de horarios

Script para analizar los horarios de las materias obligatorias de las carreras
de Ingeniería en Informática y Licenciatura en Análisis de Sistemas de la 
Facultad de Ingeniería de la Universidad de Buenos Aires.

Detecta las siguientes irregularidades:

* Materias obligatorias que no se dictan.
* Materias del mismo cuatrimestre según el plan de estudios que no tienen
horarios compatibles entre sí.
* Materias que no tienen horarios compatibles con la jornada laboral.

Script original de [Refactorizando Informática](http://refactorizandoinformatica.wordpress.com/): 
https://github.com/refactorizando/materias

Utiliza las librerías pyquery y requests.

Modo de uso:
`>>> python verificar_plan_de_estudios(archivo_plan_estudios)`
siendo `archivo_plan_estudios` la ruta a un archivo json con el plan de estudios
que se desea verificar.
