#Faça um programa que leia o comprimento do
#Cateto oposto e do cateto adjacente de um
#triângulo reetângulo, cacule e mostre o comprimento
#da hipotenusa

import math

co= float(input('Digite o comprimento do cateto oposto: '))
ca= float (input('Digite o comprimento do cateto adjacente'))

hp = math.sqrt(co**2+ca**2)

print('A hipotenusa vai medir {:.2f}'.format (hp))

import math

#co= float(input('Digite o comprimento do cateto oposto: '))
#ca= float (input('Digite o comprimento do cateto adjacente'))

#hp = (co**2+ca**2) ** (1/2)

#print('A hipotenusa vai medir {:.2f}'.format (hp))

##############################

#co= float(input('Digite o comprimento do cateto oposto: '))
#ca= float (input('Digite o comprimento do cateto adjacente'))

#hi = math.hypot(co,ca)

#print ('A hipotenusa é {}'.format(hi))





