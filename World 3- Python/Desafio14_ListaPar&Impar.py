valores= 0
salvar_dados= [[], []]
for p in range(0, 7):
    valores=(int(input(f'Valor {p+1}:')))
    if valores % 2 == 0:
        salvar_dados[0].append(valores)
    else:
        salvar_dados[1].append(valores)
print(f'Pares: {sorted(salvar_dados[0])}')
print(f'Impares: {sorted(salvar_dados[1])}')