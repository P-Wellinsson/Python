def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²')


l = float(input('Largura (m): '))
c = float(input('comprimento (m): '))
área(l, c)
