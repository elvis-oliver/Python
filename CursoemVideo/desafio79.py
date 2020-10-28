valor = []
resposta = ''

while True:
    usuario = int(input('Digite um valor: '))
    if usuario not in valor:
        valor.append(usuario)
        print('valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')
    resposta = input('Deseja continuar? [S/N] ').upper()
    if resposta in 'Nn':
        break
valor.sort(reverse=True)
print(f'Lista final: {valor}')
