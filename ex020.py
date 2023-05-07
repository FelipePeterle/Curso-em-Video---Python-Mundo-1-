#O mesmo do desafio anterior quer sortear a ordem
#de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

import random

nome1 =  str(input("Escolha o primeiro aluno: "))
nome2 =  str(input("Escolha o segundo aluno: "))
nome3 =  str(input("Escolha o terceiro aluno: "))
nome4 =  str(input("Escolha o aluno aluno: "))

lista= [nome1,nome2,nome3,nome4]
random.shuffle(lista)

print ('A ordem de apresentação foi: ')
print (lista)