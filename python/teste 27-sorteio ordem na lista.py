from random import shuffle
print('Ok, agora vamos sorteia a ordem de aprensentção dos seus quatro alunos!')
a1= input('Digite aqui o nome do primeiro aluno:')
a2= input('O do segundo:')
a3= input('O do terceiro:')
a4= input('O do quarto:')
a5= [a1, a2, a3, a4]
shuffle(a5)
print(f'A ordem sorteada foi: {a5}')