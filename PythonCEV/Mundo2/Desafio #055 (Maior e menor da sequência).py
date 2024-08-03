ma = 0
me = 9999990

for people in range(1, 6):
    peso = float(input(f'Qual é o peso da {people}ª pessoa? '))
    ma = peso if peso > ma else ma + 0
    me = peso + (me - me) if peso < me else me + 0

print(f'O maior peso lido foi {ma}Kg e o menor foi {me}Kg.')
