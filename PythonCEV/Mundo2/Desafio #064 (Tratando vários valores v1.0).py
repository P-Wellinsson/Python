n = int(input('Digite números inteiros, para parar digite o número "999" \nDigite o número: '))
c = 0
s = n - 999
while n != 999:
    n = int(input('Digite um número: '))
    s += n
    c += 1
print(f'\nPrograma finalizado!!! \nForam digitados {c} número(s), com a soma desses números sendo {s}')
