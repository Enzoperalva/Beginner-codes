print('Vamos verificar se sua cidade começa ou não com o nom SANTO')
city= str(input('Para isso, digite aqui o nome dela:')).upper().strip()
print(city[:5] == 'SANTO')