palavras = ('VIVER', 'JOGAR', 'TRANSAR', 'AMAR', 'ESTUDAR')
for c in range(0, 5):
    for cont in range(0, len(palavras[c])):
        if (palavras[c][cont] == 'A') or (palavras[c][cont] == 'E') or (palavras[c][cont] == 'I') or (palavras[c][cont] == 'O') or (palavras[c][cont] == 'U'):
            print(f'Na palavra {palavras[c]}', end=' ')
            while palavras[c] == 'viver':
                print(' temos as vogas: ', palavras[c][cont],  end=' ')


