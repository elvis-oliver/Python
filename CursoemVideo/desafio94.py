resp = ''
pessoas={}
listaP=[]
sexo=''
totIdade = 0
while resp != 'N':
    pessoas['nome'] = str(input('Nome: '))
    pessoas['idade'] = int(input('Idade: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('Valor digitado incorreto, opções válidas [M ou F] ')
    while True:
        resp = str(input('Deseja Continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('Valor digitado incorreto, opções válidas [S ou N] ')
    totIdade += pessoas['idade']
    listaP.append(pessoas.copy())
    pessoas.clear()
print(pessoas)
print(listaP)
print('=-'*20)
print(f'A) Ao todo temos {len(listaP)} pessoas cadastradas')
print(f'B) A média de idade das pessoas cadastradas é {int(totIdade/len(listaP))}')
print(f'C) As mulheres cadastradas foram: ',end='')
for p in listaP:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}... ', end='')
print('')
print(f'D) As pessoas com idade acima da média são: ')
for p in listaP:
    if p['idade'] > (totIdade/len(listaP)):
        print(p)