from datetime import date
atual = date.today().year
nasc18 = 0
nascme = 0

for people in range(1, 8):
    years = int(input(f'Em que ano a {people}º pessoa nasceu? '))
    idad = atual - years
    nasc18 = nasc18 + 1 if idad >= 18 else nasc18 + 0
    nascme = nascme + 1 if idad < 18 else nascme + 0

print(f'{nascme} pessoa(s) não atingiram a maioridade \nE {nasc18} pessoa(s) já atingiram a maioridade')
