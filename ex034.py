print('Parabéns você foi promovido!\n')
sal = float(input('Qual seu atual salário? R$'))
if sal > 1250:
    print(f'Seu novo salário será: R${(sal+sal*10/100):.2f}')
else:
    print(f'Seu novo salário será: R${(sal+sal*15/100):.2f}')
