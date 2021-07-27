continua = 'p'
valores = [] 
cinco = 5 
while continua != 'n' or continua !='s':
   valores.append(int(input('Digite um numero')))
   continua = input('Deseja continuar? [S/N]').lower().strip()[0]
   
   if continua =='n':
       print('Fechando programa')
       break
   if continua =='s':
       print('Continuando o programa.')
valores.reverse() # isso é para reverter o valor, podendo ser usado o valores.sort(reverser=True) que daria a mesma coisa.
 # valores.reverse() não ira retornar nada, vc usa isso mas ele muda a variavel, entao tera que usar só valores  

print(f'Foram digitados {len(valores)} valores \n Sendo eles {valores} \n ', 'Não teve 5 na lista.'if not 5 in valores else 'Teve 5 na lista.' )


