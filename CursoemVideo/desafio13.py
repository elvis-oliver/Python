salario = float(input('Qual o salario do funcionario? R$ '))
print('Um funcionario que ganhava R$ {}, com aumento de 15%, irá receber R$ {:.2f}'.format(salario, salario+((salario*15)/100)))
