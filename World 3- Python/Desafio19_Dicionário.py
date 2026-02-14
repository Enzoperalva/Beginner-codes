media= {'nome': str(input('Nome:')), 'media': float(input('Média:'))}
if media['media'] < 6:
    media['situacao'] = 'Reprovado'
elif 6>= media['media'] <7:
    media['situacao'] ='Recuperação'
else:
    media['situacao']= 'Aprovado'
print('-='*20)
for k,v in media.items():
    print(f'{k}: {v}')