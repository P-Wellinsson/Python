pessoas = []
while True:
    nome = input('Nome: ').strip().capitalize()
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    med = (nota1 + nota2) / 2  # Média
    pessoas.append([nome, [nota1, nota2], med])
    resp = input('Quer continuar? [S/N] ').strip().lower()
    if resp == 'n':
        break
print('-=' * 30)
print(f'{"ID":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i in range(len(pessoas)):
    print(f'{i:<4}{pessoas[i][0]:<10}{pessoas[i][2]:>8.1f}')
while True:
    print('-' * 35)
    nota = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    if nota == 999:
        break
    while nota > i or nota < 0:  # Não existe o ID desse aluno.
        nota = int(input(
            f'ID não encontrado, digite novamente.\nMostrar notas de qual aluno? (999 interrompe): '))
    if nota == 999:
        break
    print(f'Notas de {pessoas[nota][0]} são {pessoas[nota][1]}')
print('Finalizando... \n<<< VOLTE SEMPRE >>>')
