#Faça um programa que leia a largura e a altura de uma parede
#Em metros, calcula a sua área e a quantidade de tinta
#Necessária para pintálo. Sabendo que cada litro
#De tinta, pinta uma área de 2m^2

Largura = float(input('Largura da parede:'))
Altura = float (input('Altura da parede:'))

Calculolarguraaltura= Largura*Altura
Tinta= Calculolarguraaltura/2

print ('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(Largura,Altura,Calculolarguraaltura))
print ('Para pintar essa parede, você precisará de {}l de tinta'.format(Tinta))
