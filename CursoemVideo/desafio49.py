num = int(input('Digite o número que você quer ver a tabuada: '))
for c in range(1, 11):
    print('{:2} x {:2} = {:2}'.format(num, c, num * c))
print('FIM')