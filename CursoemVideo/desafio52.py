num = int(input('Digite um número: '))
contP = int(0)
for c in range(num, 0, -1):
    if num % c == 0:
        contP += 1
        print('{} é divisivel por: {}'.format(num, c))
if contP == 2:
    print('o número {} é primo'.format(num))
else:
    print('o número {} NÃO é primo'.format(num))

