#Escreva um programa que faça o computador "pensar" em um
#número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu

import random

numero = int(input('Em que número eu pensei ? : '))

lista = [0,1,2,3,4,5]

aleatoriador = random.choice(lista)

if aleatoriador!=numero:
    print('Haha você errou, não foi dessa vez !')
else:
    aleatoriador == numero
    print ('Parabéns você ganhou!')

print ('O número que eu pensei foi: {}'.format(aleatoriador))