vel= float(input('Qual a velocidade do veículo?'))
if vel > 80:
    n= vel - 80
    n1= n *  7
    print(f'Você foi multado por percorrer a {vel:.0f} km e o valor dela é R${n1:.2f}')
else:
    print('Tenha um bom dia, dirija com segurança!')