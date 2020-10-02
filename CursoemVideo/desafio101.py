from datetime import date
def voto(anoN):
    idade = date.today().year - anoN
    if (idade < 16):
        return 'NÃO VOTA'
    elif (idade >= 16 and idade < 18) or (idade >= 70):
        return 'VOTO OPCIONAL'
    elif (idade >= 18) and (idade < 70):
        return 'VOTO OBRIGATORIO'


anoN = int(input('Ano de Nascimento: '))
idade = date.today().year - anoN
print(f'Com {idade} anos: {voto(anoN)}')