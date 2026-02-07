valores = list()
while True:
    n =(int(input('Cadastre algum valor:')))
    print('Valor adicionado com sucesso!')
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado, NÃO VOU ADICIONAR')
    continuar = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    while continuar != 'N' and continuar != 'S':
        continuar = str(input('Tente novamente!Deseja continuar [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        break
print('=-'*20)
valores.sort()
print(f'Valores adicionados: {valores}')