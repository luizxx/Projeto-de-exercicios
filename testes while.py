import requests
import json
cep1 = input('Digite seu cep')
cep2 = requests.get(f'https://viacep.com.br/ws/{cep1}/json/')
cep3 = (cep2.json())

if 'erro' in cep3:
    print('error')
else:
    print('Seu cep: {} \n sua cidade {} \n seu estado {} \n seu DDD {} \n logradouro {} \n complemento {} \n bairro {} '.format(cep1,cep3['localidade'],cep3['uf'],cep3['ddd'], cep3 ['logradouro'], cep3['complemento'], cep3['bairro']))