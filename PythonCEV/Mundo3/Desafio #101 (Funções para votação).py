def voto(age):
    """
    -> Recebe o ano de nascimento de uma pessoa e diz se a votação é obrigatória, opcional ou negado.
    :para age: ano de nascimento.
    :return: Retorna OBRIGATÓRIO se a idade for maior ou igual a 18.
    :return: Retorna OPCIONAL se a idade for maior que 15 e menor que 18 ou se for maior que 65.
    :return: Retorna NEGADO se a idade for menor que 16.
    """
    from datetime import date
    age = date.today().year - age
    if age < 16:
        return f'Com {age} anos: VOTO NEGADO.'
    elif age > 65 or 16 <= age < 18:
        return f'Com {age} anos: VOTO OPCIONAL.'
    elif age >= 18:
        return f'Com {age} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
nasc = int(input(f'Em que ano você nasceu? '))
print(voto(nasc))
