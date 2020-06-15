cidade = str(input('Em que cidade você nasceu? ')).strip()
cidade = cidade.lower()
print('A sua cidade possui SANTO no nome ? {}'.format('santo' in cidade))
print('Começa com o nome SANTO? {}'.format(cidade[:5]=='santo'))
