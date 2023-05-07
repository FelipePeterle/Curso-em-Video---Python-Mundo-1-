#Faça um programa que leia um ano qualquer e mostra se ele é bissexto

from datetime import date

import calendar

ano = int(input('Digite o ano desejado para analisar,\ncoloque 0 para analisar o ano atual.'))

if ano == 0:
    ano = date.today().year


if(calendar.isleap(ano)):
    print('O ano de {} é bissexto !'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))