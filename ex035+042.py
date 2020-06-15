r1 = float(input('1º segmento de reta: '))
r2 = float(input('2º segmento de reta: '))
r3 = float(input('3º segmento de reta: '))

if r1+r2>r3 or r2+r3>r1 or r3+r1>r2:
    print('\nOs segmentos acima \033[4mPODEM FORMAR\033[m um ',end='')
    if r1 == r2 == r3:
        print('triângulo EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('triângulo ESCALENO.')
    else:
        print('triângulo ISÓSCELES.')
else:
    print('\nOs segmentos de retas NÃO PODEM formar um triângulo.')
