#Escreva um programa que leia um valor em metros
#E o exiba convertido em centímetros e milímetros

metro = float (input('Digite o valor do metro desejado:'))

centimetro = (metro)*100
milimetro =  (metro)*1000

print ('O valor do metro escolhido é de: {}\n sua conversão em centimetro vale: {}\n e sua conversão em milimetro vale: {}\n'.format(metro,centimetro,milimetro))