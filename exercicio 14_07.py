Lista1 = list()
pares = list()
impares = list()
Lista = list()
Permissao = True
while True:
    if  Permissao ==True :
        Lista1 = int(input('DIGITE UM VALOR'))
        if Lista1 % 2 == 0 :
            pares.append(Lista1)
        elif Lista1 % 2 >0:
            impares.append(Lista1)
        Lista.append(Lista1) 
        
    conti = input('Deseja continuar?').lower().strip()[0]
    if conti =='s':
        Permissao = True
    else:
        if conti =='n':
            print('Saindo do programa')
            Permissao == False
            break
        if conti not in 'n' or conti not in 's':
            print('Valor digitado erradamente, digite apenas "Sim" ou "Não. ')
            Permissao = False
print(f'Os valores digitados foram {sorted(Lista)} \n', f'Os valores pares ficaram numa lista diferente que é a {pares}' if len(pares) >0 else 'Não teve nenhum numero par nessa lista.', '\n', f'Os valores impares ficaram numa lista diferente que é a {impares}' if len(impares)>0 else 'Não teve nenhum numero impar nessa lista.')
      



