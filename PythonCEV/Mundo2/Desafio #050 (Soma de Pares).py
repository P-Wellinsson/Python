num = 0
cont = 0
for i in range(6):
    n = int(input('Digite um número inteiro: '))
    if n%2 == 0:#O número é par
        num += n
        cont += 1
print(f'A soma do(s) {cont} número(s) par(es) é igual á {num}')
