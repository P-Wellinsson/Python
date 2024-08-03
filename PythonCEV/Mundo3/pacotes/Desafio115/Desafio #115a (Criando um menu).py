# Vamos criar um menu em Python, usando modularização.
from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('OPÇÃO 1'.center(42))
    elif resposta == 2:
        cabeçalho('OPÇÃO 2'.center(42))
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(1.25)
