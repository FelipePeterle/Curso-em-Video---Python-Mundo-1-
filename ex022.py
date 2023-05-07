#Crie um programa que leia o nome completo de uma pessoa
#E mostre:
#O nome com todas as letras maúsculas e minúsculas
#Quantas letras ao todo(sem considerar espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))

maiu = nome.upper()
minus = nome.lower()
dividir = nome.split()
contador = len(nome)-nome.count(" ")


print ('Seu nome em maiúsculas é: {} '.format(maiu))
print ('Seu nome em minusculas é: {} '.format(minus))
print ('Seu nome ao todo tem {} letras'.format(contador))
print ('Ao total seu nome tem: {}'.format (len(dividir[0])))


