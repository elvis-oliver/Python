from datetime import date
menor = int(0)
maior = int(0)
for c in range(1,8):
    anoN = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = date.today().year - anoN
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também {} pessoas menores de idade'.format(menor))