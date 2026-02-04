import random
sorteio= (random.randint(1,10), random.randint(1,10),
          random.randint(1,10), random.randint(1,10),
          random.randint(1,10))
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior numero é: {max(sorteio)}') #O max serve para eu ver o valor maximo dentro da tupla
print(f'O menor numero é: {min(sorteio)}') #O min é o contrário do amx