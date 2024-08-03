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


n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
