import requests
import json
id_arraial = '3477'
nome = 'Arraial do Cabo'
n = requests.get('https://api.coingecko.com/api/v3/coins/list?include_platform=false')
n1 = (n.json())
print(n1)