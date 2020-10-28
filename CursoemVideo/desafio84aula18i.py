resposta = ''
lista = []
registros = []
while resposta != 'N':
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(registros) == 0:
        mai = men = lista[1]
    if lista[1] > mai:
        mai = lista[1]
    if lista[1] < men:
        men = lista[1]
    registros.append(lista[:])
    lista.clear()
    resposta = input('Deseja continuar? [S/N] ').upper()

print(f'Ao todo foram cadastrados {len(registros)} pessoas')
print(f'O menor peso foi de {men}', end=' ')
for p in registros:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print(f'\nO maior peso foi de {mai}', end=' ')
for p in registros:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
