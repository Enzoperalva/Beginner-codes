import time
print('Vamos cadastrar sua conta!')

#VARIAVEIS E ENTRADAS:

name= str(input('\033[7;37mNome de usuário:\033[m')).strip().lower()
senha= str(input('\033[7;37mSenha:\033[m')).strip()


quantidade= len(senha) >= 8
regra_name= name not in senha.lower()
regra_maiuscula= senha[0].isupper()
regra_numero= senha[-1].isdigit()

#INTERAÇÃO:
print('\033[33mANALISANDO...\033[m')
time.sleep(2)

#CONDIÇÕES/ PORTÃO DA SEGURANÇA:
if quantidade and regra_name and regra_maiuscula and regra_numero:
 print('\033[32mSUA SENHA É ADEQUADA, PARÁBENS!\033[m')
else:
    print('\033[35mSUA SENHA NÃO É ADEQUADA, VEJA OS MOTIVOS:\033[m')
    time.sleep(2)
    if not quantidade:
        print('\033[31mSUA SENHA PRECISA TER 8 DÍGITOS!\033[m')
    if not regra_maiuscula:
        print('\033[31mSUA SENHA PRECISA COMEÇAR COM LETRA MAIÚSCULA!')
    if not regra_name:
        print('\033[31mSUA SENHA NÃO PODE TER SEU NOME!')
    if not regra_numero:
        print('\033[31mSUA SENHA PRECISA TERMINAR COM ALGUM NÚMERO!\033[m')