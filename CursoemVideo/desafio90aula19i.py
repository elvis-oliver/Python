escola = {'aluno': str(input('Nome: ')), 'média': float(input('Média: '))}
print('=-'*40)
if escola['média'] > 7:
    for k, v in escola.items():
        print(f'{k} = {v}')
    print('Esta APROVADO!')
elif escola['média'] < 7 and escola['média'] > 3:
    for k, v in escola.items():
        print(f'{k} = {v}')
    print('Esta em RECUPERAÇÃO!')
elif escola['média'] < 3:
    for k, v in escola.items():
        print(f'{k} = {v}')
    print('Esta REPROVADO!')
