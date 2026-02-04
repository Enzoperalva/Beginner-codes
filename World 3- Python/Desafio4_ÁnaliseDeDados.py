num= (int(input('Valor 1:')),
           int(input('Valor 2:')),
           int(input('Valor 3:')),
           int(input('Valor 4:')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes!')
if 3 in num:
    print(f'O 1° valor 3 está na {num.index(3)+1}° posição ')
else:
    print('O valor 3 não apareceu em nenhuma posição! ')
print('Os valores pares foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end= ' ')