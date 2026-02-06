valores= list()
maior= menor= 0
cont_maior=cont_menor=0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c,v in enumerate(valores):
    print(f'Na posição {c} temos o valor {v}')
posicao1=valores.index(max(valores))
posicao2=valores.index(min(valores))
print(f'O maior valor é {max(valores)} e está na posição {posicao1}')
print(f'O menor valor é {min(valores)} e está na posição {posicao2}')