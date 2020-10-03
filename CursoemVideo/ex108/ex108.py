from moeda import dobro, metade, aumentar, diminuir, moeda
p = float(input('Digite um preço: '))
print('O dobro de {} é {}'.format(moeda(p), moeda(preço=dobro(p))))
print('A metade de {} é {}'.format(moeda(p), moeda(preço=metade(p))))
print('AUMENTANDO 10% de {} é {}'.format(moeda(p), moeda(preço=aumentar(p, 10))))
print('DIMINUINDO 10% de {} é {}'.format(moeda(p), moeda(preço=diminuir(p, 10))))
