a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > a:
    maior = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'Menor valor {menor}.')
print(f'Maior valor {maior}.')
