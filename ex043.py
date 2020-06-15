print('\033[7;30mTABELA DE IMC\033[m\n')

peso = float(input('Digite sua peso (kg): '))
alt = float(input('Digite sua altura (m): '))
form = peso / (alt ** 2)
#danger = \033[1;31m

print(f'IMC: {form:.1f} - ',end = '')
if form < 18.5:
        print('Abaixo do peso.')
elif form >= 18.5 and form < 25:
        print('Peso ideal.')
elif form >= 25 and form < 30:
        print('Sobrepeso.')
elif form >= 30 and form < 40:
        print('Obesidade.')
else:
        print('Obesidade mórbida.')