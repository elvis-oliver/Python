a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if (a < b + c and b < a + c and c < a + b) and ((a != b) and (b != c) and (a != c)):
    print('PODE formar um triangulo ESCALENO!')
elif (a < b + c and b < a + c and c < a + b) and ((a == b != c) or (b == c != a) or (a == c != b)):
    print('PODE formar um triangulo ISOCELES!')
elif (a < b + c and b < a + c and c < a + b) and ((a == b) and (b == c) and (a == c)):
    print('PODE formar um triangulo EQUILATERO!')
else:
    print('NÃO PODE formar um triangulo!')
