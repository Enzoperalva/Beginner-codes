count=num=0
while True:
    while num>=0:
        for c in range(0, 11):
            num= int(input('Você quer ver a tabuada de qual valor:'))
            print('=='*20)
            print(f'{num} x {count} = {num*count}')
            count+=1
            print('==' * 20)
    if num<0:
        break
print('Falha, o número não pode ser menor que zero!')