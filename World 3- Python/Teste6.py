'''teste= list()
teste.append('Gustavo')
teste.append(40)
galera=list()
galera.append(teste[:])
teste[0]= 'Maria'
teste[1]= 22
galera.append(teste[:])
print(galera)'''

galera= [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 45]]
for p in galera:
    print(f'{p[0][1]} tem {p[1]} anos de idade!')


'''galera=list()
dado= list()
total_maior= total_menor= 0
for c in range(0,3):
    dado.append(str(input('Qual é o seu nome:')))
    dado.append(int(input('Quantos anos você tem:')))
    galera.append(dado[:])# Sem esses dois pontos o dado e a galera ficam ligados, ai o clear apaga os dois, por isso precisa dos dois pontos
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f'{p[0]} é maior de idade.')
        total_maior+=1
    else:
        print(f'{p[0]} é menor de idade')
        total_menor+=1
print(f'Tem {total_maior} maior de idade\n'
      f'Tem {total_menor} menor de idade')'''