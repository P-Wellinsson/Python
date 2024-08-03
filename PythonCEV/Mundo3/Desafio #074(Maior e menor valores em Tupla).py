from random import randint

num = randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10),
print(f'Os números foram: {num} \nO maior número é {max(num)} e o menor {min(num)}')
print('\nOs valores sorteados foram: ', end='')
for n in num:
    print(n, end=' ')
