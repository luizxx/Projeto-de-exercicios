import random 
print('Vamos Jogar impa ou par agora beleza')
cont = 0

while True:
    valor = int  (input('Digite um valor.'))
    impar_par = input('Par ou Impar ? [P/I]').strip().lower()[0]
    maquina = random.randint(1,10)
    
    valorf = valor + maquina
    resultado = valorf % 2 
    
     
    if resultado == 0 :
        if impar_par == 'p' :
            print(f'Você escolheu PAR e jogou {valor}  e o computador {maquina}, portanto deu PAR e voce venceu')
            cont = cont + 1
            resultado = 0 
        elif impar_par == 'i' :
            print(f'Você escolheu IMPAR e jogou {valor} e o computador {maquina}, portanto deu PAR e voce PERDEU')
            print(f'voce tentou {cont} vezes')
            break 
    elif resultado > 0:
        if impar_par == 'p' :
            print(f'Você escolheu PAR e jogou {valor} e o computador {maquina}, portanto deu IMPAR e voce PERDEU')
            print(f'voce tentou {cont} vezes')
            break
        elif impar_par == 'i' :
            print(f'Você escolheu IMPAR e jogou {valor} e o computador {maquina}, portanto deu IMPAR e voce venceu')
            cont = cont +1
            resultado = 0 
    else : print('Encontramos um erro.')
    


 
     
