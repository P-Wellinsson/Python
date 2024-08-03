def aumentar(preço=0, taxa=0, format=False):
    resp = moeda(preço + preço * taxa/100, formatado=format)
    return resp


def diminuir(preço=0, taxa=0, format=False):
    resp = moeda(preço - preço * taxa/100, formatado=format)
    return resp


def dobro(preço=0, format=False):
    resp = moeda(preço * 2, formatado=format)
    return resp


def metade(preço=0, format=False):
    resp = moeda(preço / 2, formatado=format)
    return resp


def moeda(preço=0, moeda='R$', formatado=False):
    if formatado:
        return f'{moeda}{preço:>2.2f}'.replace('.', ',')
    else:
        return f'{moeda}{preço:>.2f}'


def resumo(preço=0, aumento=0, redução=0, format=False):
    print(f'''{"-" * 35}
{"RESUMO DO VALOR":^35}
{"-" * 35}
Preço analisado:{moeda(preço, formatado=format):>20}
Dobro do preço:{dobro(preço, format):>20}
Metade do Preço:{metade(preço, format):>20}
20% de aumento:{aumentar(preço, aumento, format):>20}
12% de redução:{diminuir(preço, redução, format):>20}
{"-" * 35}''')
