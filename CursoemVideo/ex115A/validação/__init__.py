def menu():
    print('\033[m-'*40)
    print('{:^40}'.format('MENU PRINCIPAL'))
    print('-' * 40)
    print('\033[1;33m1 - \033[1;34mVer pessoas cadastradas'
          '\n\033[1;33m2 - \033[1;34mCadastrar novas pessoas'
          '\n\033[1;33m3 - \033[1;34mSair do Programa\033[m')
    print('-' * 40)

def validar(txt):
    while True:
        try:
            op = int(input(txt))
        except:
            print('\033[1;31mERRO, OPÇÃO INVÁLIDA!')
        else:
            while op != 3:
                if op == 1 or op == 2 or op == 3:
                    if op == 1:
                        print('\033[m-' * 40)
                        print('{:^40}'.format('OPÇÃO 1'))
                        print('-' * 40)
                        menu()
                        op = int(input(txt))
                    elif op == 2:
                        print('\033[m-' * 40)
                        print('{:^40}'.format('OPÇÃO 2'))
                        print('-' * 40)
                        menu()
                        op = int(input(txt))
                else:
                    print('\033[1;31mDigite um número válido')
                    menu()
                    op = int(input(txt))
            print('\033[1;37m-' * 40)
            print('{:^40}'.format('SAINDO DO PROGRAMA'))
            print('-' * 40)
            break
