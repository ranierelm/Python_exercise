n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print('O primeiro valor é maior.')
elif n2 > n1:
    print('O segundo valor é maior.')
else:
    print('\033[31mNão existe valor maior, os dois são iguais.\033[m')