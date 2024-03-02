from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

# Define la función del servicio
def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

def suma_dos_numeros(num1, num2):
    return num1 + num2

def cadena_palindromo(cadena):
    return cadena == cadena[::-1]

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

# Registramos el servicio
dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)


#//////////Suma de numeros////////////
dispatcher.register_function(
    "SumaDosNumeros",
    suma_dos_numeros,
    returns={"resultado": int},
    args={"num1": int, "num2": int},
)

#//////////////Palindromo///////////////
dispatcher.register_function(
    "CadenaPalindromo",
    cadena_palindromo,
    returns={"es_palindromo": bool},
    args={"cadena": str},
)


# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()