dist = float(input('Qual a distância da sua viagem? '))

if dist <=200:
    print(f'Valor da passagem: R${(0.5*dist):.2f}')
else:
    print(f'Valor da passagem: R${(0.45*dist):.2f}')