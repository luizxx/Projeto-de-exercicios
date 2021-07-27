palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')
for c in palavras:

    print(f'\n{c}  temos as vogais',end=' ')
    for palavras in c:
        if palavras in 'AEIOU':
            print(palavras,end=' ')