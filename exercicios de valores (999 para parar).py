cont = s  = 0
while True:
    numero = int (input('Digite um numero inteiro (999 parar) \n R: '))
    if numero == 999 :
    
        break

    cont = cont +1
    s =  numero + s
print(f'Voce digitou {cont} numeros e soma entre les é {s}')
        
