print('='*25)
print('   10 TERMOS DE UMA PA   ')
print('='*25)
pt = int(input('Primeiro termo: '))
inicio = pt
r = int(input('Razão: '))
quant = 10
Cquant = 0
while quant != 0:
    for cont in range(pt, r*(quant+1), r):
        print(inicio, end=' ')
        inicio += r
    Cquant += quant
    quant = int(input('\nQuantos termos você quer mostrar a mais? '))
print('Foram {} interações'.format(Cquant))
