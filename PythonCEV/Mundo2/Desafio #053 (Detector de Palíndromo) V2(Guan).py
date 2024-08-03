# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = input('Digite uma frase: ').upper().strip()
word = frase.split()
junt = ''.join(word)
inverse = ''
for letra in range(len(junt) - 1, -1, -1):
    inverse += junt[letra]
print(f'O inverso de {junt} é {inverse}')
if junt == inverse:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
