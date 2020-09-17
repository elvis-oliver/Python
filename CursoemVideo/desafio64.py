num = int(0)
tot = int(0)
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        print('FIM')
    else:
        tot += num
print('A soma entre esses número é: {}'.format(tot))