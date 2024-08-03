def LeiaDinheiro(msg):
    while True:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mErro: "{entrada}" é um preço inválido\033[m')
        else:
            return float(entrada)


def LeiaInt(num):
    print('-' * 30)
    ok = False
    valor = 0
    while ok == False:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número válido.\033[m')
    return valor
