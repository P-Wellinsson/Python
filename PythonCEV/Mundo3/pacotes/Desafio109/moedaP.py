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
