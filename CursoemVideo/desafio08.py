met = int(input('Digite a distancia em metros: '))
print('='*20)
print('quilometro: {} \nhectometro: {} \ndecametro: {} \ndecimetro: {} \ncentimetro: {} \nmilimetro: {}'
      .format(met/1000, met/100, met/10, met*10, met*100, met*1000))