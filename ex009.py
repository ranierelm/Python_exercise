print('Tabuada\n')
n1 = int(input('Digite um número: '))
cont = 0
font = {'pretoebc':'\033[7;30m',
        'limpa':'\033[m'}

while cont <= 10:
    res = n1 * cont
    print('{}{} x {} = {}{}'.format( font['pretoebc'], n1, cont, res, font['limpa']))
    cont += 1
