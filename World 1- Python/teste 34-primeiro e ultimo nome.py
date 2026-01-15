'''name= str(input('Digíte seu nome:')).strip()
first= name.split('0')
last= name.split('-1')
print(f'Seu nome inteiro é: {name}')
print(f'Seu primeiro nome é: {first}')
print(f'Seu último nome é: {(name[len(last)-1])}')'''
 
#Codigo corrijido Ia

name= str(input('Digite seu nome:')).strip()
partes= name.split()
fisrt= partes[0]
lsat= partes[-1]
print(f'Seu nome é: {name}')
print(f'Seu primeiro nome é: {fisrt}')
print(f'Seu ultimo nome é: {lsat}')