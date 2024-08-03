words = 'Telescopio', 'Fluxograma', 'Batata', 'Frita', 'Cenoura', 'Abacate', 'Marrom', 'Legumes', 'Vermelhos', 'Preto',
'Imagem', 'Molho', 'Laranja', 'Morte', 'Vida', 'Dor', 'Luar', 'Sangue', 'Vermelho', 'Sangrento', 'Paz', 'Armonia'
for p in words:
    print(f'\nNa palavra {p.upper()} Temos', end=' ')
    for lyrics in p:
        if lyrics.upper() in ('AEIOU'):
            print(lyrics.lower(), end=' ')
