primeiro_termo = int (input('Digite sua primeira pa'))
razao =  int (input('Digite sua razao'))
v_l = int (input('Digite quantas pas deseja ' ))
termo = primeiro_termo
cont = 0
v_v = 0
continua = '0'
while True:
     v_l = v_v + v_l
     while cont != v_l :
        print(termo)
        termo = termo + razao
        cont = cont +1
        
     
     continua = input(' ====MENU==== \n [ENTER] - REPETIR A SEQUENCIA SELECIONADA ANTERIORMENTE \n [1] ADICIONAR MAIS PAS \n [2] ALTERAR RAZÃO OU RESETAR TUDO \n [3] SAIR DO PROGRAMA '  ).strip()
     if continua =='1':
         v_v = int (input('Digite o numero a mais de pas que deseja inserir' ))
     elif continua =='2':
         funcoes_ = input('[1] TROCAR RAZAO \n [2] RESETAR TUDO')
         if funcoes_ == '1':
            razao = int (input('Digite sua nova razão. ' ))
         elif funcoes_ == '2':
             razao = 0
             primeiro_termo = 0
             v_l = 0
             cont = 0
             v_v = 0
             termo = 0
             primeiro_termo = int (input('Digite sua primeira pa'))
             razao =  int (input('Digite sua razao'))
             v_l = int (input('Digite quantas pas deseja ' ))
     if continua == '3':
         print('saindo')
         break
     