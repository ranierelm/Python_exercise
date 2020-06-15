cont = 1
soma = 0
for cont in range(1,7):
    num = int(input(f'Digite {cont}º número: '))
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos número pares é: {soma}')