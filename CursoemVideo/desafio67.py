while True:
    num = int(input('Quer ver a tabuada de qual número? [valor negativo interrompe] '))
    if num < 0:
        break
    for c in range (1, 11):
        print(f'{num:^5} x {c:^5} = {num*c:^5}')
print('PROGRAMA ENCERRADO')