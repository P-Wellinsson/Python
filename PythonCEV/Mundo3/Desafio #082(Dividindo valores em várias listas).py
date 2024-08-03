lista = []
par = []
inpar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        inpar.append(num)  # Par
    else:
        par.append(num)  # Ínpar
    resp = input('Quer continuar? [S/N]').strip()
    if resp in 'nN':
        break
print('-=' * 30)
print(f'''A lista completa é {lista}
A lista dos pares é {inpar}
A lista dos ínpares é {par}''')
