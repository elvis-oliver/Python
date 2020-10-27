from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

'''if num[0] > num[1]:
    maior = num[0]
else:
    maior = num[1]
if num[2] > maior:
    maior = num[2]
elif num[3] > maior:
    maior = num[3]
elif num[4] > maior:
    maior = num[4]

if num[0] < num[1]:
    menor = num[0]
else:
    menor = num[1]
if num[2] < menor:
    menor = num[2]
elif num[3] < menor:
    menor = num[3]
elif num[4] < menor:
    menor = num[4]'''

print(num)
print(f'o maior é {max(num)}')
print(f'o menor é {min(num)}')