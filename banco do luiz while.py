l = 'Bem vindo ao banco do Luiz.'
ll = len(l)

print('='*ll)
print('Bem vindo ao banco do Luiz.')
print('='*ll)
valor = int (input('Digite o valor que você deseja sacar (inteiros)'))
total = valor 
cedulas = 50
cont_cedulas = 0
c50 = 0
c20 = 0
c10 = 0
while  True  :
    if total >= cedulas:
        total -= cedulas 
        cont_cedulas += +1
    else:
        if cont_cedulas > 0 :
           print(cont_cedulas, 'cedulas' if cont_cedulas >1 else 'cedula',  'de' ,cedulas, 'reais' if cedulas >1 else 'real')
          

        elif cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1

        cont_cedulas = 0

        if total  ==0: 
            break
            
        



