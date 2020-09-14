print('='*25)
print('   10 TERMOS DE UMA PA   ')
print('='*25)
pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))
pa = int(0)
for cont in range(pt, r*10, r):
    print(pt, end=' ')
    pt += r

