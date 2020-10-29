from time import sleep
def cont10():
    print('CONTANDO DE 1 ATÉ 10, DE 1 EM 1')
    for c in range(1, 11):
        print(f'{c}...', end='')
        sleep(0.5)
    print()
def cont10S():
    print('CONTANDO DE 10 ATÉ 0, DE 2 EM 2')
    for c in range(10, 0, -2):
        print(f'{c}...', end='')
        sleep(0.5)
    print()
def contP(i, f, p):
    print(f'CONTANDO DE {i} ATÉ {f}, DE {p} EM {p}')
    for c in range(i, f, p):
        print(f'{c}...', end='')
        sleep(0.5)
    print()

cont10()
print('=-'*20)
cont10S()
print('=-'*20)
contP(i=int(input('INICIO: ')), f=int(input('FIM: ')), p=int(input('PASSO: ')))

