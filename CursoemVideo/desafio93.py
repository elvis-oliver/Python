gols = []
totG = 0
jogador = {'nome': str(input('Nome do jogador: '))}
totP = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, totP):
    quantG = int(input(f'Quantos gols na partida {c+1}? '))
    gols.append(quantG)
    totG += quantG
jogador['gols'] = gols.copy()
jogador['total'] = totG

print('=-'*20)
print(jogador)

print('=-'*20)
for i, v in jogador.items():
    print(f'O campo {i} tem o valor {v}')

print('=-' * 20)
print(f'O jogador {jogador["nome"]} jogou {totP} partida')
for c in range(0, totP):
    print(f'    => Na partida {c+1}, ele fez {jogador["gols"][c]} gols')

