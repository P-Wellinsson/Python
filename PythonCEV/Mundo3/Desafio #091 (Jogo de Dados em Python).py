from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
        'jogador3': randint(1, 6), 'jogador4': randint(1, 6), }
ordem = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'   O {k} tirou {v} no dado.')
    sleep(1)
ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"-=" * 30} \nRanking dos jogadores:')
for c in range(4):
    print(f'   {c+1}ºlugar: {ordem[c][0]} com {ordem[c][1]} pontos')
    sleep(1)
