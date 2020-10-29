import random
def ajuda():
    while True:
        listaC = ['\033[1;30;47m', '\033[1;31;40m', '\033[1;32;40m']
        corALE = random.choice(listaC)
        print('\033[7;30m'*40)
        print('{:^40}'.format('SISTEMA DE AJUDA'))
        print('\033[7;30m'*40)
        resp = str(input('\033[0;0mFunção ou biblioteca: '))
        print('{}'.format(corALE))
        if 'fim' in resp:
            break
        help(f'{corALE}{resp}')
        print('\033[m')
ajuda()