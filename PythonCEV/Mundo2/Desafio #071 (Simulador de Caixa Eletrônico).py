v1 = v10 = v20 = v50 = 0
print('Bem vindo ao caixa eletrônico!\n')
saq = int(input('Valor a ser sacado: R$'))
while saq >= 50:
    v50 += 1
    saq -= 50
    print(saq, end=' ')
while saq >= 20:
    v20 += 1
    saq -= 20
    print(saq, end='*')
while saq >= 10:
    v10 += 1
    saq -= 10
    print(saq, end='-')
while saq >= 1:
    v1 += 1
    saq -= 1
    print(saq, end='|')

print(f'\n{v50} notas de R$50' if v50 != 1 else f'\n{v50} nota de R$50')
print(f'{v20} notas de R$20' if v20 != 1 else f'{v20} nota de R$20')
print(f'{v10} notas de R$10' if v10 != 1 else f'{v10} nota de R$10')
print(f'{v1} notas de R$1' if v1 != 1 else f'{v1} notas de R$1')
print('\nVolte sempre! Tenha um bom dia!')
