vel = int(input('\033[37mDigite a velocidade do carro? '))
if vel > 80:
    print(f'\033[31mVocê foi multado e a multa foi de R${(vel - 80) * 7:.2f}!')
print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
