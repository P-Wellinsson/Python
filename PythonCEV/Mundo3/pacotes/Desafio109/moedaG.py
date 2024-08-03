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
