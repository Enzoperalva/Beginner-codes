import time
n= int(input('Digíte algum número, e vamos descobrir se ele é impar ou par:'))
n2= n % 2
print('PENSANDO...')
time.sleep(2)
if n2 == 1:
    print ('Seu número é IMPAR!')
else:
    print('Seu número é PAR!')