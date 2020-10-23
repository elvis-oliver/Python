valorC = float(input('Valor da casa? R$ '))
salario = float(input('Salario do comprador? R$ '))
anosF = int(input('Quantos anos de financiamento? '))
print('=-'*20)
print('Para pagar uma casa de R$ {} em {} anos, a prestação será de R$ {:.2f}'.format(valorC, anosF, (valorC/(anosF*12))))
if (salario*30/100) <= (valorC/(anosF*12)):
    print('Seu emprestimo foi negado!')
elif (salario*30/100) > (valorC/(anosF*12)):
    print('Seu emprestimo foi concedido!')
else:
    print('Dados invalidos!')
