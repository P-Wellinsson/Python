from utilidadesCeV import moeda

p = float(input('\033[34mDigite o preço: R$\033[32m'))
print('\033[35m', end='')
moeda.resumo(p, 35, 22, True)
print('\033[m')