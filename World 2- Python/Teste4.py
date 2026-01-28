s=n=0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
    s+=n
print(f'Soma dos numeros {s}')