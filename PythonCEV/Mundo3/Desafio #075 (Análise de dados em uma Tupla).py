s = 's', 'es', ''  # Teste
num = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input(
    'Digite um número: ')), int(input('Digite um número: '))
print(f'\nVocê digitou os números {num}')
print(
    f'O número 9 aparece {num.count(9)} vez{s[2] if num.count(9) == 1 else s[1]}')

if 3 in num:
    print(f'O 3 foi digitado primeiro na posição {num.index(3)+1}')
else:
    print(f'O 3 não foi digitado.')

print(f'Os números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
