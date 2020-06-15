ano = int(input('Digite seu ano de nascimento: '))
atual = 2020
dif = atual - ano
if dif == 18:
    print('Você deve se alistar ainda este ano!')
elif dif < 18:
    print(f'\nNão ápito para alistamento. Volte daqui a {18-dif} anos.')
else:
    print(f'\n\033[1;31mNão ápito para serviço militar! \nDeve pagar multa pelos {dif-18} anos passados da apresentação.')