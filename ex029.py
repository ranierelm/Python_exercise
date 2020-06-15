vel = int(input('A qual velocidade você passou no radar? '))
valor = (vel - 80) * 7
if vel > 80:
    print(f'Você foi multado! \nValor da multa: R${valor}')
else:
    print('Velocidade permitida!')