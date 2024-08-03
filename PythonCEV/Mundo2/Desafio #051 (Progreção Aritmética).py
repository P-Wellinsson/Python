termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
d10 = termo + (10 - 1) * razao
for i in range(termo, d10 + razao, razao):
    print(i, end=' > ')
print('TERMINOU')
