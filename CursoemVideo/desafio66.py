num = 0
soma = 0
tot = 0
while True:
    num = int(input('Digite um número [999 para interromper] '))
    if num == 999:
        break
    soma += num
    tot += 1
print(f'Você digitou {tot} valores, e a soma entre eles é {soma}')
