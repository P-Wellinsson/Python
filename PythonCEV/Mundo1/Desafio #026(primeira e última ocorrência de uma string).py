frase = input('\033[34mDigite uma frase: ').strip().upper()
print(f'\033[37mA letra A aparece {frase.count("A")} vez(es)')
print(f'\033[32mAparecendo pela primeira vez na posição {frase.find("A")+1}')
print(f'\033[33mpela última vez na posição {frase.rfind("A") + 1}\033[m')
