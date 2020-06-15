n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('\n\033[31mLamento, mas você foi \033[4;31mREPROVADO.\033[m')
elif media >= 7:
    print('\n\033[7;30mPARABÉNS! VOCÊ FOI APROVADO.\033[m')
else:
    print('\n\033[31mEstude mais! Você está em recuperação.')