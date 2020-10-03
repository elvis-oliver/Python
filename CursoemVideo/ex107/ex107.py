from moeda import dobro, metade, aumentar, diminuir
p = float(input('Digite um preço: '))
print('O dobro de R$ {} é R$ {}'.format(p, dobro(p)))
print('A metade de R$ {:.2f} é R$ {:.2f}'.format(p, metade(p)))
print('AUMENTANDO 10% de R$ {:.2f} é R$ {:.2f}'.format(p, aumentar(p, 10)))
print('DIMINUINDO 10% de R$ {:.2f} é R$ {:.2f}'.format(p, diminuir(p, 10)))
