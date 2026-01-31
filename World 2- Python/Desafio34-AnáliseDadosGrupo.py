import time
contador_idade=0
contador_homem=0
contador_mulher=0

while True:
    print('='*20)
    print('CADASTRO DE PESSOAS!')
    print('='*20)
    sexo= str(input('Qual o sexo [M/F]:')).upper().strip()[0]
    if sexo == 'M' or sexo == 'm':
        contador_homem += 1
    while sexo != 'M' and sexo != 'F':
        print('\033[31mDIGITE CERTO!\033[m')
        time.sleep(1)
        sexo= str(input('Qual o sexo [M/F]:')).upper().strip()[0]
        if sexo == 'M':
            contador_homem+=1
    idade= int(input('Idade:'))
    if idade >= 18:
        contador_idade+=1
    if sexo == 'F' and idade < 20:
        contador_mulher += 1
    continuar= str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    while continuar != 'S' and continuar != 'N':
        print('\033[31mDIGITE CERTO!\033[m')
        time.sleep(1)
        continuar = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        break
print('\033[36m=======FIM DO PROGRAMA=======\033[m')
print(f'Pessoas cadastradas com mais de 18 anos: \033[32m{contador_idade}\033[m')
print(f'Homens cadastrados: \033[32m{contador_homem}\033[m')
print(f'Mulheres com menos de 20 anos cadastradas: \033[32m{contador_mulher}\033[m')