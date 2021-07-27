
n1 = int  (input('Digite um valor'))
n2 = int  (input('Digite um valor'))
n3 = int  (input('Digite um valor'))
n4 = int  (input('Digite um valor'))
v1 = n1 % 2 
numeros = 0 



print ('pares:',end=' ')
if v1 == 0:
    vv1 = n1
    print(vv1,end=',')
v2 = n2 % 2 
if v2 == 0:
    vv2 = n2 
    print(vv2,end=',')

v3 = n3 % 2
if v3 == 0:
    vv3 = n3
    print(vv3,end=',') 
v4 = n4 % 2 
if v4 == 0:
    vv4 = n4
    print(vv4,end='')



    
numeros = (n1,n2,n3,n4)
valor9 = numeros.count(9) #mostra quantas x 9 aparece
if n1 !=3 and n2 !=3 and n3 !=3 and n4 != 3:
   print('')
   valor3 = -1
else:
   valor3= numeros.index(3)
if valor3 == -1 or valor9 ==0:
    if valor3== -1 and valor9 >0:
       print(f'\n valores digitados foram {numeros} \n o valor 9 apareceu {valor9}' , 'vezes' if valor9 >1 else 'vez' ,'\nO valor 3 não apareceu. ') # mostra qual a 1 posicao q o 3 aparece
    elif valor9 == 0 and valor3 >=0:
       print(f'\nvalores digitados foram {numeros} \no valor 9 não apereceu nenhuma vez.\n o valor 3 apareceu na ', f'{valor3+1}' if valor3 >2 else f'{valor3+1}','posição')
    elif valor9 == 0 and valor3 == -1:
       print(f'\n valores digitados foram {numeros}\no valor 9 não apereceu nenhuma vez.\n o valor 3 tambem esta em nenhuma posição. ')
    






else: print(f'\nvalores digitados foram {numeros} \no valor 9 apareceu {valor9}', 'vezes' if valor9 >1 else 'vez' , f'\no valor 3 apareceu na',f'{valor3+1}' if valor3 >2 else f'{valor3+1}','posição') # mostra qual a 1 posicao q o 3 aparece

3
#QF503907518BR
#QF556234226BR