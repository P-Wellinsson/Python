dados = []
temp = []
mai = men = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('peso: ')))
    mai = temp[1] if len(dados) == 0 or mai < temp[1] else mai
    men = temp[1] if len(dados) == 0 or men > temp[1] else men
    dados.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N]').strip().upper()
    if resp == 'N':
        break
print('-=' * 30)

print(f'Foram cadastradas {len(dados)} pessoas')
print(f'O maior peso foi de {mai:.1f}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == mai:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {men:.1f}Kg. Peso de', end=' ')
for p in dados:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')
