# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
num = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > num[-1]:
        num.append(n)
        print('Adicionando no final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                print(f'Adicionando a posição {pos} da lista...')
                num.insert(pos, n)
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem são {num}')
