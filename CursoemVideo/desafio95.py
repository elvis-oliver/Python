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
    resp = input('Deseja Continuar? [S/N] ').upper()
    if resp in 'N':
        break
    print('-' * 10)
print('=-'*20)
print(time)
print(jogador)

print('=-'*50)
print('{:<5}{:<15}{:<25}{:<5}'.format('COD', 'NOME', 'GOLS', 'TOTAL'))
for j in time:
    print('{:<5} {:<15} {} {:5}'.format(j['cod'], j['nome'], j['gols'], j['total']))
    #print('{:5}{:10}{:15}{:5}'.format(j["cod"], j["nome"], j["gols"], j["total"]))
