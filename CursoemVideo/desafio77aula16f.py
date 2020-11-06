palavras = ('VIVER', 'JOGAR', 'TRANSAR', 'AMAR', 'ESTUDAR')
for c in range(0, 5):
    print(f'Na palavra {palavras[c]}', end='')
    print(', temos as vogas: ', end='')
    for cont in range(0, len(palavras[c])):
        if (palavras[c][cont] == 'A') or (palavras[c][cont] == 'E') or (palavras[c][cont] == 'I') or (palavras[c][cont] == 'O') or (palavras[c][cont] == 'U'):
            print(palavras[c][cont], end=' ')
    print('')

