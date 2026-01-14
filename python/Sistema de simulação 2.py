'''#TELA INICIAL
import time
print('Vamos ver a situação do aluno')
sim= str(input('Você quer continuar?')).lower()

if sim == 'sim':
    name= str(input('Qual é seu nome'))
    idade= int(input('Quantos anos você tem?'))
    turno= str(input('Qual seu turno (manhã, tarde ou noite? ')).lower()
    print('Vamos calcular sua média:')
    time.sleep(2)
    n1= float(input('Nota primeira unidade:'))
    n2= float(input('Nota da segunda unidade:'))
    n3= float (input('Nota da terceira unidade:'))
    n4= float(input('Noata da quarta unidade:'))
    media1= n1+n2+n3+n4
    mediatotal= media1 / 4

    if mediatotal >= 7:
        aprovado= 'aprovado'
        print('Parabéns, você foi aprovado')

    if 5 <= mediatotal < 7 and mediatotal == 6 and turno == 'noite':
        aprovado= 'recuperação'
        print('Infelizmente você está na recuperação, ESTUDADE MAIS e aguarde as provas!')

    if mediatotal < 5:
        aprovado= 'repetiu'
        print('Se lascou, repetiu de ano! Boa sorte no proximo ano.')

    print(f'Seu nome: {name}')
    print(f'Sua idade: {idade}')
    print(f'Seu turno: {turno}')
    print(f'Suas notas: {n1}, {n2}, {n3} e {n4}')
    print(f'Sua média é: {mediatotal}')
    print(f'Situação final: {aprovado}')
else:
    print('Tranquilo, tenha um bom dia!')'''



    #COREÇÃO INTELIGENCIA ARTIFICIAL:
import time

print('Vamos ver a situação do aluno')
sim = input('Você quer continuar? ').lower()

if sim == 'sim':
    name = input('Qual é seu nome? ')
    idade = int(input('Quantos anos você tem? '))
    turno = input('Qual seu turno (manhã, tarde ou noite)? ').lower()

    # ERRO 4: turno não validado
    if turno != 'manhã' and turno != 'tarde' and turno != 'noite':
        print('Turno inválido. Programa encerrado.')
    else:
        print('Vamos calcular sua média:')
        time.sleep(2)

        n1 = float(input('Nota primeira unidade: '))
        n2 = float(input('Nota da segunda unidade: '))
        n3 = float(input('Nota da terceira unidade: '))
        n4 = float(input('Nota da quarta unidade: '))

        mediatotal = (n1 + n2 + n3 + n4) / 4

        # ERRO 3: variável precisava existir antes
        aprovado = ''

        # ERRO 2: if separados → corrigido com elif
        # ERRO 1: regra do turno noite corrigida
        if mediatotal >= 7:
            aprovado = 'Aprovado'

        elif mediatotal >= 6 and turno == 'noite':
            aprovado = 'Aprovado'

        elif mediatotal >= 5:
            aprovado = 'Recuperação'

        else:
            aprovado = 'Reprovado'

        print(f'Seu nome: {name}')
        print(f'Sua idade: {idade}')
        print(f'Seu turno: {turno}')
        print(f'Suas notas: {n1}, {n2}, {n3} e {n4}')
        print(f'Sua média é: {mediatotal:.2f}')
        print(f'Situação final: {aprovado}')

else:
    print('Tranquilo, tenha um bom dia!')
