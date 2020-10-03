def dobro(preço=0, formato=False):
    d = preço * 2
    return d if formato is False else moeda(d)


def metade(preço=0, formato=False):
    m = preço / 2
    return m if formato is False else moeda(m)


def aumentar(preço=0, taxa=0, formato=False):
    res = preço + ((preço * taxa) / 100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0,  formato=False):
    res = preço - ((preço * taxa) / 100)
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
