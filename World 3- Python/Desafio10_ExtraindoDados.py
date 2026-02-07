lista= []
cinco= 5
while True:
    num= int(input('Digite um valor:'))
    lista.append(num)
    continuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar!= 'N' and continuar != 'S':
        continuar= str(input('Tente novamente. Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'A lista tem {len(lista)} números!')
print(f'Lista em ordem decrescente: {lista}')
if cinco in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O 5 não faz parte da lista')