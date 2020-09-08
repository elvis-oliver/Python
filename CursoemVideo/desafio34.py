salario = float(input('Qual o salario do funcionario? R$ '))
if salario < 2000:
    salario = salario + ((salario*15)/100)
else:
    salario = salario + ((salario*10)/100)
print('Seu novo salario é de R$ {}'.format(salario))
