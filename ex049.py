# Multiplication table
from time import sleep
n1 = int(input('Enter a number: '))
for cont in range(0,11):
    print(f'{n1} x {cont} = {n1*cont}')
    sleep(1)