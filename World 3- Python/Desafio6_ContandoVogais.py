palavras= ('Aprender','Programar','Estudar','Chorar',
           'Descansar','Sofrer','Solidao','python')
c=0
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')