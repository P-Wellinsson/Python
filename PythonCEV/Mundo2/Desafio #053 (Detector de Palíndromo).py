fras = input('Digite uma frase: ').replace(' ', '').upper().strip()
fras2 = ''.join(reversed(fras))
print(f'O inverso de {fras} é {fras2}')

if fras == fras2:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
