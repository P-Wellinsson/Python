n1 = float(input('Primeira nota do aluno: \033[34m'))
n2 = float(input('\033[mSegunda nota do aluno: \033[34m'))
méd = (n1 + n2) /2
print(f'\033[33mA média entre {n1:.1f} e {n2:.1f} é {méd:.1f}.\033[m')
