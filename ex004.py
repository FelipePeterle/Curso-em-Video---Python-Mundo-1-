#Faça um programa que leia algo pelo teclado e mostre na tela
#O seu tipo primtivo e todas as informações possíveis sobre ela

vv = input ('Digite algo:')
print ('O tipo primitivo desse valor é: ', type (vv))
print ('Só tem espaços ?: ', vv.isspace())
print ('É um número ?: ', vv.isnumeric())
print ('É alfabético ? : ', vv.isalpha())
print ('É alfanumérico ?: ', vv.isalnum())
print ('Está em maiúscula ?: ', vv.isupper())
print ('Está em minúscula ?: ', vv.islower())
print ('Está Capitalizada ?: ', vv.istitle())