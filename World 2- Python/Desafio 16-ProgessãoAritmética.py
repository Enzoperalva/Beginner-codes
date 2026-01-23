import time
num= int(input('Digíte um termo:'))
razao= int(input('Digíte a razão:'))

print(f'{num}')
for c in range(0, 10):
    num=num+razao
    print(f'{num}')
    time.sleep(1)
print(' ⬇ ')
print('FIM')