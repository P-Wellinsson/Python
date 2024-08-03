from random import randint
from time import sleep

lista = []
jogos = []
print('-' * 39)
print(f'{"JOGA NA MEGA SENA":^39}')
print('-' * 39)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'-=-=-=-={f"SORTEANDO {quant} JOGOS":^20}-=-=-=-=-=')
for i in range(len(jogos)):
    print(f'Jogo {i+1}: {jogos[i]}')
    sleep(2)
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
