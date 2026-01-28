from random import choices
num= 1,2,3,4,5,6,7,8,9,0
letrasmai= 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
letrasmin= 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
simbolos= '!','@','#','$','%','&'
tamanho= float(input('Qual o tamanho da senha que você quer:'))
porcentagem= tamanho*0.25
aleatorio= aleatorio2=aleatorio3=aleatorio4=0
if tamanho >=8:
    for numeros in range(0, 1):
        aleatorio = choices(num, k=porcentagem)
    for maiusculas in range(0, 1):
        aleatorio2= choices(letrasmai, k=porcentagem)
    for minuscula in range (0, 1):
        aleatorio3= choices(letrasmin, k= porcentagem)
    for simb in range (0, 1):
        aleatorio4= choices(simbolos, k= porcentagem)
    print(f'Sua senha é: {aleatorio}{aleatorio2}{aleatorio3}{aleatorio4}')
else:
    print('\033[31mSUA SENHA TEM QUE TER 8 DIGITOS OU MAIS!\033[m')