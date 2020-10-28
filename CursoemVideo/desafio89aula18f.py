r = ''
registros = []
dados = []
soma = 0
resp = -1
while r != 'N':
    if not registros:
        id = 0
        dados.append(id)
    else:
        id += 1
        dados.append(id)
    dados.append(str(input('Nome: ')))
    nota1 = float(input('1° Nota: '))
    dados.append(float(nota1))
    nota2 = float(input('2° Nota: '))
    dados.append(float(nota2))
    media = (nota1+nota2) / 2
    dados.append(media)
    registros.append(dados[:])
    dados.clear()
    nota = media = soma = 0
    r = input('Deseja Continuar? [S/N] ').upper()
print('{:5}{:10}{:5}'.format('ID', 'NOME', 'MÉDIA'))
print('-'*20)
for c in range(0, len(registros)):
    print('{:<5}{:10}{:5}'.format(registros[c][0], registros[c][1], registros[c][4]))
while resp != 999:
    resp = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    while resp != 999:
        if resp in registros[0]:
            print(f'As notas de {registros[resp][1]} são {registros[resp][2]} e {registros[resp][3]}')
            resp = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
        else:
            print(f'Não tenho esse registro, tente novamente...')
            resp = int(input('Mostrar notas de qual aluno? [999 interrompe] '))