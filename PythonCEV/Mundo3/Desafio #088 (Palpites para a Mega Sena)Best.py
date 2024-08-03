from random import randint
from time import sleep
num = []
print(f'''{"-" * 39}
{"JOGA NA MEGA SENA":^39}
{"-" * 39}''')
jogo = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' * 4, f'SORTEANDO {jogo} JOGOS', '-=' * 4)
for i in range(jogo):
    num.append([])
    for c in range(0, 6):
        while True:  # Valor Duplicado
            n = randint(1, 60)
            if n not in num[i]:
                break
        num[i].append(n)
    num[i].sort()
    sleep(1)
    print(f'Jogo {i+1}: {num[i]}')
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
