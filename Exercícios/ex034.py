"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%
"""
sal = float(input('Qual é o salário do funcionário? R$'))
aumento = 0.10 if sal > 1250.00 else 0.15  # Porcentagem de aumento (0.10x = 10%)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, sal + sal * aumento))
