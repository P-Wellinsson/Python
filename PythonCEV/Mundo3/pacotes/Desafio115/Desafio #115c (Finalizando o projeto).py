# Vamos finalizar o projeto de acesso a arquivos em Python.
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvídeo.txt'

if not arqveExist(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova pessoa',
                    'Sair do Sistema'])
    if resposta == 1:
        LerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO'.center(42))
        nome = input('Nome: ').title()
        age = LeiaInt('Idade: ')
        cadastrar(arq, nome, age)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1.25)
