num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
op = int(input('Qual sua opção? '))
while op != 5:
    if op == 1:
        print('=-'*20)
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, num1+num2))
        print('=-' * 20)
        print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
        op = int(input('Qual sua opção? '))
    if op == 2:
        print('=-' * 20)
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, num1*num2))
        print('=-' * 20)
        print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
        op = int(input('Qual sua opção? '))
    if op == 3:
        if num1 > num2:
            print('=-' * 20)
            print('O {} é maior que o {}'.format(num1, num2))
            print('=-' * 20)
            print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
            op = int(input('Qual sua opção? '))
        else:
            print('=-' * 20)
            print('O {} é maior que o {}'.format(num2, num1))
            print('=-' * 20)
            print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
            op = int(input('Qual sua opção? '))
    if op == 4:
        print('=-' * 20)
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
        op = int(input('Qual sua opção? '))
print('Programa encerrado!')