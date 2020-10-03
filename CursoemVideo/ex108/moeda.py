def dobro(preço=0):
    d = preço * 2
    return d


def metade(preço=0):
    m = preço / 2
    return m


def aumentar(preço=0, taxa=0):
    res = preço + ((preço * taxa) / 100)
    return res


def diminuir(preço=0, taxa=0):
    res = preço - ((preço * taxa) / 100)
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
