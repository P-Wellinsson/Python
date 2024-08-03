jogador = dict()
partidas = []
time = []
while True:
    jogador['nome'] = input('Nome do jogador: ').strip().capitalize()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for i in range(tot):
        partidas.append(int(input(f'Gols na {i+1} partida: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').strip()[0]
        if resp in ('SsNn'):
            break
        print('Erro! Digite apenas S ou N.')
    if resp in ('Nn'):
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
# c == contador, v == cada um da lista time separadamente.
for c, v in enumerate(time):
    print(f'{c:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-=' * 30)
    dados = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    if dados >= len(time) or dados < 0:
        print(f'ERRO! Não existe jogador com código {dados}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[dados]["nome"]}:')
        for i, g in enumerate(time[dados]['gols']):
            print(f'     No jogo {i+1} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
