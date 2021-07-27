
valor = float (input('Digite um valor: ' ))
valor1 = float (input('Digite outro valor ' ))
funcao = 'l'
while funcao != '1' or funcao != '2' or funcao != '3' :
          funcao =  input('[1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NUMEROS \n [5] SAIR DO PROGRAMA ' )
          if funcao == '1'   :
           somar = valor + valor1 
           print(f'Resposta: \n {valor} + {valor1} =  {somar} ' )
          elif funcao == '2'    :
               multiplicar = valor * valor1
               print(f'Resposta: \n {valor} x {valor1} = {multiplicar} ' )
          elif funcao == '3' :
             if valor > valor1 :
                     print(f'{valor} é o maior numero e {valor1} o menor .')
             elif valor1 > valor :
                     print(f'{valor1} é o maior numero e {valor} o menor .')
             else:
                     print(f'Ambos valores são iguais, portanto não há diferença entre {valor1} e {valor}.')
          elif funcao == '4':
                print('Então você quer adicionar novos numeros, né.. ')
                valor = float (input('Digite um valor: ' ))
                valor1 = float (input('Digite outro valor ' ))
          elif funcao == '5':
               print('Programa encerrado pelo usuário.')
               break