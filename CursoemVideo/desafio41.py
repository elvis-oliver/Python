from datetime import date
anoN = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - anoN
if idade <= 8:
    print('Sua idade é {} e sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Sua idade é {} e sua categoria é INFANTIL'.format(idade))
elif idade <= 18:
    print('Sua idade é {} e sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Sua idade é {} e sua categoria é SÊNIOR'.format(idade))
else:
    print('Sua idade é {} e sua categoria é MASTER'.format(idade))
