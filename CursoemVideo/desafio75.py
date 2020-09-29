listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.2)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for c in range(0, 10, 2):
    print('{:30} R$ {:5.2f}'.format(listagem[c], listagem[c+1]))