'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
Começa nesse termo. Ex:t == 2  r == 5;'''
t = int(input('Qual é o primeiro termo da PA? ')) 
# E vai somando com esse.Ex: 2, 7, 12, 17, 22, etc.
r = int(input('Qual é a razão da PA? '))
cont = 1
PAres = t

while cont <= 10:
    print(PAres, end=' -> ')
    PAres += r
    cont += 1
print('FIM')
