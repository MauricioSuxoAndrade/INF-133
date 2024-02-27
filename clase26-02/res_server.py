from http.server import HTTPServer, BaseHTTPRequestHandler
import json

estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
    }
]

class RESTRequestHandler(BaseHTTPRequestHandler):