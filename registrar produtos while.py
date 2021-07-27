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
while True:
    continuar == ''

    nome =  input('Nome: ' )
    preco = float (input('Preço: ' ))
    if preco > 1000 :
        produtos_1000 = produtos_1000 + 1
    total_produtos = preco + total_produtos
    produto_menores = nome 

    if preco == 1 or preco < cont :
        menor = preco
        cont_menor = nome
        
    while  continuar != 'n' or continuar != 's':
          continuar = input ('Deseja continuar ? (S/N) ' ).lower().strip()[0]
          if continuar == 's':
            break
          if continuar == 'n':
            break
    if continuar == 'n':
        break




print(f'O total da compra foi de {total_produtos} e fora comprados {produtos_1000} produtos acima de 1000 reas \n e o produto mais barato foi o {produto_menores}')
print(preco1, preco2)

    