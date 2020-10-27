num = int(input('Digite um número entre 0 e 20: '))
numE = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
if (num >= 0) and (num <= 20):
    print(f'Você digitou o número {numE[num]}')
else:
    print('ERRO')
    num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numE[num]}')