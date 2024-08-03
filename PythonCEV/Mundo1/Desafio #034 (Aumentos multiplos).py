sal = float(input('\033[35mQual é o seu sálario? R$\033[32m'))
if sal > 1250:
    print(
        f'O valor do aumento é de R${sal * (10/100):.2f} e o sálario depois do aumento é de R${sal + sal * (10/100):.2f}')
elif sal > 0:
    print(
        f'O valor do aumento é de R${sal * (15/100):.2f} e o sálario depois do aumento é de R${sal + sal * (15/100):.2f}')
else:
    print('\033[7;1;31mValor inválido!!')
print('\033[m')
