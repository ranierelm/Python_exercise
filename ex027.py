nome = str(input('Digite seu nome completo: ')).strip()
print('Primeiro nome: {}'.format(nome.split()[0]))
ultimo = nome.count(' ')
print('Último nome: {}'.format(nome.split()[ultimo]))
