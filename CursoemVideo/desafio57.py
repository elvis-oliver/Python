sexo = str(input('Digite seu sexo [M/F]: ').upper())
while (sexo !='M') and (sexo !='F'):
    print('Dado incorreto, digite novamente!')
    sexo = str(input('Digite seu sexo [M/F]: ').upper())
print('Dado digitado com sucesso')