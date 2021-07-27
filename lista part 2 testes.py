dados = list()
pessoas = list()
idade = list()
nome = list()
nome_maior = list() 
cont = 'p'
permissao = True
maior = 0
while cont != 's' or cont != 'n':
    if permissao ==True:
        dados.append(str(input('Nome')))
        dados.append(int(input('idade')))
        pessoas.append(dados[:])    # isso ira criar uma lista dentro de outra contendo imformacoes
        dados.clear() # isso é para criar uma lista so a acada vez, se nao tiver fica uma bagunca
        if pessoas[-1][1] >18:
            maior = maior +1
            nome_maior.append(pessoas[-1][0])
            print('funcionando aqui')
    cont = input('Deseja continuar?').strip().lower()[0]
    if cont =='s' or cont =='n':
        if cont =='s':
            permissao = True
        if cont =='n':
            permissao = False
            break

print(f'Os maiores de idade são os {nome_maior}'if len(nome_maior) > 1 else f'Tivemos apenas 1 maior de idade que é o {nome_maior}.')


print(pessoas)
    