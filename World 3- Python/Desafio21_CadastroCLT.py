from datetime import date
lista= {}
lista2=list()
lista['nome']= str(input('Nome:'))
lista['idade']= int(input('Ano de nascimento: '))
lista2.append(lista['idade'])
lista['idade']= date.today().year - lista['idade']
lista['ctps']= int(input('Carteira de Trabalho (0 não tem): '))
while True:
    if lista['ctps'] == 0:
        print('-='*30)
        for k,v in lista.items():
            print(f'{k} tem valor {v}')
        break
    lista['contratação']= int(input('Ano de contratação: '))
    lista['salário:']= float(input('Sálario:'))
    idade_trabalho = lista['contratação'] - lista2[0]
    lista['aposentadoria'] = idade_trabalho + 35
    if lista['ctps']>0:
        print('-='*30)
        for k,v in lista.items():
            print(f'{k} tem valor {v}')
        break

#Resolução guanabara
from datetime import datetime
dados= dict()
dados['nome']= str(input('Nome: '))
nasc= int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps']= int(input('Carteira de trabalho (0 não tem)'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['sálario'] = float(input('Sálario: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*20)
for k,v in dados.items():
    print(f'{k} tem valor {v}')
