import time

#INTERAÇÃO:
print('-='*16)
print('\033[36mVAMOS CALCULAR A MÉDIA DO ALUNO!\033[m')
print('-='*16)
time.sleep(1)

#VARIÁVEIS:
name= str(input('Qual o nome do aluno:')).capitalize()
num1= float(input('Primeira nota:'))
num2= float(input('Segunda nota:'))
media= (num1 + num2) / 2

#INTERAÇÃO:
print('\033[35mCALCULANDO...\033[m')
time.sleep(1.6)

#CONDIÇÕES:
if media >= 7:
    print(f'{name} foi \033[32mAPROVADO\033[m, com sua média de {media:.1f}')

elif 5 <= media < 7:
    print(f'{name} ficou de \033[33mRECUPERAÇÃO\033[m, com sua média de {media:.1f}')

elif media < 5:
    print(f'{name} infelizmente \033[31mREPROVOU\033[m de ano!')
    print(f'Sua média foi de {media:.1f}')
