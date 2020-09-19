from random import randint
print('=-'*20)
print('{:^40}'.format('VAMOS JOGAR PAR OU IMPAR'))
print('=-'*20)
while True:
    print('=-'*20)
    num = int(input('Digite um valor: [entre 1 e 10] '))
    jogador = str(input('Par ou Impar? [P/I] ').upper())
    computador = randint(1, 10)
    tot = num + computador
    if tot % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if (jogador == 'P') and (resultado == 'PAR'):
        print(f'Você jogou {num}, o computador jogou {computador}, a soma é \033[1;32m{tot}\033[1;37m, o resultado é {resultado}!')
        print('VOCÊ GANHOU')
        campeao = 1
    elif(jogador == 'I') and (resultado == 'IMPAR'):
        print(f'Você jogou {num}, o computador jogou {computador}, a soma é \033[1;32m{tot}\033[1;37m, o resultado é {resultado}!')
        print('VOCÊ GANHOU')
        campeao = 1
    else:
        print(f'Você jogou {num}, o computador jogou {computador}, a soma é \033[1;32m{tot}\033[1;37m, o resultado é {resultado}!')
        print('VOCÊ PERDEU')
        campeao = 0
    if campeao == 1:
        break
print('PROGRAMA ENCERRADO, APROVEITE SUA VITORIA!')

