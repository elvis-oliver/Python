totIdade = 0
maior = 0
saveNome = ''
contM = 0
for c in range(1, 5):
    print('========== {}° PESSOA =========='.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    totIdade += idade
    if c == 1:
        maior = idade
    else:
        if idade > maior and sexo == 'M':
            maior = idade
            saveNome = nome
        if sexo == 'F' and idade < 20:
            contM += 1
print('A média de idade do grupo é de {}'.format(totIdade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, saveNome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(contM))
