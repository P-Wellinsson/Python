num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    while True:
        resp = input('Quer continuar? [S/N]').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
num.sort()
print(f'Você digitou {num}')
