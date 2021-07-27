n = -1
cont = 0 
falso= True
continua='p'
while True:
    while n >=0 or n <=15:
        
        n = int (input('Digite um numero de 0 até 15.'))
        continua ='p'
        if n <0 or n >15:
            print('Digitou errado, tente novamente')
            falso= falso
            cont += +1
            break
        if falso == True:
            tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
            'Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze ','Quinze')
            print('Voce digitou ',tupla[n])
            cont = 0 

        while continua !='s':
            continua = input('Voce quer continuar? [S/N]')
            if continua =='s' or continua =='n':
                if continua =='n':
                    break
            
        if continua =='n':
            break
    if continua =='n':
        print('Encerrando')
        break
    if cont >4:
        print('Atingiu o nivel de tentativas maximas, o programa foi encerrado.')
        break
   