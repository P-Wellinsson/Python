l = float(input('\033[37mLargura da parede: '))
a = float(input('Altura da parede: '))
print(f'\033[33mSua parede tem a dimensão de {l}X{a} e sua área é de {l*a}m².')
print(f'Para pintar essa parede, você precisará de {l*a/2}l de tinta.\033[m')
