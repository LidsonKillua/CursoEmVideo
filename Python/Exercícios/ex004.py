"""
Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e mostre
algumas informações possíveis sobre ele.
"""

item = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(item)))
print('Só tem espaços? {}'.format(item.isspace()))
print('É um número? {}'.format(item.isnumeric()))
print('É alfabético? {}'.format(item.isalpha()))
print('É alfanumérico? {}'.format(item.isalnum()))
print('Está em maiúsculas? {}'.format(item.isupper()))
print('Está em minúsculas? {}'.format(item.islower()))
print('Está capitalizada? {}'.format(item.istitle()))
