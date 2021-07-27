maior_de_18 = 0 
maior_de_18 = 0
mulher_menor = 0
sexo = 'o'
idade = 0 
homens_18 = 0
continuar = '0'
cont = 0
ca = 'cadastre uma pessoa'
ca1 = len(ca)
while continuar != '2' :
         if cont >3:
              break
         else:
          cont = 0 
          print ( '=' * ca1)
          print('CADASTRE UMA PESSOA')
          print( '=' * ca1 )
          idade = int (input('IDADE  R: ' ))
          while sexo not in 'f' or sexo not in 'm':
                    sexo =  input ('SEXO [F/M]\n R: '  ).strip().lower()[0]
                    cont += + 1
                    if cont >3:
                         print('numero grande de tentativas, programa encerrado.')
                         break
                    if sexo == 'm' or sexo == 'f' and cont <=3:    
                              if sexo == 'm' :
                                   homens_18 = homens_18 +1 
                              if idade > 18 :
                                   maior_de_18 = maior_de_18 +1
                              elif idade < 20 and sexo == 'f' : 
                                   mulher_menor = mulher_menor +1 
                              continuar = input('Deseja continuar ? \n [enter ou qualquer letra] - SIM \n [2] - NÃO. \n R: ' )
                              if continuar == '2' or continuar == 'n' :
                                   print(f'Tivemos {homens_18} homens  \n {maior_de_18} pessoas com mais de 18 anos \n {mulher_menor} mulheres com menos de 20 anos.')
                                   break
                              break
          