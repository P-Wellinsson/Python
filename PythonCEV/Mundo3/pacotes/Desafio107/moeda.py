def aumentar(preç, taxa):
    resp = preç + preç * (taxa / 100)
    return resp


def diminuir(preç, taxa):
    resp = preç - preç * (taxa / 100)
    return resp


def dobro(preç):
    resp = preç * 2
    return resp


def metade(preç):
    resp = preç / 2
    return resp
