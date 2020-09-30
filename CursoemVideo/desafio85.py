resposta = ''
temp = []
oficialPar = []
oficialImpar = []
for c in range(0,7):
    temp.append(int(input(f'Digite o {c+1}° valor: ')))
    if temp[c]%2==0:
        oficialPar.append(temp[c])
    else:
        oficialImpar.append(temp[c])
print(temp)
print(f'Os valores pares digitados foram: {oficialPar}')
print(f'Os valores impares digitados foram: {oficialImpar}')
