km = float(input('\033[37mQual a distância da sua viagem? digite em Km: '))
if 200 >= km > 0:
    print(f'\033[35mO preço da passagem é de R${km * 0.5:.2f}')
elif km > 200:
    print(f'\033[35mO preço da passgem é de R${km * 0.45:.2f}')
else:
    print('\033[7;1;31mValor inválido')
print('\033[m')
