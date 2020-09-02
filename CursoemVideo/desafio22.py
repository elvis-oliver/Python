nome = input('Digite seu nome completo: ')
print('Analisando seu nome...')
print('Seu nome em maiusculas é: ', nome.upper())
print('Seu nome em minusculas é: ', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome.replace(" ", ""))))
dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format((dividido[0]), (len(dividido[0]))))

