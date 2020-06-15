#Make a program ... calculate the sum of all odd numbers, multiples of 3 and in the range 1 to 500.

s = 0
for cont in range(1,501):
    if cont%2==1 and cont%3==0:
        s += cont
print(f'The sum is {s}')