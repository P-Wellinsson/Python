n = int(input('Digite um número para mostrar o fatorial: '))
np = n
fac = 1
if n >= 0:
    print(f'{n}! = ',end = '')
    while np > 0:
        print(np, end ='')
        print(' X ' if np > 1 else ' = ', end = '')
        fac *= np
        np -= 1
    print(f'{fac}', end = '')
else:
    print('Não existe fatorial negativo!! ')
