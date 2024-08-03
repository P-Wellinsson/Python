n = int(input('Digite um número inteiro: '))
print('''Qual é a conversão da base? 
[1] para binário 
[2] para Octal 
[3] para hexadecimal''')
opção = int(input('Opção: '))
if opção == 1:
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Valor Inválido')
