#Crie um programa que leia um número inteiro
#e mostre na tela se ele é par ou ímpar

numero = float(input('Digite o número a ser verificado: '))

if numero %2 == 0:
    print ('O número é par')
else:
    print ('O número é impar')