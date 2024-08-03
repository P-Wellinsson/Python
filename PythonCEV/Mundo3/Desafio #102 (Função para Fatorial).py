# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :para num: O número que vai ser calculado.
    :para show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} X' if c > 1 else f'{c} =', end=' ')
        f *= c
    return f


print(fatorial(7, show=True))  # True conta inteira. False só resultado
help(fatorial)
