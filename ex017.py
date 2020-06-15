import math
opos = float(input('Medida do cateto oposto: '))
adj = float(input('Medida do cateto adjacente: '))

h = math.hypot(opos,adj)
#h = (opos**2 + adj**2)**0.5
print(f'A hipotenusa do triângulo é: {h:.2f}')
