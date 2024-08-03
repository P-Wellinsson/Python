from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.5)
    if i < f:
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i += p
    else:
        while i >= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i -= p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem! ')
início = int(input('Início: '))
fim = int(input('fim:    '))
passo = int(input('passo:  '))
contador(início, fim, passo)
