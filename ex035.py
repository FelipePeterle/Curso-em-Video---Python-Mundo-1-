#Desenvolva um programa que leia o comprimento de três retas e diga ao
#usuário se elas podem ou não formar um triângulo

print ('-=-=-='*8)
print ('Analisador de Triãngulos')
print ('-=-=-='*8)

lado1 =(float(input('Digite o primeiro lado do triângulo: ')))
lado2 = (float(input('Digite o segundo lado do triângulo: ')))
base = (float(input('Digite o base lado do triângulo: ')))

if lado1<lado2 + base and lado2<lado1 + base and base< lado1+lado2:
    print ('Os segmentos acima podem formar triângulo')
else:
    print('Os segmentos acima não podem formar triângulo.')



