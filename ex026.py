#Faça um programa que leia uma frase pelo teclado e mostra:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#E mque posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A letra A final aparece na posição {}'.format(frase.rfind('A') +1))

