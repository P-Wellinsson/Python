from random import randint
from time import sleep

numcomp = randint(0, 5)
print('\033[32m-=-' * 14)
num = int(input(f'\033[35mTente adivinhar um número entre 0 e 5: \033[32m'))
print('-=-' * 14)
sleep(2)
if num == numcomp:
    print('\033[36mVocê venceu, PARABÉNS!!',end='')
else:
    print(
        f'\033[31mVocê Perdeu!! \nO número certo é {numcomp} \nTente de novo!', end='')
print('\033[m')
