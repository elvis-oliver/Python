resposta = ''
lista = []
while resposta != 'N':
    lista.append(int(input('Digite um valor: ')))
    resposta = input('Deseja continuar? [S/N] ').upper()
print(f'Você digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 esta na lista? VERDADEIRO')