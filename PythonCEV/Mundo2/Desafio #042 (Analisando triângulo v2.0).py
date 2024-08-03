ret1 = float(input('primeira segmento: '))
ret2 = float(input('segunda segmento: '))
ret3 = float(input('terceira segmento: '))
if ret1 + ret2 > ret3 and ret1 + ret3 > ret2 and ret2 + ret3 > ret1:
    print('Os segmentos acima podem formar triângulo') 
    if ret1 == ret2 and ret1 == ret3: 
        print('Esse é um triândulo Equilátero!')
    elif ret1 == ret3 and ret1 != ret2 or ret2 == ret3 and ret2 != ret1 or ret1 != ret2 and ret2 != ret3:
        print('E um triângulo Escaleno! ')  
    else:
        print('Esse é um triângulo Isósceles!')
else:
    print('Os segmentos não podem formar um triângulo')
