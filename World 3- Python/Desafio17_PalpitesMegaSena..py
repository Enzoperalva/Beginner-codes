import random, time
numero= []
print('__'*20)
print(f'{"JOGA NA MEGA SENA":^40}')
print('__'*20)
escolha= int(input('Quantos jogos você vai querer que eu sorteie ?'))
for c in range(escolha):
    numero.append(random.sample(range(60), k=6)[:])
    print(f'Jogo {c+1}: {numero}')
    numero.clear()
    time.sleep(1.5)
print(f'{"-=-=-=-=-=-=< BOA SORTE! >-=-=-=-=-=-=":^10}')

#Versão guanabara
import random, time
lista=list()
jogos= list()
quant= int(input('Quantos jogos você quer que eu sorteie?'))
tot=1
while tot<= quant:
    cont = 0
    while True:
        num= random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    time.sleep(1)
