fra= str(input('Digite alguma frase:')).lower().strip()
print(f'A letra a aparece: {fra.count('a')}')
print(f'Ela aparece a primeira vez na posição: {fra.find('a')+1}')
print(f'E aparece a ultima vez na posição: {fra.rfind('a')+1}')