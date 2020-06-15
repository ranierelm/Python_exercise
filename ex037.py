import math
num = int(input('Digite um número inteiro: '))
bin = [1]
octal = [2]
hexa = [2]

print('''Escolha uma das bases para conversão:
[1] BINÁRIO
[2]OCTAL
[3] HEXADECIMAL''')
op = int(input('Sua opção: '))
#if opcao == 1:
#    print(f'{num} convertido para \033[4mBINÁRIO\033[m é igual a {bin(num)}'.strip())
if op == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}'.strip())
elif op == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}'.strip())
else:
    print('\n\033[31mOPÇÃO INVÁLIDA!')
