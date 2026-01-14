n= input('Olá jovem garfanhoto, poderia me informar seu nome?')
print('Prazer em conhecer {:=^20}, me chamo PC e vou te ajudar a fazer alguns cálculos'.format(n))
n1= float(input('Escolha algum número:'))
n2= float(input('Escolha outro número:'))
s= n1 + n2
m= n1-n2
p= n1 * n2
i= n1 / n2
y= n1 ** n2
t= n1 // n2
r= n1 % n2
print('A soma desses números é: {}'.format(s))
print('A subtração desse números é: {}'.format(m))
print('A multiplicação desse números é: {}'.format(p))
print('A divisão desse números é: {}'.format(i))
print('A potênciação desse números é: {}'.format(y))
print('A divisão inteira desses números é: {}'.format(t))
print('O resto da divisão desses números é: {}'.format(r))
