p = float(input('\033[4;31mQual é o preço do produto? R$'))
d = p - p * (5/100)
print(f'\033[m\033[7;1;40mO produto que custava R${p:.2f}, na promoção com desconto de 5% vai custar R${d:.2f}\033[m')
