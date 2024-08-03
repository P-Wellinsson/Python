from urllib.request import urlopen


def verifica_site(url):
    try:
        site = urlopen(url)
    except:
        print(f'\033[31mNão foi possível se conectar ao site {url}\033[m')
    else:
        print(f'O site {url} ainda está no ar.')


verifica_site('https://www.pudim.com.br/')
