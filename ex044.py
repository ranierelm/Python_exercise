print('\033[7;30m======= LOJAS AMERICANAS =======\033[m\n')
preco = float(input('Preço das compras: R$'))

forma = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/débito
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Escolha a opção: '''))
avista = (preco - preco*10/100)
if forma == 1:
    print('Sua compra de R${:.2f} vai custa R${:.2f}'.format(preco, avista))
elif forma == 2:
    print('')
