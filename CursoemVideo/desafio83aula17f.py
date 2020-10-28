expr = str(input('Digite a sua expressão matematica: '))
listaA = []
listaF = []
for simb in expr:
    if simb == '(':
        listaA.append('(')
    elif simb == ')':
        listaF.append(')')
if len(listaA) == len(listaF):
    print('Expressão correta!')
else:
    print('Expressão incorreta')
