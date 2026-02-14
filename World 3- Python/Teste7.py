pessoas= {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())
for k, v in pessoas.items():
    print(f'{k} = {v}')