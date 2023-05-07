#Desenvolva um programa que pergunte a distância de uma viagem
#em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
#Viagens de até 200Km e R$0.45 para viagens mais longas

Dist = float(input('Digite a distância que deseja percorrer: '))

Desconto = (Dist*0.50)
Caro = (Dist*0.45)

print ('Você está prestes a começar uma viagem de {}km'.format(Dist))
if Dist <=200:
    print ('E o preço da sua passagem será de R${:.2f}'.format(Desconto))
else:
    print ('E o preço de sua passagem será de R${:.2f}'.format(Caro))