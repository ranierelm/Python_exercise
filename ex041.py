ano = int(input('Seu ano de nascimento: '))
atual = 2020
idade = atual - ano

if idade <= 9:
    print('Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <=19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 40:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
