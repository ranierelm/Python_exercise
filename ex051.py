print('=' * 25)
print('   10 TERMOS DE UMA PA')
print('=' * 25)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = p + (10-1)*r
for cont in range(p, n+r, r):
    print(cont, end = ' -> ')
print('ACABOU')