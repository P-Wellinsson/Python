SumAge = 0
oldMan = 0
maioridadeMan = 0
nameMan = ''
mul20 = 0

for people in range(1, 5):
    print(f'------ {people}ª PESSOA ------')
    name = input(f'Nome: ').strip()
    age = int(input(f'Idade: '))
    sex = input(f'Sexo: (M/F)/: ').strip() .upper()
    SumAge += age

    if sex == 'M' and people == 1:
        maioridadeMan = age
        nameMan = name
    if sex == 'M' and age > maioridadeMan:
        maioridadeMan = age
        nameMan = name
    if sex == 'F':
        mul20 += 1 if age < 20 else mul20 + 0

print('-' * 20)
print(f'A média da idade do grupo é de {SumAge/ 4} anos')
print(f'O homem mais velho tem {maioridadeMan} anos e se chama {nameMan}')
print(f'Tem {mul20} mulhere(s) com menos de 20 anos')
