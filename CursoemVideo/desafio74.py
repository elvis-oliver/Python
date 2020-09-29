contNove = 0
posTres = 0
contPar = 0
num = (int(input('Digite primeiro número: ')),
       int(input('Digite segundo número: ')),
       int(input('Digite terceiro número: ')),
       int(input('Digite quarto número: ')))
for c in range(0, 4):
    if num[c] == 9:
        contNove += 1
for c in range(3, -1, -1):
    if num[c] == 3:
        posTres = c
for c in range(0, 4):
    if num[c] % 2 == 0:
        contPar += 1
print(f'os números digitados foram: {num}')
print(f'o valor {9} apareceu {contNove} vezes')
print(f'o valor {3} apareceu primeiro na posição {posTres + 1}')
print(f'a quantidade de números pares foi: {contPar}')

