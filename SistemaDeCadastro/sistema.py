from SistemaDeCadastro.lib.interface import *
from SistemaDeCadastro.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opçoão de listar o conteúdo de um arquivo.
        lerArquivo(arq)
        sleep(1)
    elif resposta ==  2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome= str(input('Nome: '))
        idade= leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(1)