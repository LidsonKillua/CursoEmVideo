"""
Faça um programa que leia a largura e a altura de uma parede em metros,
e a quantidade de tinta necessária para pintá-la, sabendo que cada
litro de tinta pinta uma área de 2m²
"""
larg = float(input('Quantos metros de largura? '))
alt = float(input('Quantos metros de altura? '))
area = larg*alt
qtd = area/2
print('A área é de {:.2f}m² e precisa de {:.2f}l de tinta para ser pintada'.format(area, qtd))
