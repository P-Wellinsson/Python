# Vamos ver como fazer acesso a arquivos usando o Python.
'''
'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo
'r+' -> Usado para ler e escrever algo
'a' -> Usado para acrescentar algo
'''
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
        cabeçalho('OPÇÃO 2'.center(42))
        pessoa = input('Nome: ').title()
        age = LeiaInt('Idade: ')
        with open(arq, 'a') as arquive:
            arquive.write(f'{pessoa};{age} \n')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1.25)
