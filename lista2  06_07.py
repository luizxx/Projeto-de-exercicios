dados = list()
pessoas = list()
pessoas_pesadas_peso = list()
pessoas_leves_nome = list()
pessoas_leves_peso = list()
pessoas_pesadas_nome = list()
contagem = 0 
condi = True
contt = 0
contte = 0

while True:
    if condi == True:
        dados.append(input('Nome: ' ).lower())
        dados.append(int(input('Peso: ' )))
        pessoas.append(dados[:])
        contagem = contagem +1 
        if pessoas[-1][1] >=100:
            pessoas_pesadas_nome.append(pessoas[-1][0])
            pessoas_pesadas_peso.append(pessoas[-1][1])
            contt = contt +1
                       
        if pessoas[-1][1] <=70:
            pessoas_leves_nome.append(pessoas[-1][0])
            pessoas_leves_peso.append(pessoas[-1][1])
            contte = contte +1
        dados.clear()
        
    contin = input('Deseja continuar? [S/N]').lower().strip()[0]
    if contin == 's':
        condi = True
    elif contin =='n':
        condi = False
        break
    elif contin not in 's':
        condi =False
if contte == 0 and  contt ==0:
    print('Não teve pessoas leves com MENOS de 70KG e nem pessoas pesadas com MAIS de 69KG.')
if contt >=1:
        print('pessoas mais pesadas com MAIS de 99KG')
        for c in range(0,contt):
            print(f'{pessoas_pesadas_nome[c]} = {pessoas_pesadas_peso[c]}KG')
if contt == 0 and contte >=1:
        print('Não teve pessoas com MAIS de 99KG.')
            

if contte >=1:
        print('pessoas com MENOS de 70KG ou menos')
        for c in range (0,contte):
                print(f'{pessoas_leves_nome[c]} = {pessoas_leves_peso[c]}KG')

if contte ==0 and contt >=1:
        print('Sem pessoas com MENOS de 70KG.')


        
            
#print(f'Tiveram {contagem} pessoas \n pessoas pesadas', f'{pessoas_pesadas_nome} com {pessoas_pesadas_peso} kilos' if len(pessoas_pesadas_peso) >0 else'Não tiveram pessoas pesadas.')
#print(f' pessoas leves {pessoas_leves_nome} com {pessoas_leves_peso} kilos.' if len(pessoas_leves_peso) >0 else 'não teve pessoas leves.')




    