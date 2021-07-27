import requests
import json
dolar = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
conversao = dolar.json()
print(conversao['bid'])
