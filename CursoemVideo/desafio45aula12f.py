from random import randint
from time import sleep
print(''' SUAS OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogadaInt = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if jogadaInt == 0:
    jogadaStr = str('PEDRA')
elif jogadaInt == 1:
    jogadaStr = str('PAPEL')
elif jogadaInt == 2:
    jogadaStr = str('TESOURA')
computador = int(randint(0, 2))
if computador == 0:
    computadorStr = str('PEDRA')
elif computador == 1:
    computadorStr = str('PAPEL')
elif computador == 2:
    computadorStr = str('TESOURA')
print('=-'*20)
if jogadaInt == computador:
    print('Jogador jogou {} - {}'.format(jogadaInt, jogadaStr))
    print('Computador jogou {} - {}.'.format(computador, computadorStr))
    print('EMPATOU!')
elif (jogadaInt == 0 and computador == 2) or (jogadaInt == 1 and computador == 0) or (jogadaInt == 2 and computador == 1):
    print('Jogador jogou {} - {}'.format(jogadaInt, jogadaStr))
    print('Computador jogou {} - {}.'.format(computador, computadorStr))
    print('VOCÊ GANHOU!')
elif (computador == 0 and jogadaInt == 2) or (computador == 1 and jogadaInt == 0) or (computador == 2 and jogadaInt == 1):
    print('Jogador jogou {} - {}'.format(jogadaInt, jogadaStr))
    print('Computador jogou {} - {}.'.format(computador, computadorStr))
    print('VOCÊ PERDEU!')
print('=-'*20)
