luiz = 'mamara'
otavio = 'luiz'
senha1 = luiz
usuario1 = otavio
usuario = 'l'
senha = 'j'

while usuario != usuario1 and senha != senha1:
    usuario = input('NOME DE USUÁRIO: ' )
    senha = input('SENHA: ' )
    print('USUÁRIO OU SENHA INCORRETO.')
print('Parabéns, você fez loguin.')
break
