import random
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print(' Estou pensando em um número entre 0 e 10, veja se você consegue advinhar...')
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
num = int(input('Seu palpite: '))
ale = random.randint(0, 10)
if num == ale:
    print('Você GANHOU! Eu pensei no {} e seu palpite foi o {} PARABÉNS!'.format(ale, num))
else:
    while num != ale:
        if num < ale:
            print('MAIS! Tente novamente...')
            num = int(input('Seu palpite: '))
        if num > ale:
            print('MENOS! Tente novamente...')
            num = int(input('Seu palpite: '))
    print('Você acertou! Eu pensei no {} e seu palpite foi o {}'.format(ale, num))