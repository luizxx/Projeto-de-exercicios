import json
import requests
import json
cont = 0 
while True:
    cont = input('Deseja continuar?').lower().strip()[0]
    if cont == 's':
        r  = requests.get('https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/rj') #api
        r1 = (r.json())
        print('RIO DE JANEIRO \n NUMERO DE MORTES: {} \n CASOS CONFIRMADOS: {} \n CASOS SUSPEITOS: {} \n DATA: {}'.format(r1['deaths'],r1['cases'], r1['suspects'],r1['datetime']))
    else:
        break