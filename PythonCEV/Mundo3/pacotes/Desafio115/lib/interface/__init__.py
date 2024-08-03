def linha(tam=42):
    print('-' * tam)


def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(
                f'\033[31mERRO: Por favor digite um número inteiro válido.\033[m')
            continue  # Volta pro while
        except KeyboardInterrupt:
            print(f'\033[31mDigite um valor.\033[m')
        else:
            return n


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for i in range(len(lista)):
        print(f'\033[33m{i+1} - \033[34m{lista[i]}\033[m')
    linha()
    opc = LeiaInt('\033[32mSua Opção: \033[m')
    return opc
