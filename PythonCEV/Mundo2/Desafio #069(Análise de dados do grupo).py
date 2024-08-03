maior = man = tot = 0
while True:
    while True:
        age = int(input('Idade: '))
        if age > 0 and age < 180:
            break
    sex = ' '
    while sex not in ('MF'):
        sex = input('Sexo: [M/F]').strip().upper()[0]

    if age > 18:
        maior += 1
    if sex == 'M':
        man += 1
    if age < 20 and sex == 'F':
        tot += 1
    cont = ' '
    while cont not in ('SN'):
        cont = input('Quer continuar? [S/N]').strip().upper()[0]
    if cont == 'N':
        break
print(f'Tiveram {maior} pessoas com mais de 18 anos.' if maior != 1 else f'Teve {maior} pessoa com mais de 18 anos.')
print(f'{man} homens foram cadastrados.' if man != 1 else f'{man} homem foi cadastrado.')
print(f'E tiveram {tot} mulheres com menos de 20 anos.' if tot != 1 else f'E teve {tot} mulher com menos de 20 anos.')
