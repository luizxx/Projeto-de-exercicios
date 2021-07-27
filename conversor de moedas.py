import requests
import json

moedas = requests.get("https://economia.awesomeapi.com.br/last/BTC-BRL")
moedas1 = json.loads(moedas.content)
moedas1.keys()
#moedas1.pop('BTCBRL')
print(moedas1)
