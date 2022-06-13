"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import sin, cos, tan, radians
n = radians(int(input('Digite o ângulo que você deseja: ')))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(n, sin(n)))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(n, cos(n)))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(n, tan(n)))
