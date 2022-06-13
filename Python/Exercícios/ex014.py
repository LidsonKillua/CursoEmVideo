"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

c = float(input('Informe a temperatura em ºC: '))
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(c, (c * 1.8 + 32)))
