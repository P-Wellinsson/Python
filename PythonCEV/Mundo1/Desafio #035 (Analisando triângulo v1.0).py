ret1 = float(input('\033[36mprimeira segmento: '))
ret2 = float(input('segunda segmento: '))
ret3 = float(input('terceira segmento: '))
if ret1 + ret2 > ret3 and ret1 + ret3 > ret2 and ret2 + ret3 > ret1:
    print('\033[32mOs segmentos acima podem formar triângulo')
else:
    print('\033[31;7;1mOs segmentos não podem formar um triângulo.')
print('\033[m')
