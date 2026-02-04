times=  ('Botafogo','Chapecoense','EC Vitoria','Fluminense',
        'Mirasol','Bahia','São paulo','Atletico-PR',
        'Bragantino','Palmeiras','Atlético-MG','Flamengo',
        'Grêmio','Corinthians','Vasco da Gama','Coritiba',
        'Internacional','Santos','Remo','Cruzeiro')
print('-='*70)
print(f'Lsta de time brasileirão:{times}')
print('-='*70)
print(f'Os 5 primeiro são: {times[:5]}')
print('-='*70)
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*70)
print(f'Time em ordem alfabética: {sorted(times)}')
print('-='*70)
posicao= times.index('Chapecoense', 1)
print(f'Chapecoense está na {posicao+1}° posição')