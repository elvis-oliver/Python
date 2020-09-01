'''
MINHA SOLUÇÃO
num = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(num, int(num)))
'''

from math import trunc
num = float(input('Digite um número: '))
print('O número digitado foi {} e sua porção inteire é {}'.format(num, trunc(num)))
