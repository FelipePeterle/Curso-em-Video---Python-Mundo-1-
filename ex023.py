#Faça um programa que leia um número de 0 a 9999
#E mostre na tela cada um dos digitos separados.

numero = int(input('Digite o número a ser analisado: '))
print('Analisando o número {}'.format(numero))

u= numero// 1%10
d= numero// 10%10
c= numero// 100%10
m=numero//  1000%10

print ('Unidade {}: '.format(u))
print ('Dezena {}: '.format(d))
print ('Centena {}: '.format(c))
print ('Milhar {}: '.format(m))