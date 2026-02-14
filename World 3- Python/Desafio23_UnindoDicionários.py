galera= list()
pessoa= dict()
soma=media=0
while True:
    pessoa.clear()
    pessoa['nome']= str(input('Nome: '))
    while True:
        pessoa['sexo']= str(input('Sexo: [M/F]')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERROR! Digíte apenas M ou F.')
    pessoa['idade']= int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continuar= str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERROR! Digíte apenas S ou N.')
    if continuar == 'N':
        break
print('-='*30)
print(f'-- O grupo tem {len(galera)} pessoas.')
media= soma / len(galera)
print(f'-- A média de idades é de {media:.2f}')
print(f'-- As mulhere cadastradas foram: ', end=' ')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end='')
print()
print('-- Pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('ENCERRADO')