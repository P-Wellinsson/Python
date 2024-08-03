peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
print(f'O seu (IMC) é de {imc:.1f}')
if 18.5 > imc > 0:
    print('Você está abaixo do peso!!')
elif 25 > imc >= 18.5:
    print('Você está no peso ideal!!')
elif 30 > imc >= 25:
    print('Você está com sobrepeso!!')
elif 40 > imc >= 30:
    print('Você está com obesidade!!')
elif imc >= 40:
    print('Você está com obesidade mórbida!!')
else:
    print('Valor Inválido!!!')
