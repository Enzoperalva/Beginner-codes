import time

print('-='*8)
print('TABUADA!')
print('-='*8)
n1= int(input('Você quer a tabuada de qual número:'))
n2= 0
n3= n1 * n2

print(f'A TABUADA DE {n1} AÍ!')
for c in range(1, 11):
    n2=n2+1
    print(f'{n1}x{n2}={n1*n2:.0f}')
    time.sleep(1.3)