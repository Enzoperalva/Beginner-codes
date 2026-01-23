import time

print('VAMOS VER SE UM NÚMERO É PRIMO!')
num= int(input('Dígite um número:'))
primo= 0
for c in range(1, num+1):
    if num % c== 0:
        print(f'\033[32m')
        primo+=1
    else:
        print('\033[31m \033[m')
    print(f'{c}')
    time.sleep(0.7)
print(f'\n\033[mO número {num} foi dividido {primo} vezes!')
print('PORTANTO...')
time.sleep(1.5)
if primo == 2:
    print('\033[32mELE É PRIMO!\033[m')
else:
    print('\033[31mELE NÃO É PRIMO!\033[m')