lanche= 'hamburguer', 'refri', 'pizza', 'pudim'
#TUPLAS SÃO IMUTÁVEIS
print(lanche[-3:])
print(len(lanche))

#primeira maneira de repetição:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('COMI DE MAIS!')

print('='*20)
print('OUTRA MENEIRA:')
print('='*20)

#Segunda maneira
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('COMI DE MAIS!')

#Terceira maneira
for comida in lanche:
    print(f'Eu vou comer {comida}')