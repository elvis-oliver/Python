num = int(input('Digite o número do fatorial: '))
f = 1
c = num
print('{}! = '.format(num), end='')
while c >= 1:
    print(c, end='')
    if c != 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))