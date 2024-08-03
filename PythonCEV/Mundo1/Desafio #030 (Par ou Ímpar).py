n = int(input('\033[33mDigite um número: '))
if n % 2 == 0:
    print(f'\033[34;7mO número {n} é par!!\033[m')
else:
    print(f'\033[36;7mO número {n} é ímpar\033[m')
