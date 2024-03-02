import requests

url = "http://localhost:8000/"

#///////////////Pruebas
#Estudiantes cuyos nombres comienzan con "P"
ruta_buscar_nombre = url + "buscar_nombre"
buscar_nombre_response = requests.request(method="GET", url=ruta_buscar_nombre)
print(buscar_nombre_response.text)

#Contar la cantidad de estudiantes por carrera
ruta_contar_carreras = url + "contar_carreras"
contar_carreras_response = requests.request(method="GET", url=ruta_contar_carreras)
print(contar_carreras_response.text)

#Obtener la cantidad total de estudiantes
ruta_total_estudiantes = url + "total_estudiantes"
total_estudiantes_response = requests.request(method="GET", url=ruta_total_estudiantes)
print(total_estudiantes_response.text)
