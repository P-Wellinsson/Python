s = float(input('\033[37mQual é o salário do Funcionário? R$'))
print(
    f'\033[31mUm funcionário que ganhava R${s:.2f}, com 15% de aumento, passa a receber R${s+s*(15/100):.2f}\033[m')
