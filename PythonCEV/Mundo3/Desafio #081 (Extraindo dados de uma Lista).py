num = []
while True:
    num.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Quer continuar? [S/N]').strip().upper()
        if resp in ('SN'):
            break
    if resp == 'N':
        break
print('=-' * 20)
print(f'Foram digitados {len(num)} valores.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {num}')
print(f'O valor 5 está na lista.' if 5 in num else f'O valor 5 não está na lista.')
