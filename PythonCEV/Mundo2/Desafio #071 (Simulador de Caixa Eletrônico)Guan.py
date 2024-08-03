print('Bem vindo ao caixa eletrônico!\n')
saq = int(input('Valor a ser sacado: R$'))
nota = 50
totnota = 0
while True:
    if saq >= nota:
        saq -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'{totnota} notas de R${nota}' if totnota != 1 else f'{totnota} nota de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totnota = 0
        if saq == 0:
            break
print('\nVolte sempre! Tenha um bom dia!')
