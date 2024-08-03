# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import moeda

p = float(input('\033[34mDigite o preço: R$\033[32m'))
print(f'\033[33mA metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'A dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}\033[m')
