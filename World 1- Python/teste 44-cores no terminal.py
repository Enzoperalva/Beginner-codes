'''
\033[0;30;41m #Fundo vermelho, letra branca e fonte padrão
\033[4;33;44m #fundo azul, letra amarela e fonte sublinhada
\033[1;35;43m #Fundo amarelo, letra rosa e fonte negrito
\033[30;42m #Fundo verde, letra branco fonte padrão
\033[m #Configuração padrão do terminal
\033[7;30m #O 7 inverte  cor 30 que é preta e deixa a letra preta e o fndo branco!
'''

#PRÁTICAAAAA:
print ('\033[7;33;44mHello, World!\033[m') #Esse \033[m no final é para a cor do fundo so ir até ali!!
name= str(input('Qual o seu nome?'))
verde= '\033[1;32m'
fim= '\033[m'
print(f'Prazer em te conhecer {verde}{name}{fim}')

#Forma mais organizada de cores!!!

name1= str(input('Qual seu nome?'))
cores={'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoebranco':'\033[7;30m'}
print(f'Olá {cores ['azul']} {name} {cores['limpa']}')