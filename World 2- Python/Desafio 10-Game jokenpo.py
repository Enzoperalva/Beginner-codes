import random, time

#VARIÁVEIS:
lista= ('pedra', 'papel', 'tesoura')
bot= (random.choice(lista)).lower()

#INTERAÇÃO:
print('-='*12)
print('VAMOS BRINCAR DE JOKENPO!')
print('-='*12)
time.sleep(1)

print('Eu ja escolhi o meu, agora é sua vez!')
time.sleep(1)
print('PEDRA')
print('PAPEL')
print('TESOURA')
time.sleep(0.7)

#VARIÁVEIS:
opcao= str(input('Opção:')).lower()
print('JO')
time.sleep(0.4)
print('KEN')
time.sleep(0.4)
print('PO')
time.sleep(0.5)

print('--='*10)
#CONDIÇÕES DE DEORRTA E EMPATE:
        #PEDRA:
if opcao == 'pedra' and 'papel' and 'tesoura':

    if bot == 'pedra' and opcao== 'tesoura':
        print(f'\033[31mPERDEDOR!!!!\033[m')
        print(f'Eu escolhi {bot}')

    elif bot == 'pedra' and opcao== 'pedra':
        print('\033[36mEMPATAMOS\033[m')
        print('Ambos de nós escolhemos pedra')

    elif bot == 'pedra' and opcao== 'papel':
        print(f'\033[32mGANHADOR\033[m')
        print(f'Eu escolhi {bot}')

        #PAPEL:
    elif bot== 'papel' and opcao== 'tesoura':
        print(f'\033[32mGANHADOR\033[m')
        print(f'Eu escolhi {bot}')

    elif bot== 'papel' and opcao== 'pedra':
        print(f'\033[31mPERDEDOR!!!!\033[m')
        print(f'Eu escolhi {bot}')

    elif bot== 'papel' and opcao== 'papel':
        print('\033[36mEMPATAMOS\033[m')
        print('Ambos de nós escolhemos papel')

        #TESOURA:
    elif bot== 'tesoura' and opcao== 'tesoura':
        print('\033[36mEMPATAMOS\033[m')
        print('Ambos de nós escolhemos tesoura')

    elif bot== 'tesoura' and opcao== 'papel':
        print(f'\033[31mPERDEDOR!!!!\033[m')
        print(f'Eu escolhi {bot}')

    elif bot== 'tesoura' and opcao== 'pedra':
        print(f'\033[32mGANHADOR\033[m')
        print(f'Eu escolhi {bot}')
else:
    print('\033[31mJOGADA INVALIDA\033[m')
    print('Escolha pedra, papel ou tesoura!')

print('--='*10)