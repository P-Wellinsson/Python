# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moedaP

p = float(input('\033[34mDigite o preço: R$\033[32m'))
print(
    f'\033[33mA metade de {moedaP.moeda(p, formatado=True)} é {moedaP.metade(p, True)}')
print(
    f'A dobro de {moedaP.moeda(p, formatado=True)} é {moedaP.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedaP.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedaP.diminuir(p, 13, True)}\033[m')
