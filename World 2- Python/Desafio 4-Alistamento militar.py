from datetime import date
from readline import set_completer

sexo= str(input('Qual seu sexo?')).lower()
if sexo == 'masculino':
    nasceu= int(input('Qual ano você nasceu:'))
    ano= date.today().year
    idade= ano - nasceu


    if idade == 18:
        print('Faz 18 esse ano HAHAHAHAHAH')
        print('Hora de se alistar!')
    elif idade < 18:
        print(f'Você tem {idade} anos')
        print(f'Faltam {18 - idade} anos para você se alistar!')
        print(f'Seu alistamento está marcado para o ano de {ano- (idade-18)}!')
    else:
        print(f'Você tem {idade} anos')
        print(f'Já passou {idade - 18} anos, e você ainda não se alistou!')
        print(f'Seu alistamento estava marcado para o ano de {ano- (idade-18)}')
else:
    print('Você não precisa se alistar!')
    print('O alistamento militar só é obrigatório para os homens!')