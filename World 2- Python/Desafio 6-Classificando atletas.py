from datetime import date
import time

#INTERAÇÃO:
print('-='*13)
print('\033[36mVAMOS VER SUA CATEGORIA..\033[m')
print('-='*13)
time.sleep(1)

#VARIÁVEIS:
nasc= int(input('Em qual ano você nasceu:'))
ano= date.today().year
idade= ano - nasc
time.sleep(0.5)
#CONDIÇÕES:
if idade <= 9:
    print(f'Você tem {idade} anos e é classificado como MIRIM!')

elif 9 < idade <= 14:
    print(f'Você tem {idade} anos e é classificado como INFANTIL!')

elif 14 < idade <= 19:
    print(f'Você tem {idade} anos e é classificado como JUNIOR!')

elif 19 < idade <= 25:
    print(f'Você tem {idade} anos e é classificado como SÊNIOR!')

else:
    print(f'Você tem {idade} anos e é classificado como MASTER!')