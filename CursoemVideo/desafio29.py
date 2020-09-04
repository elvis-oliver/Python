vel = float(input('Qual a velocidade atual do carro? [km/h] '))
if vel <= 70:
    print('Tenha um Bom Dia! Dirija com cuidado!')
else:
    multa = float((vel - 70) * 7)
    print('VOCÊ FOI MULTADO! sua multa é de R$ {}'.format(multa))
