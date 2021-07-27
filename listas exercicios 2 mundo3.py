valores = list()
v = 0
valores_d = ''
continua = 'p'
cont =  0

permissao = True
original = valores[:]
while True:
    
    if permissao == True:
       v = int (input('Digite algum valor')) # ele pede um valor mais ainda sem adiciona a lista
       if v not in valores: # aqui dei o criterio pra ele só adicionar a lista se não estiver la, caso tenha ele não da append e o valor continuara na variavel v.
          valores.append(v) # aqui como passou no criterio que propus, ele adicionou a lista valores 
       else: # caso nao passe, aqui ele da essa mensagem e não faz nada, sem adiciona nada a lista
          print('Valor repetido anteriormente, irei excluir o mesmo.')
          cont = cont +1 # aqui e so caprixiu meu, p ele falar quantas x o usuario digitou nmr repetido

         
    continua = input('Deseja continuar? [S/N] ' ).lower().strip()[0]
    if continua =='n':
            print('Programa encerrado')
            permissao = False
            break
    if continua =='s':
            permissao = True
    else: 
        permissao = False

   
print(f'Voce digitou os valores {sorted(valores)}', f'repetiu {cont} vezes' if cont >0 else print())

   