num= int(input('Número:'))
for num in range(1, num+1):
    for i in range(1, num+1):
        print(i, end='')
    for i in range(num-1, 0, -1):
        print(i, end='')
    print()