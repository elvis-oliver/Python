maior = 0
homem = 0
mulher = 0
while True:
    print('=-'*20)
    print('{:^40}'.format('CADASTRO DE PESSOAS').upper())
    print('=-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ').upper())
    r = str(input('Deseja Continuar? [S/N] ').upper())
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if (sexo == 'F') and (idade < 20):
        mulher += 1
    if r == 'N':
        break
print('~'*20)
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {homem}')
print(f'Total de mulheres com menos de 20 anos: {mulher}')
