print('Olá, vamos fechar a conta do seu aluguel?')
n= float(input('Blz, vamos lá. Quantos km foram rodados: '))
n1= (n * 0.15)
n2= float(input('Quantos dias alugados:'))
n3= n2 * 60
print (f'Você teve {n} km rodados, {n2} dias alugados, que da um total de R${n1+n3}')