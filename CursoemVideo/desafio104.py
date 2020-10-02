def leiaInt(s):
    global n
    n = input(s)

    while True:
        if n.isnumeric() == False:
            print('ERRO! Digite um número inteiro valido')
            n = input(s)
        else:
            return n
            break
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')