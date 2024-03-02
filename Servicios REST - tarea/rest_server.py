from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "Choque",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 2,
        "nombre": "Juan",
        "apellido": "Mamani",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 3,
        "nombre": "Laura",
        "apellido": "Bozo",
        "carrera": "Derecho",
    },
    {
        "id": 4,
        "nombre": "Pepito",
        "apellido": "López",
        "carrera": "Ingeniería de Sistemas",
    },
    {
        "id": 5,
        "nombre": "Andrea",
        "apellido": "Martínez",
        "carrera": "Ingeniería Eléctrica",
    },
    {
        "id": 6,
        "nombre": "Alejandro",
        "apellido": "Gutiérrez",
        "carrera": "Ingeniería Civil",
    },
    {
        "id": 7,
        "nombre": "Valeria",
        "apellido": "Sánchez",
        "carrera": "Medicina",
    },
    {
        "id": 8,
        "nombre": "Diego",
        "apellido": "Fernández",
        "carrera": "Arquitectura",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/lista_estudiantes":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/eliminar_estudiante":
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            estudiantes.clear()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path.startswith("/buscar_estudiante_id/"):
            id = int(self.path.split("/")[-1])
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiante).encode("utf-8"))
        
        #/////////////////Buscar los que inician por p
        elif self.path == "/buscar_nombre":
            estudiantes_con_p = [estudiante["nombre"] for estudiante in estudiantes if estudiante["nombre"].startswith("P")]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"nombres_con_p": estudiantes_con_p}).encode("utf-8"))

        #////////////////Buscar estudiantes por carrera
        elif self.path == "/contar_carreras":
            carreras = [estudiante["carrera"] for estudiante in estudiantes]
            contar_carreras = {carrera: carreras.count(carrera) for carrera in set(carreras)}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"contar_carreras": contar_carreras}).encode("utf-8"))

        #/////////////////Total estudiantes
        elif self.path == "/total_estudiantes":
            total_estudiantes = len(estudiantes)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"total_estudiantes": total_estudiantes}).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))

    def do_POST(self):
        if self.path == "/agrega_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            post_data["id"] = len(estudiantes) + 1
            estudiantes.append(post_data)
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        elif self.path == "/actualizar_estudiante":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            post_data = json.loads(post_data.decode("utf-8"))
            id = post_data["id"]
            estudiante = next(
                (estudiante for estudiante in estudiantes if estudiante["id"] == id),
                None,
            )
            if estudiante:
                estudiante.update(post_data)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(estudiantes).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()