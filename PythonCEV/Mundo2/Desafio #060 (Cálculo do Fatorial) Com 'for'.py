n = int(input('Digite um número para ser o fatorial: '))
nCon = n
fac = 1
print(f'{n}! = ', end='')

for i in range(1, n + 1):
    print(f'{nCon}', end='')
    print(f' X ' if nCon > 1 else ' = ', end='')
    fac *= nCon
    nCon -= 1
print(fac, end='')
