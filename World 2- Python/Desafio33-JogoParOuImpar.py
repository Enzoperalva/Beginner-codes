import random, time
print('=-'*20)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-'*20)
count=0
while True:
    bot = random.randint(1, 10)
    valor= int(input('Diga um valor:'))
    escolha= str(input('Par ou Impar? [I/P]')).upper().strip()[0]
    print('=='*20)
    soma=bot+valor
    count=+1
    if soma % 2 == 0 and escolha =='P':
        print('\033[32mGANHADOR!\033[m')
        print('Vamos jogar novamente...')
        time.sleep(1)
    elif soma % 2 == 1 and escolha =='I':
        print('\033[32mGANHADOR!\033[m')
        print('Vamos jogar novamente...')
        time.sleep(1)
    else:
        print('\033[31mPERDEDOR')
        print(f'Você me ganhou {count-1} vezes...')
        break