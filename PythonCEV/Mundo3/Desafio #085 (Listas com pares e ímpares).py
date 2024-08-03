num = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        num[0].append(n)  # Par
    else:
        num[1].append(n)  # Ímpar
num[0].sort()
num[1].sort()
print('-=' * 30)
print(f'Os números pares são {num[0]}')
print(f'Os números ímpares são {num[1]}')
