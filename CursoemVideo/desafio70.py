tot = 0
tot1000 = 0
barato = 0
Nbarato = ''
print('=-' * 20)
print('{:^40}'.format('LOJAS OLIVEIRA').upper())
print('=-' * 20)
nome = str(input('Nome do produto: '))
preco = int(input('Preço: R$ ').upper())
r = str(input('Deseja Continuar? [S/N] ').upper())
barato = preco
tot = preco
if preco > 1000:
    tot1000 += 1
while r != 'N':
    print('=-'*20)
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço: R$ ').upper())
    r = str(input('Deseja Continuar? [S/N] ').upper())
    tot += preco
    if preco > 1000:
       tot1000 += 1
    if preco < barato:
        barato = preco
        Nbarato = nome
print('~'*20)
print(f'Total de suas compras: {tot}')
print(f'Total de produtos acima dos R$ 1000: {tot1000}')
print(f'O produto mais barato foi o {Nbarato} e custou R$ {barato}')
