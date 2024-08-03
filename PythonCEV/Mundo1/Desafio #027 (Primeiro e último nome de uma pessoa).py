nome = input('\033[7;1;32mDigite o seu nome completo:\033[m ').strip().title()
separ = nome.split()
print(f'\033[36mO seu primeiro nome é \033[31m{separ[0]}.')
print(f'\033[36mO seu último nome é \033[31m{separ[len(separ)-1]}.\033[m')
