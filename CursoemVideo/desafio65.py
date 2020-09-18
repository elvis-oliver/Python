
cTot = 1
maior = 0

num = int(input('Digite um número: '))
r = str(input('Deseja continuar? [S/N] ').upper())

tot = num
menor = num

while r != 'N':
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N] ').upper())
    tot += num
    cTot += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print('{} {} A média entre os valores digitados é: {}'.format(tot, cTot, tot/cTot))
print('O maior valor digitado foi {} e o menor valor digitado foi {}'.format(maior, menor))