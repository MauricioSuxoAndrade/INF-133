from zeep import Client

client = Client(
	'https://localhost:8000'
)
result = client.service.NumberToWords(5)
print(result)
