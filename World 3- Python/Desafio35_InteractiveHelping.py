from time import sleep
while True:
    def visu(msg,cor):
        print(f'\033[7;{cor}m')
        help(msg)
        print('\033[m')

    def esc(msg,cor):
        print(f'\033[1;{cor}m~' * (len(msg) + 4))
        print(f'  {msg}')
        print('~' * (len(msg) + 4 ))
        print('\033[m')


    esc('SISTEMA DE AJUDA PyHELP', 42)
    n = str(input('Função ou biblioteca > '))
    if n == 'fim':
        esc('ATÉ LOGO!', 41)
        break
    esc(f"Acessando manual do comando '{n}'", 44)
    sleep(0.6)
    visu(n,40)
    sleep(2)

#Resolução guanabara
from time import sleep
c= ('\033[m',          # 0 - Sem cor
    '\033[7;40m',      # 1 - Branco
    '\033[0;30;41m',   # 2 - Vermelhor
    '\033[0;30;42m',   # 3 - Verde
    '\033[0;30;43m',   # 4 - Amarelo
    '\033[0;30;44m',   # 5 - azul
    '\033[0;30;45m',   # 6 - Roxo
    '\033[7;30m')      # 7 - Preto

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 5)
    print(c[1], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg,cor=0):
    print(c[cor], end='')
    print('~' * (len(msg)+4))
    print(F'  {msg}')
    print('~' * (len(msg)+4))
    print(c[0], end='')
    sleep(1)

comando= ''
while True:
    titulo('SISTEM DE AJUDA PyHELP', 3)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 2)