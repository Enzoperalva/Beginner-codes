import time

n1= int(input('Primeiro valor:'))
n2= int(input('Segundo valor:'))
menu= 1 and 2 and 3 and 4

while menu !=5:

    print('\033[36mMENU\033[m')
    print('\033[35m[ 1 ]\033[m SOMAR')
    print('\033[35m[ 2 ]\033[m MULTIPLICAR')
    print('\033[35m[ 3 ]\033[m MAIOR')
    print('\033[35m[ 4 ]\033[m NOVOS NÚMEROS')
    print('\033[35m[ 5 ]\033[m SAIR DO PROGRAMA')
    menu= int(input('>>>>>>Qual opção você vai escolher:'))
    if menu== 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif menu == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif menu == 3:
        if n1> n2:
            print(f'O {n1} é maior que {n2}')
        elif n2>n1:
            print(f'O {n2} é maior que {n1:}')
        else:
            print(f'{n1} e {n2} tem o mesmo valor!')
    elif menu == 4:
       n1= int(input('Primeiro valor:'))
       n2= int(input('Segundo valor:'))
    elif menu != 5:
        print('\033[31mOpção invalida!\033[m')
    print('-='*20)
    time.sleep(2)
print('Programa finalizado')