"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
s = float(input('Qual é o seu salário? '))
print('Um funcionário que ganhava R${:.2f}, com o aumento de 15% passa a receber R${:.2f}'.format(s, (s+(s*0.15))))
