'''name= str(input('Qual é o seu nome?'))
tempo= int(input('Quantos anos seu carro tem?'))
if tempo <= 3:
    print(f'Caramba {name}, seu carro está novinho ein')
else:
    print(f'Já está na hora de trocar ein {name} akakkakakakkaka')
print ('Fim')'''

#Condição simplificada (Mas não recomendo pois não da para entendder os blocos, fica meio confusa)

'''tempo= int(input('Quantos anos seu carro tem?'))
print('carro novo'if tempo<=3 else'carro velho')
print('--FIM--')'''

#Teste classico de notas:
n1= float(input('Me fale a nota da sua primeira unidade:'))
n2= float(input('A da segunda:'))
n3= float(input('A da terceira:'))
n4= float(input('A da quarta:'))
n5= n1+n2+n3+n4
n6= n5 / 4
print (f'Sua média foi {n6:.1f}')
if n6 >=6:
    print('Parabens, você se livrou da recuperação!')
else:
    print ('HAHAHAHAHHA se lascou, boa sorte na recuperação!')