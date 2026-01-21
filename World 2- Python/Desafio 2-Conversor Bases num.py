import time

num= int(input('Digite algum número inteiro:'))

print('[ 1 ] para \033[32mBINÁRIO!\033[m')
print('[ 2 ] para \033[32mOCTAL\033[m!')
print('[ 3 ] para \033[32mHEXADECIMAL\033[m!')

#VARIÁVEIS:

opcao= int(input('Qual sua opção:'))

#INTERAÇÃO:

print('\033[36mCALCULANDO...\033[m')
time.sleep(1.5)

if opcao == 1:
    print(f'RESULTADO: {bin(num)[2:]}')
elif opcao == 2:
    print(f'RESULTADO: {oct(num)[2:]}')
elif opcao == 3:
    print(f'RESULTADO: {hex(num)[2:]}')
elif opcao != 1 and 2 and 3:
    print('AS OPÇÕES SÃO 1, 2 OU 3')
    print('\033[31mESCOLHA DE NOVO!!!\033[m')

