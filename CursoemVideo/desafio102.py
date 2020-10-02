def fatorial(num=1, show=False):
    '''
    :param num=número que o usuario deseja obter o fatorial:
    :return=retorna o resultado do fatorial:
    '''
    f = 1
    for c in range(num, f-1, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            elif c == 1:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))