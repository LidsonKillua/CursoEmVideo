"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
"""
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
print('A média das notas {:.2f} e {:.2f} é: {:.2f}'.format(nota1, nota2, media))
