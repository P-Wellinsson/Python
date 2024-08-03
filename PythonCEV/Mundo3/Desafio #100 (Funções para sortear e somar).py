from random import randint
from time import sleep


def sorteia(n):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        n.append(randint(1, 10))
        print(n[i], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    s = 0
    for n in lista:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {lista}, temos {s}')


nunbers = []
sorteia(nunbers)
somapar(nunbers)
