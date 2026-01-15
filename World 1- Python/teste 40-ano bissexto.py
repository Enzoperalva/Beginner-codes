from datetime import date
ano= int(input('Me fale algum ano e vamos ver se ele é bissexto, se quiser do ano atual, digite 0:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #Se ano for divisivel por 4 e tambem por 100, não pode ser diferente de 0 ou então o ano ser divisivel por 400!
    print(f'O ano de {ano} é bissexto!')            #Isso ai em cima é a tradução!
else:
    print(f'O ano de {ano} não é bissexto!')