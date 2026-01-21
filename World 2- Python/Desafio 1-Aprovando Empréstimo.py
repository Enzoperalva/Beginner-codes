import time

#INTERAÇÃO:
name= str(input('Seja bem vindo, qual o seu nome?'))
print(f'Prazer em te conhecer {name.capitalize()}. Agora sim podemos começar!')
time.sleep(2)

print('-='*15)
print('\033[37mVAMOS ANALISAR O EMPRÉSTIMO:\033[m')
print('-='*15)
time.sleep(1)

#VARIÁVEI:

preco= float(input('Qual o preço do ímovel: R$'))
salario= float(input('Qual o seu salário: R$'))
parcela= int(input('Em quantos anos você quer pagar:'))

#CÁLCULOS:

mensal= preco / (parcela * 12)
taxa= salario * 0.3


#CONDIÇÕES/ PARTES FINAIS:

if mensal >= taxa:
    print(f'\033[31mEMPRÉSTIMO NEGADO\033[m')
    print(f'Para pagar uma casa de R${preco:.2f} em {parcela} anos a prestação será de R${mensal:.2f}')
else:
    print(f'\033[32mParabéns {name}, seu empréstimo foi aprovado! \033[m')