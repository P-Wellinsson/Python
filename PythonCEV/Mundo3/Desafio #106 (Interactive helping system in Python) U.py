from time import sleep
c = '\033[m', '\033[0;30;41m', '\033[0;42;30m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m'
# Sem cores 0   Vermelho 1   Verde 2   Amarelo 3   Azul 4   Roxo 5     Branco 6


def linha(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))
    print(c[0], end='')
    sleep(1)


def ajuda(cod):
    linha(f'Acessando o manual do comando \'{cod}\'', 4)
    print(c[6], end='')
    help(cod)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    linha('SISTEMA DE AJUDA PyHELP', 2)
    comando = input("Função ou Biblioteca: > ")
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
linha('ATÉ LOGO!', 1)
