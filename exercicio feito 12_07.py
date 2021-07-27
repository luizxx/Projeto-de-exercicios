lista = list()
pos = 0
for c in range (0,5):
    n = int (input('Digite algum numero'))
    if c == 0:
        lista.append(n)
        print('Adicionado ao primeiro da lista')
        
    elif n > lista[-1]:  # esse lista[-1] ele ta dizendo que se n for menor que o ultimo da lista ele passa no criterio, [-1] é igual ao ultimo da lista
        lista.append(n)
        print('Valor adicionar ao final da da lista')

    
    else:
        
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n )
                print(f'Valor adicionado ao valor {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')

            
# exercicio muuito dificil, no futuro quando estiver mais experientei irei retornar aqui para termina-lo do meu jeito sem copiar..

 