num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
if num1 > num2:
    maior = num1
else:
    maior = num2
if num1 < num2:
    menor = num1
else:
    menor = num2
num3 = int(input('Terceiro valor '))
if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3
print('O MENOR VALOR DIGITADO FOI {}'.format(menor))
print('O MAIOR VALOR DIGITADO FOI {}'.format(maior))
