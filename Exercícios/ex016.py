"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""
n = float(input('Digite um número: '))
print('{:.2f} inteiro = {}'.format(n, int(n)))
