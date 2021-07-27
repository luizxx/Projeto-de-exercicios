valores = []
maior = 0
menor = 0
for c in range(0,5):
   valores.append( int (input (f'Digite um valor para a posicao [{c+1}]  ' )))
   if c == 0:  # se nao tiver rodado nenhum numero ainda o c sera 0 obviamente.
      maior = menor = valores[c] # se c for zero significa que o maior e o menor tambem é.. isso serve para achar maior e menor numero usando for
   else: 
      if valores[c] > maior : # se o c for maior que o maior entao maior recebera o valor em c
         maior = valores[c]
      if valores[c] < menor : # mesma coisa aqui
         menor = valores[c]
print(f'Voce digitou os valores {valores}')
print(f'O maior valor encontrado foi {maior} nas posições',end='')
for i,v in enumerate(valores):
   if v == maior :
       print(f' ({i+1})', end='' )

       
print(f'\nO menor valor encontrado foi {menor} nas posições',end='')
for i,v in enumerate (valores):
   if v == menor :
      print(f' ({i+1})', end='' )
print()
   #ordem_menor = valores.index(menor)+1
   #ordem_maior = valores.index(maior)+1

   
#print(f'entre os numeros digitados {valores} \no maior valor foi {maior} o menor foi {menor} \no menor valor esta na posicao {valores.index(menor)+1} já o maior esta na posicao {valores.index(maior)+1} ')
#nesse print ele procura usando i index o valor da variavel maior e menor na variavel valores atraves das f'strings.