matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
somaColuna = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'VALOR {l}/{c}: '))

print('=-'*20)
print(matriz[0])
print(matriz[1])
print(matriz[2])

for l in range(0, 3):
    for c in range(0, 3):
        soma += matriz[l][c]
        if c == 2:
            somaColuna += matriz[l][c]
        if matriz[l][c] > maior:
            maior = matriz[l][c]
print('=-'*20)
print('A soma do valores da matriz é: {}'.format(soma))
print('A soma dos valores da terceira coluna é {}'.format(somaColuna))
print('O maior valor digitado foi {}'.format(maior))