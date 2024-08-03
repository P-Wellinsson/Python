num = []
ma = me = 0
for c in range(5):
    num.append(int(input(f'Digite um número para a posição {c}: ')))
    ma = ma if ma > num[c] and c != 0 else num[c]
    me = me if me < num[c] and c!= 0 else num[c]
print(f'\nO maior número digitado foi {ma} nas posicões', end=' ')
for i in range(len(num)):
    if num[i] == ma:
        print(i, end='... ')
print(f'\nO menor número digitado foi {me} nas posições ',end='')
for i in range(len(num)):
    if num[i] == me:
        print(i,end='... ')
