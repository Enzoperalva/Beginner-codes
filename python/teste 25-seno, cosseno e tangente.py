from math import sin, cos, tan, pi
print('Vamos ver o valor do seno, cosseno e da tangente')
an= float(input(('Informe aqui o valor do ângulo:')))
print ('Como nosso querido python não lê os produtos em graus, vamos transformar ele em radianos')
rad= an * (pi / 180)
print(f'O valor é {sin (rad):.2f} seno, {cos(rad):.2f} cosseno e {tan(rad):.2f} tangente!')