num = int(input('\033[33mInforme um número: \033[37m'))
print(f'Analisando o número {num}')
print(f'\033[31mUnidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}\033[m')
