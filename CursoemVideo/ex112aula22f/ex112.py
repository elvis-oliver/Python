from utilidades.moeda import dobro, metade, aumentar, diminuir, moeda, resumo
from utilidades.dados import leiaDinheiro

p = leiaDinheiro('Digite o preço: R$ ')
print('O dobro de {} é {}'.format(moeda(p), dobro(p, True)))
print('A metade de {} é {}'.format(moeda(p), metade(p, True)))
print('AUMENTANDO 10% de {} é {}'.format(moeda(p), aumentar(p, 10, True)))
print('DIMINUINDO 10% de {} é {}'.format(moeda(p), diminuir(p, 10, True)))

print(resumo(50, 10, 20))
