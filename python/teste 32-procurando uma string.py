print('Vamos ver se você tem "Silva" no nome')
name= str(input('Digite seu nome:')).upper().strip()
tem= 'SILVA' in name
print(f'{tem}')