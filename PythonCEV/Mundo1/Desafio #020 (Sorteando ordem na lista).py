from random import shuffle
a1 = input('\033[34mPrimeiro aluno: \033[32m').title().strip()
a2 = input('\033[34mSegundo aluno: \033[32m').title().strip()
a3 = input('\033[34mTerceiro aluno: \033[32m').title().strip()
a4 = input('\033[34mQuarto aluno: \033[32m').title().strip()
list = [a1, a2, a3, a4]
shuffle(list)
print(f'\033[35mA ordem da apresentação será: \n\033[32m{list}\033[m')
