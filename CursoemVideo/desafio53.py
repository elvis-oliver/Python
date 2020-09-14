frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
i = str('')
for c in range(len(frase), 0, -1):
    i += frase[c-1]
print('O inverso de {} é {}'.format(frase, i))
if frase == i:
    print('Temos um palindromo')
else:
    print('Não temos um palindromo')