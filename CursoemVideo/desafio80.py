lista = []
print('Você irá criar uma lista com 5 valores!')
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print('ADD ao final da lista')
    else:
        pos = 0
        while pos < len(lista)-1:
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'ADD na posição {pos}')
                break
            pos += 1
print(lista)
