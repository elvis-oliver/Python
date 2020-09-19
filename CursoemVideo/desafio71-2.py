num = int(input('Digite um número: '))
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
for c1 in range(1, num+1):
    if c1 % 50 == 0:
        nota50 += 1
        cont1 = c1
for c2 in range((nota50*50), num):
    if c2 % 20 == 0 and (((nota50*50)-num) > 20):
        nota20 += 1
        cont2 = c2
for c3 in range(((nota50*50)+(nota20*20)), num):
    if c3 % 10 == 0 and (((nota50*50)+(nota20*20)-num) > 10):
        nota10 += 1
for c4 in range(((nota50*50)+(nota20*20)+(nota10*10)), num):
    if c4 % 5 == 0 and (((nota50*50)+(nota20*20)+(nota10*10)-num) > 10):
        nota5 += 1
print('nota50: {}'.format(nota50))
print('nota20: {}'.format(nota20))
print('nota10: {}'.format(nota10))
print('nota5: {}'.format(nota5))
