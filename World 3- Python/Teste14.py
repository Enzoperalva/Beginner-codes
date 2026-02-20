try:
    a= int(input('Numerador: '))
    b= int(input('Denominador: '))
    r= a/b
except(ValueError, TypeError): #ERROS: Dado correto mas valor improprio, Operação realizada com tipo de dado incompatível.
    print('Tivemos um problema com os tipos de dados que você digitou!')
except ZeroDivisionError: #ERRO: Dividir valor por zero.
    print('Não é possível dividir um número por zero! ')
except KeyboardInterrupt: #ERRO: Quando o usuário interrompe o programa...
    print('O usuário preferiu não informar os dados!')
except Exception as erro: #Generaliza e pega todos os erros.
    print(f'Problema encontrado {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')