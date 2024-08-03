som = 0
cont = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        som += i
        cont += 1
print(f'A soma dos valores é de {som} e foram {cont} valores')
