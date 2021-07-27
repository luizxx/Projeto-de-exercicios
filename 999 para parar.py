valores = []
nvalores = 0
m = int (input('quantos numeros você digitara?'))
while nvalores != m :
  valores.append   (int (input('Digite um numero inteiro ' )))
 
  nvalores = nvalores + 1
  if valores == [999] or nvalores == m:
       print('')
       break
v = sum(valores)
print(f'Foram digitados {nvalores} numeros sendo eles {valores}\n e a soma entre eles é {v}.')