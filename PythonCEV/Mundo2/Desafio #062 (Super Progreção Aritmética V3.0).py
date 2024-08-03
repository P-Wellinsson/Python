first = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while c <= tot:
        print(first, end = ' ->> ')
        c += 1
        first += r
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progreção finalizada com {tot} termos mostrados.')
