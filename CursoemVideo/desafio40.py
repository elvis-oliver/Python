nome = input('Digite o nome do aluno: ')
nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print('O aluno {} teve média {:.2f} e esta APROVADO!'.format(nome, media))
elif 3 <= media < 7:
    print('O aluno {} teve média {:.2f} e esta em RECUPERAÇÃO!'.format(nome, media))
elif media < 3:
    print('O aluno {} teve média {:.2f} e esta REPROVADO!'.format(nome, media))
