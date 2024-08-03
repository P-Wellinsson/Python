prods = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Caneta', 1.50, 'Lápisera', 3.35, 'Estojo', 42.00, 'Mochila', 148.69, 'Pasta', 9.99, 'Tesoura', 5.50
print('-' * 40)
print(f'{"Lista dos Preços":=^40}')
print('-' * 40)
for i in range(0, len(prods)):
    if str(prods[i]) == prods[i]:  # if i % 2 == 0:
        print(f'|{prods[i]:.<30}', end='')  # Produtos
    else:
        print(f'R$ {prods[i]:>6.2f}|')  # Preços
print('-' * 40)
