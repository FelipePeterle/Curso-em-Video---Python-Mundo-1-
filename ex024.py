#Crie um programa que leia o nome de uma cidade e digo se ela
#começa ou não com o nome Santo

cidade = str(input('Em que cidade você nasceu ? ')).strip()
print(cidade[:5].upper() == 'SANTO')


