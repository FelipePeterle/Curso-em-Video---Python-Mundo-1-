#Crie um programa que leia quanto dinheiro uma pessoa tem
#Na carteira e mostre quantos dólares ela pode comprar

reais = float (input('Quanto dinheiro você tem na carteira ?: R$'))

realdolar= reais/ 3.27



print('Com {:.2f} você pode comprar US$ {:.2f}'.format (reais,realdolar))