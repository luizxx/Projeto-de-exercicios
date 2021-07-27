continuar = 'i'
produtos_1000 = 0
menor = 0
produto_menores = 'l'
produto_menoress = 'l'
total_produtos = 0
preco = 0 
preco1 = 'l'
preco2 = 'l'
cont = 0
cont_fechar = 0
while True:
    continuar = ''
    cont_fechar = 0

    nome =  input('Nome: ' )
    preco = float (input('Preço: ' ))
    cont = cont +1
    if cont == 1 or menor > preco :
        menor = preco
        cont_menor = nome
    elif preco > 1000 :
        produtos_1000 = produtos_1000 + 1
    total_produtos = preco + total_produtos
    produto_menores = nome 

    if cont == 1 or preco < menor :
        menor = preco
        cont_menor = nome
    while  True:
        continuar = input ('Deseja continuar ? (S/N) ' ).lower().strip()[0]
        cont_fechar = cont_fechar +1
        if continuar == 'n' or cont_fechar >3 :
               break

        elif continuar == 's':
            break
    if continuar == 'n'or cont_fechar >3 :
        if continuar == 'n':
            break
        elif cont_fechar >3 :
            print('Numero de tentativas muito alto, encerrando programa.')
            break
        
 




print(f'O total da compra foi de {total_produtos} e fora comprados {produtos_1000} produtos acima de 1000 reas \n e o produto mais barato foi o {cont_menor} custando {menor:.0f} ', ('reais') if menor >1 else ('real') )


    