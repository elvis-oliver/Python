from random import randint
import time
print('-'*40)
print('{:^40}'.format('JOGAR NA MEGA SENA'))
print('-'*40)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('=-'*6, end='')
print('SORTEANDO {} JOGOS'.format(quant), end='')
print('=-'*6)
jogos = []
for cont in range(0, quant):
    for c in range(0, 6):
        ale = randint(1, 61)
        if ale not in jogos:
            jogos.append(ale)
        else:
            ale = randint(1, 61)
    time.sleep(1)
    print(f'{jogos[0]:^3}, {jogos[1]:^3}, {jogos[2]:^3}, {jogos[3]:^3}, {jogos[4]:^3}, {jogos[5]:^3}')
    jogos.clear()