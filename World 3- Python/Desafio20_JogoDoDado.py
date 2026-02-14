import random, time, operator
jogo = {'jogador 1': random.randint(1,6),
        'jogador 2': random.randint(1,6),
        'jogador 3': random.randint(1,6),
        'jogador 4': random.randint(1,6)}
ranking= list()
print('-='*20)
print(f'{"VALORES SORTEADOS":^40}')
print('-='*20)
for c,k in jogo.items():
    print(f'{c}: {k}')
    time.sleep(0.5)
ranking= sorted(jogo.items(), key= operator.itemgetter(1), reverse= True)
print('-='*20)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    time.sleep(1)