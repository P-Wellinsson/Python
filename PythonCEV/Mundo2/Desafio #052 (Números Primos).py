som = 0
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
        som += 1
if som == 2:
    print('Primo')
else:
    print('Não é Primo')
