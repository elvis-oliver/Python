nome = input('Digite seu nome completo: ').upper().strip()
nome2 = nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome2[0]))
print('Seu ultimo nome é {}'.format(nome2[len(nome2)-1]))

