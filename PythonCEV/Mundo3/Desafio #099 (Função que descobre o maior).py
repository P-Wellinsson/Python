from time import sleep


def maior(* num):
    mai = 0
    print('-=' * 30)
    print('Analisando valores passados...')
    for c, n in enumerate(num):
        print(n, end=' ', flush=True)
        sleep(0.3)
        mai = mai if mai >= n and c != 0 else n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
