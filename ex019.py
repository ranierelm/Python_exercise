import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
sorteio = [a1,a2,a3,a4]
random.shuffle(sorteio)
#Shuffle (embaralha lista)
#Choice (Escolhe 1 da lista)
print(f'Ordem de apresentação: {sorteio}')


