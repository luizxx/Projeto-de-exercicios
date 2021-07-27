import requests
import json
cid = 'Arraial do Cabo'
API= '8d4630c4bb8c564715b946a7c0156f91'
latitude = '22.96611'
longitude = '-42.027779'
url = f'api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API}'

codigo = requests.get(url)
cod = codigo.json()
print(cod)
