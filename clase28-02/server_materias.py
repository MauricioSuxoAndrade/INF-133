from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": "INF-133",
        "nombre": "Programacion web 3",
        "docente": "Lic Tatiana",
        "carrera": "Informatica",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

def do_GET(self):
        if self.path == "/carreras":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(carreras).encode("utf-8"))
        elif self.path.startswith("/carreras/"):
            id = int(self.path.split("/")[-1])
            carrera = next(
                (carrera for carrera in carreras if carrera["id"] == id),
                None,
            )
            if carrera:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(carrera).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"Error": "Ruta no existente"}).encode("utf-8"))
if __name__ == "__main__":
    run_server()
