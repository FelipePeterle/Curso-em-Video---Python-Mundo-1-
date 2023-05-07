#Faça um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e
#tangente desse ângulo

import math

angulo = float (input('Digite o ângulo que você deseja: '))

rad = math.radians(angulo)

seno =  math.sin(rad)
cosseno= math.cos(rad)
tangente= math.tan(rad)

print (' o valor de {} tem o seno de {:.2f}'.format(angulo,seno))
print (' o valor de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print (' o valor de {} tem a tangente de {:.2f}'.format(angulo,tangente))




