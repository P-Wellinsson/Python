def notas(* nota, sit=False):
    """
    -> A Função vai pegar as notas nele e a situação e mostrar a quantidade, a maior, a menore a média das notas. Além da situação se você pedir. Sendo Ótima, Boa, Mediana ou Ruim.

    :nota: Vai pegar cada nota individualmente.
    :sit: Vai ver a situação, True ou False, se for True vai mostrar a situção.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    info = {'total': len(nota), 'maior': max(nota),
            'menor': min(nota), 'média': sum(nota) / len(nota)}
    if sit:
        if 0 <= info['média'] < 5:
            info['situação'] = 'RUIM'
        elif info['média'] < 7:
            info['situação'] = 'MEDIANA'
        elif info['média'] < 10:
            info['situação'] = 'BOA'
        elif info['média'] == 10:
            info['situação'] = 'ÓTIMA, PARÁBENS'
        else:
            info['situação'] = f'Tem alguma coisa ERADA AÍ! A média está com {info["média"]}'
    return info


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
