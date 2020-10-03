import random
def ajuda():
    while True:
        listaC = ['\033[1;41m', '\033[1;42m', '\033[1;43m']
        corALE = random.choice(listaC)
        print('\033[1;44m-'*40)
        print('{:^40}'.format('SISTEMA DE AJUDA'))
        print('\033[1;44m-'*40)
        resp = str(input('\033[0;0mFunção ou biblioteca: '))
        print('{}'.format(corALE))
        if 'fim' in resp:
            break
        help(f'{corALE}{resp}')
ajuda()