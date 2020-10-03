def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print('\033[31mERRO! digite um número inteiro válido\033[m')
            continue
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except:
            print('\033[31mERRO! digite um número real válido\033[m')
            continue
        else:
            return num


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')