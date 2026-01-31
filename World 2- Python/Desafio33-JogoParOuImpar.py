import random, time
print('=-'*20)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-'*20)
cont1=cont2=0
while True:
    bot = random.randint(0, 10)
    valor= int(input('Diga um valor:'))
    escolha= str(input('Par ou Impar? [I/P]')).upper().strip()[0]
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [I/P]')).upper().strip()[0]
    print('=='*20)
    soma=bot+valor
    if soma % 2 == 0 and escolha =='P':
        print('\033[32mGANHADOR!\033[m')
        print('Vamos jogar novamente...')
        cont1+=1
        time.sleep(1)
    elif soma % 2 == 1 and escolha =='I':
        print('\033[32mGANHADOR!\033[m')
        print('Vamos jogar novamente...')
        cont2+=1
        time.sleep(1)
    else:
        print('\033[31mPERDEDOR\033[m')
        print(f'O computador jogou {bot} e você {valor} ')
        print(f'Você me ganhou {cont1+cont2} vezes...')
        break