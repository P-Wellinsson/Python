def aumentar(preço=0, taxa=0, format=False):
    resp = preço + preço * taxa/100
    return resp if not format else moeda(resp)


def diminuir(preço=0, taxa=0, format=False):
    resp = preço - preço * taxa/100
    return resp if not format else moeda(resp)


def dobro(preço=0, format=False):
    resp = preço * 2
    return resp if not format else moeda(resp)


def metade(preço=0, format=False):
    resp = preço / 2
    return resp if not format else moeda(resp)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>2.2f}'.replace('.', ',')


def resumo(preço=0, aumento=10, redução=5, format=False):
    print(f'''{"-" * 35}
{"RESUMO DO VALOR":^35}
{"-" * 35}
Preço analisado: \t{moeda(preço)}
Dobro do preço: \t{dobro(preço, format)}
Metade do Preço: \t{metade(preço, format)}
{aumento}% de aumento: \t{aumentar(preço, aumento, format)}
{redução}% de redução: \t{diminuir(preço, redução, format)}
{"-" * 35}''')
