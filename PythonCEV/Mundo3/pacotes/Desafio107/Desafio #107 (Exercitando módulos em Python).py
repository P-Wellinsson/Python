import moeda

preço = float(input('\033[34mDigite o preço: R$'))
print(f'\033[33;4mA metade de R${preço} é {moeda.metade(preço)}')
print(f'O dobro de R${preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10% temos {moeda.aumentar(preço, 10)}')
print(f'Diminuindo 10% temos {moeda.diminuir(preço, 10)}\033[m')
