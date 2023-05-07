#Faça um programa que leia três números e mostre qual
#é o maior e qual é o menor.

primeiro = float(input('Digite o primeiro valor: '))
segundo = float(input('Digite o segundo valor: '))
terceiro = float(input('Digite o terceiro valor: '))

if (primeiro >= segundo) and (primeiro >= terceiro):
    print ('Esse é o maior valor : {}'.format(primeiro))

if (segundo >= primeiro) and (segundo >= terceiro):
    print ('Esse é o maior valor : {}'.format(segundo))

if (terceiro >= primeiro) and (terceiro >= segundo):
    print ('Esse é o maior valor : {}'.format(terceiro))

if (primeiro <= segundo) and (primeiro <= terceiro):
    print ('Esse é o menor valor : {}'.format(primeiro))

if (segundo <= primeiro) and (segundo <= terceiro):
    print ('Esse é o menor valor : {}'.format(segundo))

if (terceiro <= primeiro) and (terceiro <= primeiro):
    print ('Esse é o menor valor : {}'.format(terceiro))
