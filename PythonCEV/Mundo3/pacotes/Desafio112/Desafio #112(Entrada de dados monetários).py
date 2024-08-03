from utilidadesCeV import moeda
from utilidadesCeV import dado

while True:
    p = dado.LeiaDinheiro('\033[34mDigite o preço: R$\033[32m')
    print('\033[35m', end='')
    moeda.resumo(p, 35, 22, True)
    print('\033[m')
