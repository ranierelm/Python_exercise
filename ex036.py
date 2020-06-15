print('\033[7;30mEMPRÉSTIMO CONSIGNADO\033[m\n')

vlcasa = float(input('Qual valor do imóvel? R$'))
sal = float(input('Qual é seu atual salário? R$'))
prazo = int(input('Em quantos meses quer pagar? R$'))
parcela = vlcasa/prazo

if parcela > sal*30/100:
    print('\033[0;31m\nSeu empréstimo foi negado!\033[m')
else:
    print('\n\033[7;30mParabéns!!! Seu emprestimo foi aprovado.\033[m')