while True:
    n = int(input('Quer ver qual tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c} = {n * c}')
print('Programa encerrado. \nVolte sempre!')
