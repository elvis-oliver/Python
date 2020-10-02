maior = 0
def maior(* num):
    print(f'Os número foram: {num}')
    print(f'Foram incluidos {len(num)} números')
    for i, n in enumerate(num):
        if i == 0:
            maior = n
        elif n > maior:
            maior = n
    print(f'o maior número foi {maior}')
    print('=-'*20)

maior(1,2,3,4,5)
maior(1,2,3)