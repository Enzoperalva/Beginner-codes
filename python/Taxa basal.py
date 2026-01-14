import time
name= str(input('Olá, como posso te chamar?'))
print(f'Bme-vindo {name}, para calcular sua taxa basal vou precisar de algumas informações <3')
genero= str(input('Qual seu gênero:')).lower()
if genero == 'masculino':
    peso= float(input('Qual seu peso em kg:'))
    altura= float(input('Qual sua altura em cm:'))
    idade= int(input('Qual sua idade'))
    n1= (10 * peso) + (6.25 * altura)
    n2= n1 - (5 * idade) + 5
    print('CALCULANDO...')
    time.sleep(2)
    print(f'{name},sem contar sua atividade física, você tem uma média de gasto de {n2} calorias diárias!')
else:
    peso= float(input('Qual seu peso em kg:'))
    altura= float(input('Qual sua altura em cm:'))
    idade= int(input('Qual sua idade:'))
    n1= (10 * peso) + (6.25 * altura)
    n2= n1 - (5 * idade) - 161
    print('CALCULANDO...')
    time.sleep(2)
    print(f'{name}, sem contar sua atividade física, você gasta aproximadamente {n2} calorias diárias!')