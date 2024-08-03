from random import randint
from time import sleep
jokenpo = ('Pedra', 'Papel', 'Tesoura')
ncomput = randint(0, 2)
print('''Suas opcões:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
sleep(1)
usuario = int(input('Digite a opçâo escolhida: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
if usuario == 0 and ncomput == 1 or usuario == 1 and ncomput == 2 or usuario == 2 and ncomput == 0:
    print(f'Você PERDEU!! \nEu coloquei {jokenpo[ncomput]}')
elif usuario == 1 and ncomput == 0 or usuario == 2 and ncomput == 1 or usuario == 0 and ncomput == 2:
    print(f'Você GANHOU!! \nEu coloquei {jokenpo[ncomput]}')
elif usuario == 0 and ncomput == 0 or usuario == 1 and ncomput == 1 or usuario == 2 and ncomput == 2:
    print(f'EMPATAMOS!\nEu coloquei {jokenpo[ncomput]} também')
else:
    print('Valor INVÁLIDO')
