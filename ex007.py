#Desenvolva um programa que leia as duas
#Notas de um aluno e calculea sua média.

nota = float (input('Digite a primeira nota do aluno:'))
nota2 = float(input('Digite a segunda nota do aluno:'))
média = (nota+nota2)/2

print ('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(nota,nota2,média))