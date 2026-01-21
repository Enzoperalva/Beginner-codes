import time

#INTERAÇÃO:
print('Vamos calcular seu Indice de Massa Corporal!')
time.sleep(0.8)

#VARIÁVEIS:
name= str(input('Antes de começar a calcular o seu IMC, eu preciso saber o seu nome:')).capitalize()
kg= float(input('Quantos kg você pesa:'))
altura= float(input('Qual sua altura em metros:'))
imc= kg / (altura * altura)

#INTERAÇÃO:
print('-='*6)
print('\033[36mCALCULANDO...\033[m')
print('-='*6)
time.sleep(1.5)

#CONDIÇÕES:
if imc<18.5:
    print(f'{name}, seu IMC é de {imc:.2f} e você está abaixo do peso!')
elif imc<25:
    print(f'{name}, seu IMC é de {imc:.2f} e você está no peso ideal!')
elif imc<30:
    print(f'{name}, seu IMC é de {imc:.2f} e você está com sobrepeso!')
elif imc<40:
    print(f'{name}, seu IMC é de {imc:.2f} e você está com obesidade!')
else:
    print(f'{name}, seu IMC é de {imc:.2f} e você está com obesidade morbida!')