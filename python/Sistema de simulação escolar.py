#TELA INICIAL:
import time
print('Olá eu sou o simulador escolar')
time.sleep(1)
print('Seja bem-vindo ao meu programa!')
time.sleep(1)
sim= str(input('Deseja continuar?')).lower()

if sim == 'sim':
    print('-=' *20)
    print('Certo, vamos realizar seu cadastro <3')
    print('-=' *20)

    name= str(input('Qual seu nome?'))
    idade= int(input('Qual sua idade?'))
    escola= str(input('Qual sua escola?'))
    cidade= str(input('Qual sua cidade?'))

    print('Agora vamos para área acadêmica!')
    time.sleep(1)

    n1= float(input('Nota primeira unidade:'))
    n2= float(input('Nota segunda unidade:'))
    n3= float(input('Nota terceira unidade:'))
    media= (n1+n2+n3) / 3

    print('PROCESSANDO...')
    time.sleep(2)
    if media >= 6:
        resultado= 'aprovado'
        print(f'Sua média: {media}')
        print('Média exigida: 6')
        print('Você foi aprovado, meus parabens!')

    else:
        print(f'Infelizmente sua média de {media} não foi a mínima alcançada, ESTUDE e tente novamente')
        resultado= 'reprovado'

    print('RESULTADO FINAL:')
    print('PROCESSANDO...')
    time.sleep(2)
    print(f'Nome: {name}')
    print(f'Idade: {idade}')
    print(f'Escola: {escola}')
    print(f'Notas: {n1}, {n2}, {n3}')
    print(f'Média: {media}')
    print(f'Média exigida: 6')
    print(f'Situação final: {resultado}')

else:
    print('Tranquilo fica para próxima, tenha um ótimo dia!')