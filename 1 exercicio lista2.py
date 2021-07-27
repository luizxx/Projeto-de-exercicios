nome = list()
peso = list()
galera = list()
pessoas_cadastradas = 0
permissao = True
dados = list()
while True:
    if permissao == True :
        dados.append(input('Digite seu nome').lower().strip())
        dados.append(int(input('Peso: ' ).lower().strip()))
        galera.append(dados[:])
        dados.clear()
        if galera[-1][1] >=100:
            print('Cheguei aqui 0 ')
        elif galera[-1][1] <71:
            print('Cheguei aqui 1')
        elif galera not in galera and galera not in 100:
            print('To aqui 2')
        pessoas_cadastradas = pessoas_cadastradas +1
        conti = input('Deseja continuar?').lower().strip()[0]
    if conti =='s':
        
        permissao= True
    elif conti =='n':
        permissao = False
        break
    else:
        permissao=False
