frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {}x em sua frase.'.format(frase.count('a')))
print('Aparece primeiro na {}ª letra da sua frase.'.format(frase.find('a')+1))
print('Aparece pela última vez na {}ª letra da sua frase.'.format((frase.rfind('a')+1)-frase.count(' ')))
