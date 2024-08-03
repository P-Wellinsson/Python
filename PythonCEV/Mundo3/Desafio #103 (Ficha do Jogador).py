def ficha(n, g):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


print('-' * 40)
name = input('Nome do Jogador: ').capitalize()
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    name = '<desconhecido>'
ficha(name, gols)
