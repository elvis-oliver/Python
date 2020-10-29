from datetime import date
trabalhador = {'nome': str(input('Nome: ')),
                'ano de nascimento': int(input('Ano de Nascimento: ')),
                'carteira de trabalho': int(input('Carteira de trabalho: [0 não tem] '))}

if trabalhador['carteira de trabalho'] == 0:
    print('=-'*20)
    print(f'nome = {trabalhador["nome"]}')
    print(f'idade = {date.today().year - trabalhador["ano de nascimento"]}')
    print(f'CTPS tem o valor {trabalhador["carteira de trabalho"]}')
else:
    trabalhador['ano de contratação'] = int(input('Ano de contratação: ')),
    trabalhador['salario'] = float(input('Salario: '))
    print('=-' * 20)
    print(f'nome = {trabalhador["nome"]}')
    print(f'idade = {date.today().year - trabalhador["ano de nascimento"]}')
    print(f'CTPS tem o valor {trabalhador["carteira de trabalho"]}')
    print('ano de contratação = {}'.format(trabalhador["ano de contratação"]))
    print(f'salario = {trabalhador["salario"]}')
