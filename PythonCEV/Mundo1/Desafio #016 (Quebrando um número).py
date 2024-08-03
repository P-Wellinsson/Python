from math import trunc
n = float(input('\033[32mDigite um número: \033[33m'))
print(
    f'\033[m\033[7;37;1mO valor digitado foi {n} e a sua porção inteira é {trunc(n)}.\033[m')
