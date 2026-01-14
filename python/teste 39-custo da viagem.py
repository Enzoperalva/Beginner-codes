km= float(input('Quantos km de distância:'))
if km <= 200:
    n= km * 0.50
    print(f'O valor para {km:.1f} quilômetros é de R${n:.1f}')
else:
    n1= km * 0.45
    print(f'O valor para {km:.1f} quilômetros é de {n1:.2f}')
print('Tenha uma ótima viagem!')