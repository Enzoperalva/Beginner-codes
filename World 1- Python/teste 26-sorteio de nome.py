import random
print('Vamos fazer o sorteio um dos seus 4 alunos para apagar o quadro')
aluno= input('Escreva o nome do primeiro aluno:')
aluno2= input('O do segundo aluno:')
aluno3= input('O do terceiro:')
aluno4= input('O do quarto:')
print('Certo, vamos sortea:')
lista= [aluno, aluno2, aluno3, aluno4]
so= (random.choice (lista))
print(f'E o aluno sorteado foi o: {so}')