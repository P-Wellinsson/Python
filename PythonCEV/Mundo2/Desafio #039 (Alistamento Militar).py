from datetime import date
nasc = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year
idade = ano - nasc
print(f'Você nasceu no ano de {nasc} e tem {idade} anos de idade em {ano}')
if idade == 18:
    print('É a hora exata para você se alistar')
elif idade > 18 and idade < 180:
    print(f'Você deveria ter se alistado há {idade - 18} ano(s)')
    print(f'Seu alistamento foi em {ano -(idade - 18)}')
elif idade < 18 and idade >= 0:
    print(f'Você ainda não tem 18 anos. Faltam {18 - idade} ano(s) para o seu alistamento')
    print(f'Seu alistamento será em {ano +(18 - idade)}')
else:
    print('Valor inválido')
