"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""
n = int(input('Informe um número '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000  % 10

print('Analisando o número {}'.format(u))
print('Unidade: {}'.format(d))
print('Dezena: {}'.format(c))
print('Milhar: {}'.format(m))
