from time import sleep
preço = float(input('Qual o valor das compras? R$'))
if preço <= 0:
    print('Valor incorreto')
else:
    sleep(1)
    print('''    Digite[1] para pagamentos à vista/cheque
    Digite[2] para pagamentos à vista pelo cartão
    Digite[3] para pagamentos em até 2x no cartão
    Digite[4] para pagamentos de 3x ou mais pelo cartão''')
    sleep(2)
    pagament = int(input('Digite a condição de pagamento: '))
    if pagament == 1:
        print(f'O valor do produto é de R${preço:.2f} \nCom o desconto de 10% fica por R${preço - preço * (10/100):.2f}')
    elif pagament == 2:
        print(f'O valor do produto é de R${preço:.2f} \nCom o desconto de 5% fica por R${preço - preço * (5/100):.2f}')
    elif pagament == 3:
        print(f'O valor do produto é de R${preço:.2f}, sem nenhum desconto.')
    elif pagament == 4:
        jur = preço + preço * (20/100)
        parcel = int(input('Quantas parcelas? '))
        print(f'Sua compra será parcelada em {parcel}x de R${jur/ parcel:.2f} com juros \nSua compra de R${preço:.2f}, fica por R${jur:.2f} no final')
    else:
        print('Valor INVÁLIDO')
