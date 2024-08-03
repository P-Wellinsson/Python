expre = input('Digite a expressão: ')
pilha = list()
for simb in expre:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('Sua expressão está válida!' if len(pilha)
      == 0 else 'Sua expressão está errada!')
