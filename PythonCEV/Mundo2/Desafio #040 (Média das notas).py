nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media  = (nota1 + nota2)/ 2
print(f'A sua nota é {media:.1f}')
if media >= 7 and media <= 10:
    print('Aprovado')
elif media >= 5 and media < 7:
    print('Você está de Recuperação')
elif media >= 0 and media < 5:
    print('Reprovado')
else:
    print('Nota Inválida')
