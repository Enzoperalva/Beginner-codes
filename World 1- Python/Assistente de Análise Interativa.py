import time, random
#Coletar dados do usuário:

print('-=' * 20)
print('ANÁLISE DE DADOS!')
print('-=' * 20)

print('Vamos coletar alguns dados!')
frase= str(input('Digite aqui uma frase qualquer:')).lower().strip()
m1= (int(input('Digíte algum número inteiro:')))
m2= (float(input('Digíte algum número real com casa decimais:')))

print('-=' * 20)
print('\033[4;31mANALISANDO A FRASE...\033[m')
print('-=' * 20)
time.sleep(2)

#Analisando a frase:

n1= len(frase)
n2= frase.replace(' ', '')
n3= len (n2)
n4= frase.count('a')

partes= frase.split()
first= 'python' in partes [0]
last= 'programação' in partes[-1]

print(f'Na sua frase possui: {n1} caractéres, contando os espaços!')
print(f'Sem os espaços tem {n3}')
print(f'Na sua frase tem {n4} letras ''a''')
print(f'Sua frase começa com python: {first}')
print(f'Sua frase termina com programação: {last}')

#Processar os números:
print('-=' * 20)
print('\033[31mANALISANDO NÚMEROS...\033[m')
print('-=' * 20)

time.sleep(5)

soma= m1 + m2
menos= m1 - m2
vezes= m1 * m2
divisao= m1 / m2
potencia= m1 ** m2
raiz= m1 ** (1/2)
aleatorio= random.randint(1, 100)
number= m1 % 2

if m1 > 0:
    positivo= 'POSITIVO'

elif m1 < 0:
    positivo= 'NEGATIVO'

else:
    positivo= 'ZERO'

#SEPARANDO IFFFF

if number == 0:
    par= 'PAR'
else:
    par= 'ÍMPAR'

print(f'A soma de {m1} mais {m2} é: \033[36m{soma}\033[m')
print(f'A subtração de {m1} menos {m2} é: \033[36m{menos}\033[m')
print(f'A multiplicação de {m1} vezes {m2} é: \033[36m{vezes}\033[m')
print(f'A divisão de {m1} com {m2} é: \033[36m{divisao:.2f}\033[m')
print(f'O número inteiro {m1} elevado a potência do número real {m2} é igual a: \033[36m{potencia:.2f}\033[m')
print(f'A raiz quadrada do número inteiro {m1} é \033[36m{raiz:.2f}\033[m')
print(f'Aqui está um número aleatório de 1 a 100: \033[36m{aleatorio}\033[m')
print(f'O número {m1} é \033[36m{par}\033[m')
print(f'Seu número real é \033[36m{positivo}!\033[m')