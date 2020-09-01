altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f} m²'.format(altura, largura, altura*largura))
print('Você precisará de {:.2f} litros de tinta para pinta-la'.format((altura*largura)/2))
