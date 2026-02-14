import statistics

lista= list()
while True:
    nota= float(input('Nota:'))
    continuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    lista.append(nota)
    while continuar not in 'SN':
        continuar = str(input('TENTE NOVAMENTE.Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'Maior nota da lista: {max(lista)}')
print(f'Lista em ordem crescente: {sorted(lista)}')
print(f'A media da lista é {statistics.mean(lista)}')