def lin(op):
    if op == 'P':
        print('=-'*10)
    if op == 'M':
        print('=-'*20)
    if op == 'G':
        print('=-'*30)


lin('P')
print('{:^20}'.format('PEQUENO'))
lin('P')

lin('M')
print('{:^40}'.format('RELATIVAMENTE MÉDIO'))
lin('M')

lin('G')
print('{:^60}'.format('MUITO GRANDE, ENORME, GIGANTE'))
lin('G')