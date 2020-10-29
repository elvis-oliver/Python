gols = []
time = []
totG = 0
cod = 0
while True:
    jogador = {'cod': cod}
    cod += 1
    jogador['nome'] = str(input('Nome do jogador: '))
    totP = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, totP):
        quantG = int(input(f'Quantos gols na partida {c+1}? '))
        gols.append(quantG)
        totG += quantG
    jogador['gols'] = gols.copy()
    jogador['total'] = totG
    time.append(jogador.copy())
    jogador.clear()
    gols.clear()
    totG = 0
    resp = input('Deseja Continuar? [S/N] ').upper()
    if resp in 'N':
        break
    print('-' * 10)

print('=-'*50)
print('{:<5}{:<10}{:<15}{:<5}'.format('COD', ' NOME', '  GOLS', '   TOTAL'))
print('-'*40)
for j in time:
    s = str(j['gols'])
    print('{:<5} {:<10} {:<15} {:<5}'.format(j['cod'], j['nome'], s, j['total']))

print('=-'*40)
resp = int(input('Mostrar dados de qual jogador? [digite o id do jogador] [999 interrompe] '))
while True:
    if resp == 999:
        break
    if resp >= len(time):
        print('Jogador inexistente!')
        resp = int(input('Mostrar dados de qual jogador? [digite o id do jogador] [999 interrompe] '))
    else:
        print('levantamento do jogador {}'.format(time[resp]['nome']))
        for i, g in enumerate(time[resp]['gols']):
            print(f'na partida {i+1} fez {g} gols')
        print('=-' * 40)
        resp = int(input('Mostrar dados de qual jogador? [digite o id do jogador] [999 interrompe] '))
