valores= []
maior= menor= 0
cont_maior=cont_menor=0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para posição {cont}:')))
maior= max(valores)
menor= min(valores)
print('=-='*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {max(valores)} nas posições',end= ' ')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor é {min(valores)} nas posições', end=' ')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()