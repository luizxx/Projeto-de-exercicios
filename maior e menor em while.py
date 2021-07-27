contador = 0 
valores = []
valores.append (int (input('Digite algum valor  '  )))
while True:
    
    contador = contador +1  
    res = input('Quer continuar? \n [1] SIM \n [2] NÃO ' )

    if res == '1':
       valores.append (int (input('Digite algum valor  ' )))

    if res == '2':

        total = sum(valores) / contador
        maximo = max(valores)
        minimo = min(valores)
        print(f'Média : {total}\n maior numero foi {maximo} e o menor \n {minimo}')

        
        break
    
    