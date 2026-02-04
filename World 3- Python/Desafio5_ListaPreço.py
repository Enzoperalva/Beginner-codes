print('__'*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('__'*20)
lista= ('Pizza', 40,
        'Água',2,
        'Café',9,
        'Compasso',7,
        'Cavalo',1000 )
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R${lista[pos]:7>.2f}')
print('__'*20)
