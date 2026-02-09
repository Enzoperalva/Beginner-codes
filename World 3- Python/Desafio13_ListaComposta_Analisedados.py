pessoas= []
dados= []
maior=menor=0

while True:
    dados.append(str(input('Qual seu nome?')))
    dados.append(float(input('Qual seu peso?')))
    if len(pessoas) == 0:
        maior=menor=dados[1]
    else:
        if dados[1] > maior:
            maior=dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas!')
print(f'O maior peso foi {maior}KG! Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print()
print(f'O menor peso foi {menor}KG! Peso de ', end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}', end=' ')
print()