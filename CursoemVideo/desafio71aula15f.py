print('=-'*20)
print('{:^40}'.format('BANCO OLIVEIRA'))
print('=-'*20)
valor = int(input('Digite o valor que deseja sacar: R$ '))

if (valor % 2 == 1) & (valor / 5 != 0):
    print('=-' * 20)
    print('{:^40}'.format('BANCO OLIVEIRA'))
    print('=-' * 20)
    print('Não temos moedas de R$ 1, digite o valor de saque novamente')
    valor = int(input('Digite o valor que deseja sacar: R$ '))

nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0

if (valor/100) > 0:
    nota100 = int(valor/100)
    valor = valor % 100
if (valor/50) > 0:
    nota50 = int(valor/50)
    valor = valor % 50
if (valor/20) > 0:
    nota20 = int(valor/20)
    valor = valor % 20
if (valor/10) > 0:
    nota10 = int(valor/10)
    valor = valor % 10
if (valor/5) > 0:
    nota5 = int(valor/5)
    valor = valor % 5
if (valor/2) > 0:
    nota2 = int(valor/2)
    valor = valor % 2

print('NOTAS DE 100: {}'.format(nota100))
print('NOTAS DE 50: {}'.format(nota50))
print('NOTAS DE 20: {}'.format(nota20))
print('NOTAS DE 10: {}'.format(nota10))
print('NOTAS DE 5: {}'.format(nota5))
print('NOTAS DE 2: {}'.format(nota2))

