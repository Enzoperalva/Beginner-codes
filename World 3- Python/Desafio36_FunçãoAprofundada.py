def leiaInt(msg):
    while True:
        try:
           inteiro= int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUsuário preferiu não digitar esse número!\033[m')
            return 0
        else:
            return inteiro


def leiaFloat(msg):
    while True:
        try:
            real=  float(input(msg))
        except ValueError:
            print('\033[31mERRO: Por favor, digíte um número real válido!\033[m')
            continue
        else:
            return real


num1= leiaInt('Digite um Inteiro: ')
num2= leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {num1} e o real foi {num2}')