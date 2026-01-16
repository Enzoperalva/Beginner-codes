import time
print('Vamos cadastrar sua conta:')

#VARIAVEIS:

name= str(input('\033[7;37mNome de usuário:\033[m')).lower()
senha= str(input('\033[7;37mSenha:\033[m'))
quantidade= len(senha) >= 8
maiuscula= name.capitalize()
num= senha[-1].isdigit()
teste_tamanho= quantidade > 8

#INTERAÇÃO:
print('\033[33mANALISANDO...\033[m')
time.sleep(2)

#CONDIÇÕES:
if name in senha:

 print('\033[35mSUA SENHA NÃO É ADEQUADA, VEJA O MOTIVO:\033[m')
time.sleep(2)

print('\033[31mSua senha não pode conter seu nome!\033[m')
if quantidade < 8:
    print('\033[31mSua senha precisa ter 8 ou mais dígitos!\033[m')
if name != maiuscula:
    print('\033[31mPrecisa começar com letra maiúscula!\033[m')
if not num:
    print('\033[31mPrecisa terminar com algum número!\033[m')
else:
    print('\033[32mSua senha está adequada!\033[m')