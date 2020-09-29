resposta = ''
listaC = []
listaPar = []
listaImpar = []
while resposta != 'N':
    num = int(input('Digite um valor: '))
    listaC.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    resposta = input('Deseja continuar? [S/N] ').upper()
print(f'A lista completa é: {listaC}')
print(f'Os números pares: {listaPar}')
print(f'Os números impares: {listaImpar}')