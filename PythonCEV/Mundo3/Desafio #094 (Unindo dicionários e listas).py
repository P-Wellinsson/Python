galera = []
pessoas = dict()
média = 0
while True:
    pessoas['nome'] = input('Nome: ').strip().capitalize()
    pessoas['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
    while pessoas['sexo'] not in 'MF':
        pessoas['sexo'] = input(
            'Sexo Inválido, Digite novamente. \nSexo [M/F]: ').strip().upper()[0]
    pessoas['idade'] = int(input('Idade: '))
    while not 160 > pessoas['idade'] >= 0:
        pessoas['idade'] = int(
            input('Idade Inválida, Digite novamente. \nIdade: '))
    média += pessoas['idade']
    galera.append(pessoas.copy())
    resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while resp not in ('SN'):
        resp = input(
            'Erro! Responda apenas S ou N. \nQuer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print(f'{"-=" * 30} \nA) Foram cadastradas {len(galera)} pessoas.')
média /= len(galera)
print(f'B) A média de idade das pessoas é de {média:5.2f} anos.')
print(f'C) As mulheres cadatradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print(f'\nD) Lista das pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<< ENCERRADO >>')
