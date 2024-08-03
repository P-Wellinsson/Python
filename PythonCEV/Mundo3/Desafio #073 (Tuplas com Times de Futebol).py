times = 'Ceará', 'Palmeiras', 'Atletico-PR', 'Flamengo', 'São Paulo', 'Chapecoense', 'Bahia', 'Atlético-MG', 'Santos', 'Goiás', 'Corinthians', 'Avaí', 'Grêmio', 'Fluminense', 'Cruzeiro', 'Internacional', 'Botafogo', 'Vasco', 'Fortaleza', 'CSA'

print('-----' * 20)
print(f'''Lista dos times {times}
\nOs cinco primeiros são {times[:5]}
\nOs 4 últimos são {times[-4:]}
\nTimes em ordem alfabética: {sorted(times)}
\nO {times[5]} está em {times.index('chapecoense'.capitalize())+1}º posição.''')
print('-----' * 20)
