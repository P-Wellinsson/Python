tot = m1000 = cheap = c = 0
prbar = ' '#Produto mais barato   #Erro
while True:
    name = input('Produto: ').strip().capitalize()
    prec = float(input('Preço: R$'))
    tot += prec if prec > 0 else tot + 0
    c += 1
    if prec > 1000:
        m1000 += 1
    if cheap > prec or c == 1:
        cheap = prec
        prbar = name
    cont = ' '
    while cont not in('SN'):
        print('=-' * 16)
        cont = input('Quer continuar? [S/N]').strip().upper()[0]
        print('=-' * 16)
    if cont == 'N':
        break
print(f'O total gasto na compra é R${tot:.2f} \n{m1000} Produto(s) custa(m) mais de R$1000')
print(f'O produto mais barato é {prbar} custando R${cheap:.2f}')
