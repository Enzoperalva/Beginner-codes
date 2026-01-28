soma=count=0
while True:
    numero = int(input('Digite um valor [PARA COM 999]:'))
    if numero == 999:
        break
    soma+=numero
    count += 1
print(f'Valores digitados: {count}')
print(f'Soma desses valores: {soma}')