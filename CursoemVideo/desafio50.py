num = int(0)
soma = int(0)
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos números pares é: {}'.format(soma))
