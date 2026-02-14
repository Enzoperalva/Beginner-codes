ficha= list()
i=0
i1=0
i2=1
while True:
    name= str(input('Nome do aluno:'))
    nota1= float(input('Nota 1:'))
    nota2= float(input('Nota 2:'))
    media = (nota1+nota2) / 2
    ficha.append([name, [nota1, nota2], media])
    continuar= str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        print('TENTE NOVAMENTE')
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
print('-='*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-='*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')
while True:
    print('_'*35)
    opc= int(input('MOstrar notas de qual aluno? (999 interrompe)'))
    if opc==999:
        break
    if opc <=len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')