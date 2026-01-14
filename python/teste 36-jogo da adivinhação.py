import time, random

print('Vamos jogar um jogo da adivinhação?')
time.sleep(1)
print('--' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('--' * 20)
print('PROCESSANDO...')
time.sleep(2)
num= random.randint (0, 5)
n1= str(input('Em qual número eu pensei?'))
if n1 == num:
    print('Parabens voce acertou o número que eu pensei!')
else:
    print(f'Você errou, eu pensei no número {num}')