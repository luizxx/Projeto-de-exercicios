
termos = int (input('Digite o numero de termos que você deseja calcular. '  ))
t1 = 0
t2 = 1
cont = 1

while cont <= termos : 
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    cont += +1