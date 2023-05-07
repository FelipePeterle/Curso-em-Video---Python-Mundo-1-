#Um professor quer sortear um de seus quatro alunos para apagar
#o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo do escolhido

import random

nome1 =  str(input("Escolha o primeiro aluno: "))
nome2 =  str(input("Escolha o segundo aluno: "))
nome3 =  str(input("Escolha o terceiro aluno: "))
nome4 =  str(input("Escolha o aluno aluno: "))

lista = [nome1,nome2,nome3,nome4]

sorteio = random.choices(lista)

print ('O aluno escolhido foi {' '}: '.format(sorteio))

