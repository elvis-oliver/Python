from datetime import date
anoN = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - anoN
print('Quem nasceu em {} tem {} anos em {}'.format(anoN, idade, date.today().year))
if idade == 18:
    print('ALISTE-SE AGORA')
elif idade < 18:
    print('Faltam {} anos para o seu alistamento obrigatorio!'.format(18 - idade))
elif idade > 18:
    print('Seu alistamento foi em {}'.format(date.today().year-(idade-18)))

