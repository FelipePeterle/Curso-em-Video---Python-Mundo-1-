#Faça um algoritmo que leia o preço de um produto e mostre
#seu novo preço, com 5% de desconto

money = float(input('Qual é o preço do produto ?: R$'))

porcentagem = 5/100
desconto=money-(porcentagem*money)


print ('O produto que custava {}, na promoção com desconto de 5% vai custar R${:.2f}'.format(money,desconto))