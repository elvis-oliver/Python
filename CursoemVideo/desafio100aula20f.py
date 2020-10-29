from random import randint

def sorteio(lista):
    for c in range(0,5):
        lista.append(randint(0,10))
    print(f'Os itens da lista são: {lista}')
def verificador(lst):
    somaPar = 0
    for i, v in enumerate(lst):
        if v % 2 == 0:
            somaPar += v
    print(f'A soma dos valores pares da lista são: {somaPar}')

números = list()
sorteio(números)
verificador(números)
