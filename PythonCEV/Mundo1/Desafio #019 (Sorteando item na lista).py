from random import choice
a1 = input('\033[33mPrimeiro aluno: \033[31m').title()
a2 = input('\033[33mSegundo aluno: \033[31m').title()
a3 = input('\033[33mTerceiro aluno: \033[31m').title()
a4 = input('\033[33mQuarto aluno: \033[31m').title()
list = [a1, a2, a3, a4]
print(f'\033[35mO aluno escolhido foi: \033[36m{choice(list)}\033[m')
