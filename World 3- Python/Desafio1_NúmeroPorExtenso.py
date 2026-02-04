while True:
    extenso=('Zero','Um','Dois','três','Quatro','Cinco','Seis','Sete','Oito','Nove',
             'Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete',
             'Dezoito','Dezenove','Vinte')
    while True:
        num= int(input('Escolha um número entre 0 e 20:'))
        if 0 <= num <= 20:
            break
        print('TENTE NOVAMENTE!', end=' ')
    print(f'O número que você escolheu foi {extenso[num]}')

    continuar= str(input('Você deseja continuar [S/N]:')).upper().strip()[0]
    if continuar != 'S':
        print('OBRIGADO!')
        break