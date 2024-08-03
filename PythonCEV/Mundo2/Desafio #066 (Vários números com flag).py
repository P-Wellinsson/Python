n = c = s = 0
while True:
    n = int(input('Digite um número [999 para parar]: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} números e a soma entre eles foi de {s}!')
