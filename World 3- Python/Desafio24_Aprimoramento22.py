jogador= dict()
partidas= list()
time=list()
while True:
    jogador.clear()
    jogador['nome']= str(input('Nome do jogador: '))
    tot= int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Gols no jogo {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total']= sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERROR! Digíte S ou N.')
    if continuar == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i,a in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in a.values():
        print(f'{str(d):<15}', end='')
    print()
print('_'*30)
while True:
    opc= int(input('Mostrar qual jogador? (999 interrompe)'))
    if opc == 999:
        break
    if opc >=len(time):
        print(f'ERRO! Não existe jogador do código {opc} ')
    else:
        print(f'-- ESTATISTICAS JOGADOR {time[opc]["nome"].upper()}')
        for i,g in enumerate(time[opc]["gols"]):
            print(f'     No jogo {i+1} fez {g} gols')
print('_'*30)
print('<<< VOLTE SEMPRE >>>')
