valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um o {cont}° valor: ')))
    if cont == 0:
        menor = valores[0]
        maior = valores[0]
    if valores[cont] > maior:
        maior = valores[cont]
    if valores[cont] < menor:
        menor = valores[cont]
print('=-'*20)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições: ', end=' ')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições: ', end=' ')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}...', end=' ')

