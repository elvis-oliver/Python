from random import randint
from operator import itemgetter
jogadores={}
ranking = {}
jogadores = {'JOGADOR 1': randint(1, 6),
             'JOGADOR 2': randint(1, 6),
             'JOGADOR 3': randint(1, 6),
             'JOGADOR 4': randint(1, 6)}

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('{:-^25}'.format('RANKING'))
cont = 1
for k, v in ranking:
    print(f'{cont}° LUGAR: {k}, pontos = {v}')
    cont += 1