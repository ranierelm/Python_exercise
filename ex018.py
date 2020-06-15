import math
ang = float(input('Digite um ângulo: '))
sn = math.sin(math.radians(ang))
cs = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O Ângulo {ang} tem seno {sn:.2f} \ncosseno {cs:.2f} e \ntangente {tg:.2f}')
