import random
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
print(' Estou pensando em um número entre 0 e 3, veja se você consegue advinhar...')
print('=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=')
num = int(input('Seu palpite: '))
ale = random.randint(0, 3)
if num == ale:
    print('Você acertou! Eu pensei no {} e seu palpite foi o {} PARABÉNS!'.format(ale, num))
else:
    print('Você errou, eu pensei no {} e seu palpite foi o {}'.format(ale, num))


