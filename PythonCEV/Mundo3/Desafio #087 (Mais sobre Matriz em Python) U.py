matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = scol = mai = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:  # Par
            par += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:  # Soma das colunas
            scol += matriz[l][2]
        if matriz[l][c] == matriz[1][c]:  # Maior número da segunda linha
            if c == 0 or matriz[l][c] > mai:
                mai = matriz[l][c]
print('-=' * 30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-' * 30)
print(f'''A soma dos pares é {par}
A soma dos valores da terceira colona é {scol}
O maior valor da segunda linha é {mai}''')
