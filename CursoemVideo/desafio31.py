dist = float(input('Digite a distância da sua viagem: [km] '))
if dist <= 200:
    valor = dist * 0.5
    print('A tarifa é de 0.5 e o valor da sua passagem será: R$ {:.2f}'.format(valor))
else:
    valor = dist * 0.25
    print('A tarifa é de 0.25 e o valor da sua passagem será R$ {:.2f}'.format(valor))
