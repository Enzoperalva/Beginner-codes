import time
print('-=' * 22)
print('Vamos ver se os segmentos formam um triangulo')
print('-=' *22)
time.sleep(1)
n1= float(input('Primeiro segmento:'))
n2= float(input('Segundo segmento:'))
n3= float(input('Terceiro segmento:'))
print('ANALISANDO...')
time.sleep(2)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Esses segmentos FORMAM  um triângulo!')
else:
    print('Elas não formam um triangulo!')