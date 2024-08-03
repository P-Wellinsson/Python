d = int(input('\033[35mQuantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
p = (d * 60) + (km * 0.15)
print(f'\033[32mO total a pagar é de R${p:.2f}\033[m')
