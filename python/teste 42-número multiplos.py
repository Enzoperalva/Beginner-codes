import time
print('Parabéns, você ganhou um aumento!')
time.sleep(1)
n1= float(input('Informe o seu salário atual para fazermos o reajuste:'))
if n1 > 1250:
    total= n1 * 1.10
    print('ANALISANDO...')
    time.sleep(2)
    print(f'Seu aumente foi de 10%, antigo salário: {n1}, salário atual: {total:.2f}')
else:
    total= n1 * 1.15
    print('ANALISANDO...')
    time.sleep(2)
    print (f'Seu salário saiu de {n1} para {total:.2f}, parábens, seu aumente foi de 15%')