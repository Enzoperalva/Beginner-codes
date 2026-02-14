'''brasil= []
estado1= {'uf': 'Rio de Janeu', 'sigla': 'RJ'}
estado2={'uf': 'São paulo', 'sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])'''

estado= dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla']= str(input('Sigla: '))
    brasil.append(estado.copy())
    estado.clear()
'''print(brasil)
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')'''
for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()