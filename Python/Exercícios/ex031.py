"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
"""

dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(dist))

# Outra forma de fazer o if else abaixo:
# taxa = 0.45 if dist > 200 else 0.50

if dist > 200:  # Taxa de 0,45 para distâncias maiores que 200Km
    taxa = 0.45
else:
    taxa = 0.50

p = dist * taxa  # Cálculo de preço
print('E o preço da sua passagem será de R${:.2f}'.format(p))
