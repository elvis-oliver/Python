def dobro(preço):
    d = preço * 2
    return d


def metade(preço):
    m = preço / 2
    return m


def aumentar(preço, taxa):
    res = preço + ((preço * taxa) / 100)
    return res


def diminuir(preço, taxa):
    res = preço - ((preço * taxa) / 100)
    return res
