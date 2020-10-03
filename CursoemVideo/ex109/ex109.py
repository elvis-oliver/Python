from moeda import dobro, metade, aumentar, diminuir, moeda
p = float(input('Digite um preço: '))
print('O dobro de {} é {}'.format(moeda(p), dobro(p, True)))
print('A metade de {} é {}'.format(moeda(p), metade(p, True)))
print('AUMENTANDO 10% de {} é {}'.format(moeda(p), aumentar(p, 10, True)))
print('DIMINUINDO 10% de {} é {}'.format(moeda(p), diminuir(p, 10, True)))
