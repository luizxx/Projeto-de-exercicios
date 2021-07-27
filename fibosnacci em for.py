termos = int (input('Digite quantas fibonasccis deseja.'))
t1 = 0
t2 = 1
cont = 0 
t3 = 0

for c in range(t3,termos):
    t3 = t1 + t2 # t3 vai receber t2 mais t1
    t1 = t2 # para nao fica em loop t1 vai receber t2 em seguinda
    t2 = t3  # depois t2 recebe t3
    print(t3)
    cont += +1