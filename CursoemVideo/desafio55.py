menor = float(0)
maior = float(0)

for c in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor foi: {} kg'.format(menor))
print('O maior foi: {} kg'.format(maior))
