def lin():
    print('=-'*20)
def area(b, h):
    a = b * h
    print(f'A área de um terreno {b} x {h} é igual a {a}m²')

lin()
print('{:^}'.format('CONTROLE DE TERRENOS'))
lin()
area(b=float(input('LARGURA [m]: ')), h=float(input('COMPRIMENTO [m]: ')))