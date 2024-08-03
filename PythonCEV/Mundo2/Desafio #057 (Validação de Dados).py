#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = input('Digite o seu sexo [M/F] ').strip().upper() [0]
while not sex in ('MF'):
    sex = input('\nDados Ínvalidos!! \nDigite o seu sexo novamente [M/F] ').strip().upper() [0]
print(f'\nTudo certo! \nSexo: {sex} registrado com sucesso! ')
