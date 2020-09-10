num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] para binario
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)))
else:
    print('Opção invalida!')
