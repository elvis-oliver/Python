preço = float(input('Digite o preço de suas compras: R$ '))
pagamento = int(input('''FORMAS DE PAGAMENTO!
[1] a vista no dinheiro/cheque
[2] a vista no cartão
[3] 3x no cartão
[4] 4x ou mais vezes no cartão
Qual é sua opção? '''))
if pagamento == 1:
    print('Você recebeu um desconto de 10%, sua compra de R$ {} vai custar R$ {:.2f}'.format(preço, (preço-((preço*10)/100))))
elif pagamento == 2:
    print('Você recebeu um desconto de 2%, sua compra de R$ {} vai custar R$ {:.2f}'.format(preço, (preço-((preço*2)/100))))
elif pagamento == 3:
    print('Sua compra parcelada em 3 vezes vai custar 3 parcelas de R$ {:.2f}'.format(preço/3))
elif pagamento == 4:
    parcelas = int(input('Qual a quantidade de parcelas? '))
    print('Sua compra parcelada em {} vezes vai custar {} parcelas de R$ {:.2f}'.format(parcelas, parcelas, preço/parcelas))
