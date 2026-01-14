'''from math import sqrt
name= input('Olá, como posso te chamar?')
print (f'Ok {name}, vamos calcular a hipotenusa de um triangulo retângulo:')
cato= float(input('Qual o valor do cateto oposto:'))
cata= float(input('Qual o valor do cateto adjacente'))
n1= cato * cato
n2= cata * cata
n3= n1+ n2
print (f'Tendo {cato} como seu cateto oposto, {cata} como adjacente temos {sqrt(n3):.2f} como hipotenusa!')'''

#Essa aqui é uma forma mais fácil de fazer o calculo da hipotenusa:

from math import hypot
co= float(input('Digíte o valor do cateto oposto:'))
ca= float(input('Digíte o valor do cateto adjacente:'))
print (f'Tendo {co} como cateto oposto, {ca} como cateto adjcaete, temos {hypot(co, ca)} como hipotenusa!')