import moedaG

p = float(input('\033[34mDigite o preço: R$\033[32m'))
print('\033[35m', end='')
moedaG.resumo(p, 20, 12, True)
print('\033[m')
