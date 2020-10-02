def ficha(n="<desconhecido>", q=0):
    print(f'O jogador {n} fez {q} gols')


nome = str(input('Nome do jogador: '))
quantG = str(input('Quantidade de gols: '))
if quantG.isnumeric():
    quantG = int(quantG)
else:
    quantG = int(0)
if nome.strip() == '':
    ficha(q=quantG)
else:
    ficha(n=nome, q=quantG)
