while True:
    cont= 0
    num = int(input('Você quer ver a tabuada de qual valor:'))
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} x {cont} = {num*cont}')
        cont+=1
print('\033[31mFalha, o número não pode ser negativo!\033[m')