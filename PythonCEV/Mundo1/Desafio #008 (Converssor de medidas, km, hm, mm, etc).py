m = float(input('\033[7;1;40mDigite uma distância em metros:\033[m '))
print(f'\033[35mA medida de {m}m corresponde a:\033[m')
print(f'\033[34m{m / 1000} km')
print(m / 100,'hm')
print(m /10,'dam')
print(f'{m*10:.0f}dm')
print(f'{m*100:.0f}cm')
print(f'{m*1000:.0f}mm\033[m')