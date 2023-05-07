#Crie um programa que leia um número real qualquer
#pelo teclado e mostre na tela a sua
#porção inteira

import math


num = float(input('Digite um número real: '))

print ('A porção inteira de {} é igual a {}'.format(num,math.floor(num)))