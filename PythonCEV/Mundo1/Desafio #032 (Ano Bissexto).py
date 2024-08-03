from datetime import date
ano = int(input('\033[34mDigite algum ano para analisar, 0 sendo para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano% 4 == 0 and ano% 100 != 0 or ano % 400 == 0:
    print(f'\033[32mO ano {ano} é bissexto!!\033[m')
else:
    print(f'\033[31mO ano {ano} não é bissexto.\033[m')
