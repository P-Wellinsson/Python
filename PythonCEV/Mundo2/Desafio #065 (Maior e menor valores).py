resp = 'S'
mai = men = s = c = 0
while resp == 'S':
    n = int(input('Digite um número: '))
    resp = input('Você quer continuar a digitar valores? [S/N]').upper().strip()
    s += n
    c += 1
    mai = mai if mai > n else n
    men = men if men < n and men != 0 else n
print(f'Você digitou {c} números, a média dos números é {s/c} \nSendo {mai} o maior valor e {men} o menor')
