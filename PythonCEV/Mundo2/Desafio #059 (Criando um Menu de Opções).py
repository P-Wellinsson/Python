from time import sleep
opçao = 0

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while opçao != 5:
    print('=-' * 15)
    sleep(1.25)
    opçao = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
  '''))
    print('=-' * 15)
    if opçao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opçao == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
    elif opçao == 3:
        print(f'O maior número é {n1 if n1 > n2 else n2}')
    elif opçao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('Finalizando...')
    else:
        print(f'Opção {opçao} não existe!')
sleep(1.5)
print('Fim do programa! Volte sempre!')
