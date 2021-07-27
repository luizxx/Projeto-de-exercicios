valores = [ ]
cont = 0
valoress = valores
for c in range (0,5):
   valores.append(int (input('Digite um valor')))
   cont += +1
   if len(valores) == 1:
      print('Valor adicionado no indice 1 da lista.')
   if cont >1 or cont >2 or cont >3:
      if valores[0] < valores[1]:
         print('Sera colocado no indice 1.')
      else: print('sera colocado no indice 0')
      if cont >2:
         if valores[1] < valores[2]:
            print('Sera colocado no indice 2 ')
         else: print('Sera colocado no indice 1.')
      

print(valores)
#listas = [1,2,3,4,5]
#listas.insert(1,'luiz')
#listas.remove(3)
#print(listas)
   