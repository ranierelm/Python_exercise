print('PROMOÇÃO RELÂMPAGO\n')

pr = float(input('Informe o preço: R$'))
valor = pr - (pr*5/100)
print(f'Preço com 5% desconto fica: R${valor:.2f}')