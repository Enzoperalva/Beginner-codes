soma=0
validas=0
maior_de_idade=0
while True:
    idade= int(input('Idade:'))
    if idade>0:
        soma+=idade
        validas+=1
        if idade>=18:
            maior_de_idade+=1
    elif idade<0:
        print('INVÁLIDA')
    else:
        break
if validas>0:
    media= soma / validas
    percentual= (maior_de_idade / validas) * 100
else:
    media=0.0
    percentual=0.0
print(f'Idades válidas: {validas}')
print(f'A média das idades é: {media:.2f}')
print(f'Tem aproximadamente {percentual:.1f} por cento de jovens com ou mais de 18 anos!')