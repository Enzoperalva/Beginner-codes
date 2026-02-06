valores= list()
while True:
    valores.append(int(input('Cadastre algum valor:')))
    while valores == valores:
        print('Não repita valores:')
        valores.append(int(input('Cadastre algum valor:')))
    continuar= str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    while continuar != 'N' and continuar != 'S':
        continuar= str(input('Tente novamente!Deseja continuar [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        break