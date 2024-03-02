from zeep import Client

client = Client('http://localhost:8000')
result = client.service.Saludar(nombre="Tatiana")

#///////////Pruebas suma/////////////
result1 = client.service.SumaDosNumeros(num1 = 3, num2 = 3)
result2 = client.service.SumaDosNumeros(num1 = 4, num2 = 5)

#///////////Pruebas palindromo////////
result3 = client.service.CadenaPalindromo(cadena = "reconocer")
result4 = client.service.CadenaPalindromo(cadena = "nopalindromo")
print(result)

#//////////Resultados suma/////////////
print(result1)
print(result2)

#//////////Resultados palindromo/////////
print(result3)
print(result4)