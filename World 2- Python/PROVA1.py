import time
num= int(input('Digíte um número:'))
if num>0 and num % 2 == 0 and num % 5 != 0:
    print('\033[36mCLASSE A!\033[m')
    time.sleep(1)
    print('Nela o número é positivo, par, e NÃO é múltiplo por 5.')
elif num < 0 or num > 1000:
    print('\033[36mCLASSE B!\033[m')
    time.sleep(1)
    print('Nela o número é negativo ou maior que 1000.')
elif num==0:
    print('\033[36mCLASSE C!\033[m')
    time.sleep(1)
    print('Nela o número é igual a 0.')
else:
    print('\033[36mCLASSE D!\033[m')
    time.sleep(1)
    print('Não se encaixa com as outras classes.')