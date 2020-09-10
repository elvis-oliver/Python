peso = float(input('Digite o seu peso [kg]: '))
altura = float(input('Digite a sua altura [m]: '))
imc = peso/(altura*altura)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Seu status é: MAGREZA')
elif imc <= 24.9:
    print('Seu status é: NORMAL')
elif imc <= 29.9:
    print('Seu status é: SOBREPESO')
elif imc <= 39.9:
    print('Seu status é: OBESIDADE')
elif imc > 40:
    print('Seu status é: OBESIDADE GRAVE')
