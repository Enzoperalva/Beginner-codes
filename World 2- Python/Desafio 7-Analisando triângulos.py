import time

#INTERAÇÃO:
print('-='*27)
print('VAMOS ANALISAR SEGMENTOS, E VER SE FORMAM TRIANGULOS?')
print('-='*27)

#VARIÁVEIS:
n1= float(input('Primeiro segmento:'))
n2= float(input('Segundo segmento:'))
n3= float(input('Terceiro segmento:'))

#INTERAÇÃO:
print('ANALISANDO...')
time.sleep(1.5)

#CONDIÇÕES:
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[32mESSES SEGMENTOS FORMAM UM TRIÂNGULO!\033[m')

    if n1 == n2 == n3:
        print('Todos os lados são iguais.')
        print('Seu triângulo é EQUILÁTERO!')

    elif n1 == n2 or n2 ==  n3 or n3== n1:
        print('Dois lados são iguais.')
        print('Seu triângulo é ISÓSCELES!')

    elif n1 != n2 != n3 != n1:
        print('Todos os lados são diferentes.')
        print('Seu triângulo é ESCALENO!')
else:
    print('\033[31mESSES SEGMENTOS NÃO FORMAM UM TRIÂNGULO! \033[m')