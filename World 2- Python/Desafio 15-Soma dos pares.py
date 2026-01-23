soma=0
cont=0
print('Me fale 6 números inteiros!')
for c in range(1, 7):
    num= int(input(f'Número {c}:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você me informou {cont} números pares e a soma deles é:{soma}')