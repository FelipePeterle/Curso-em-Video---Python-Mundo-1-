#Escreva um programa que converta uma temperatura
#Digitada em °C e converta para °f

temperatura = float( input('Informe a temperatura em °C: '))

faren= (temperatura*9/5)+32

print ('A temperatura de {} corresponde a {}°F'.format(temperatura,faren))