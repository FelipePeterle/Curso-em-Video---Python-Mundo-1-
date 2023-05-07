#Faça um programa que leia o nome completo de uma pessoa,
#mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Olá ! para saber seu primeiro e último nome,\npor favor digite ele completo:')).strip()

divisão = nome.split()

print('Seu primeiro nome é {} '.format(divisão[0]))
print('Seu último nome é {}'.format(divisão[len(divisão)-1]))