#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento. Para salários superiores a
#R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais,
#o aumento é de 15%.

salario = float(input('Qual é o salário do funcionário ? : '))

aumento1 = (salario*15/100+salario)
aumento2 = (salario*10/100+salario)

if salario <= 1250:
    print ('Quem ganhava {} passa a ganhar {:.2f}'.format(salario,aumento1))
else:
    salario>=1250
    print('Quem ganhava {} passa a ganhar {:.2f}'.format(salario,aumento2))