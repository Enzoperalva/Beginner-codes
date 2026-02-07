lista_completa= []
par= []
impar= []
while True:
    num= int(input('Digite um valor?'))
    lista_completa.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    cotinuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while cotinuar != 'S' and cotinuar != 'N':
        cotinuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if cotinuar == 'N':
        break
print(f'Lista completa: {lista_completa}')
print(f'Lista par: {par}')
print(f'Lista impar: {impar}')