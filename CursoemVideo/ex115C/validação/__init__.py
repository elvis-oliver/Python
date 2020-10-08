import codecs
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
            if op == 3:
                print('\033[1;37m-' * 40)
                print('{:^40}'.format('SAINDO DO PROGRAMA'))
                print('-' * 40)
                return op
                break
            elif op == 1 or op == 2:
                return op
                break
            else:
                print('\033[1;31mERRO, Digite um número válido!')
                menu()
def opções(op):
    while True:
        if op == 3:
            break
        else:
            if op == 1:
                print('\033[m-' * 40)
                print('{:^40}'.format('OPÇÃO 1'))
                print('-' * 40)

                try:
                    arquivo = 'pessoas'
                    arquivo = open(arquivo, 'r+', encoding='utf-8')
                    for line in arquivo:
                        valores = line.split(';')
                        valores[1] = valores[1].replace("\n", "")
                        print(f'Nome: {valores[0]:<20} Idade: {valores[1]}')

                except FileNotFoundError:
                    arquivo = open(arquivo, 'w+', encoding='utf-8')
                    # arquivo.writelines(u'')
                    print('Arquivo pessoas criado com sucesso ')
                menu()
                op = validar('\033[1;33mSua opção: ')

            elif op == 2:
                print('\033[m-' * 40)
                print('{:^40}'.format('OPÇÃO 2'))
                print('-' * 40)

                arquivo = open('pessoas', 'r', encoding='utf-8')
                conteudo = arquivo.readlines()
                conteudo.append(input('Nome: '))
                conteudo.append(';')
                conteudo.append(input('Idade: '))
                arquivo.close()

                arquivo = open('pessoas', 'w', encoding='utf-8')
                arquivo.writelines(conteudo)
                arquivo.write("\n")
                arquivo.close()

                print('Registro adcionado com sucesso')
                menu()
                op = validar('\033[1;33mSua opção: ')

