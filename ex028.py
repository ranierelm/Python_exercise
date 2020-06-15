import random
escolha = random.randint(0,5)
num = int(input('Escolha 1 número entre 0 e 5: '))
if num == escolha:
    print('Parabéns, você venceu!')
else:
    print(f'Você perdeu! Número correto: {escolha}')
