"""
Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('Qual o preço do produto? '))
np = p-(p*0.05)
print(' Promoção: \n De: R${:.2f} Por: R${:.2f}'.format(p, np))
