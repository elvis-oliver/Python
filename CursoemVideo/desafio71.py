print('=-'*20)
print('{:^40}'.format('BANCO OLIVEIRA'))
print('=-'*20)
valor = int(input('Digite o valor que deseja sacar: R$ '))

nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0

nota100 = int(valor / 100)
num2 = int(valor % 100)
nota50 = int((valor % 100)/50)

if nota50 > 0:
    nota20 = int(((valor % 100)-50)/20)
else:
    nota20 = int((valor % 100)/20)
if nota50 > 0 and nota20 > 0:
    nota10 = int((((valor % 100)-50)-(nota20*20))/10)
else:
    nota10 = int(((valor % 100)-(nota20*20))/10)
if nota50 > 0 and nota20 > 0 and nota10 > 0:
    nota5 = int( (((valor % 100)-50)-(nota20*20)-(nota10*10)) / 5)
else:
    nota5 = int( ((valor % 100)-(nota20*20)-(nota10*10)) / 5)
if nota50 > 0 and nota20 > 0 and nota10 > 0 and nota5 > 0:
    nota2 = int( (((valor % 100)-50)-(nota20*20)-(nota10*10)-(nota5*5)) / 2)
else:
    nota2 = int( ((valor % 100)-(nota20*20)-(nota10*10)-(nota5*5)) / 2)

if valor%50==0:
    nota20=0
    nota10=0
    nota5=0
    nota2=0

if True:
    print('NOTAS DE 100: {}'.format(nota100))
if True:
    print('NOTAS DE 50: {}'.format(nota50))
if True:
    print('NOTAS DE 20: {}'.format(nota20))
if True:
    print('NOTAS DE 10: {}'.format(nota10))
if True:
    print('NOTAS DE 5: {}'.format(nota5))
if True:
    print('NOTAS DE 2: {}'.format(nota2))

if int( ((valor % 100)-(nota20*20)-(nota10*10)-(nota5*5)-(nota2*2)) % valor) == 1 or valor == 1:
    print('=-'*20)
    print('NÃO TEMOS NOTA DE R$ 1')
    print('=-' * 20)