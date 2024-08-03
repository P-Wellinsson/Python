# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = []

jogador['nome'] = input('Nome do jogador: ')
tot = int(input(f'Quantidade de partidas de {jogador["nome"]}: '))
for i in range(tot):
    partidas.append(int(input(f'gols feitos na {i+1}º partida: ')))
jogador['gols'] = partidas[:]
print(jogador['gols'])
jogador['total'] = sum(partidas)
print(f'{"-=" * 30} \n{jogador} \n{"-=" * 30}')

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(f'{"-=" * 30} \nO jogador {jogador["nome"]} jogou {tot} partidas.')
for i in range(tot):
    print(f'    => Na partida {i+1}, fez {partidas[i]} gols')
print(f'Foi um total de {jogador["total"]} gols')
