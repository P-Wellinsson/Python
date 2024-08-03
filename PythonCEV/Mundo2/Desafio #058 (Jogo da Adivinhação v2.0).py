# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

tentat = 1
nComp = randint(0, 10)

n = int(input('Escolha um número de 0 á 10 para ver se é o mesmo do computador \nDigite o número: '))
while nComp != n:
    if nComp > n:
        n = int(input('\nMais... Tente de novo: '))
    elif nComp < n:
        n = int(input('\nMenos... Tente de novo: '))
    tentat += 1
print(f'\nForam necessários {tentat} tentativas para vencer!')
