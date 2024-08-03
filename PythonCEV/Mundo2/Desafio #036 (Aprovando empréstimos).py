casa = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o seu sálario? R$'))
ano = int(input('Em quantos anos você vai pagar? '))
prest =  casa /(ano * 12)
print(f'Para uma casa que custa R${casa:.2f} em {ano} anos, a pretação será de R${prest:.2f}')
if prest <= sal * 30/100:
    print('Emprestimo aprovado! ')
else:
    print('Emprestimo negado! ')
