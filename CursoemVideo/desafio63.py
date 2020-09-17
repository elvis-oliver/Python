print('=-'*20)
print('Sequencia de Fibonacci')
print('=-'*20)
quant = int(input('Quantos termos você quer mostrar? '))
t1 = int(0)
t2 = int(1)
t3 = int(t1 + t2)
print('~'*20)
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= quant:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
