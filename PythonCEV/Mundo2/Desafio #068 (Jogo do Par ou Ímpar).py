from random import randint
v = 0
while True:
    comp = randint(0, 10)
    n = int(input(f'Digite um valor: ({comp})'))# arrumar depois
    pijog = ' '
    while not pijog in('PI'):
        pijog = input('Par ou Impar? [P/I] ').strip().upper()[0] # Par ou Impar do jogador.
    nf = n + comp # Número Final
    pif = 'PAR' if nf % 2 == 0 else 'ÍMPAR' # Par ou impar total.
    print(f'\nVocê jogou {n} e o computador jogou {comp}, Total: {nf} e foi {pif}')
    
    if nf % 2 == 0 and pijog == 'P' or nf % 2 == 1 and pijog == 'I':
        print('Você venceu \nVamos jogar de novo.')
        v += 1
        print('-=' * 30)
    else:
        break
print('-=' * 20)
print(f'Você PERDEU!! \nVocê venceu {v} vez(es)')
print('-=' * 20)
