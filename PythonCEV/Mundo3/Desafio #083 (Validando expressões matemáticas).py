expre = input('Digite uma expressão: ')
pilha = []
for algar in expre:
    if algar == '(':
        pilha.append('(')
    elif algar == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
print('\nSua expressão está correta!' if len(pilha)
      == 0 else '\nSua expressão está errada!')
