num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O {} é MAIOR'.format('primeiro número'))
elif num2 > num1:
    print('O {} é MAIOR'.format('segundo número'))
elif num1 == num2:
    print('Os dois são IGUAIS!')
