from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano que você nasceu: '))
idade = atual - nasc
if idade >= 0 and idade <= 9:
    print(f'Voce tem {idade} anos, portanto está na Categoria MIRIM')
elif idade <= 14:
    print(f'Voce tem {idade} anos, portanto está na Categoria INFANTIL')
elif idade <= 19:
    print(f'Voce tem {idade} anos, portanto está na Categoria JÚNIOR')
elif idade <= 25:
    print(f'Voce tem {idade} anos, portanto está na Categoria SÊNIOR')
elif idade <= 175:
    print(f'Voce tem {idade} anos, portanto está na Categoria MASTER')
else:
    print('Idade Inválida')
