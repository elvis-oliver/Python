s = int(0)
cont = int(0)
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        s += c
    print(c, end=' ')
print('\nA soma entre todos os {} números impares que são multiplos de 3 é {}'.format(cont, s))

