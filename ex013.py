#Faça um algoritmo que leia o salário de um funcionário e
#Mostre seu novo salário, com 15% de aumento.

dindin = float(input("Qual é o salário do funcionário ?: R$"))

porcentagem=15/100
aumento=dindin+(porcentagem*dindin)

print ('Um funcionário que ganhava R$ {}, com 15% de aumento, passa a receber R${:.2f}'.format(dindin,aumento))