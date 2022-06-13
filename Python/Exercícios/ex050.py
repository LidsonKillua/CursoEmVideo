"""
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

s = 0
cont = 0

for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        cont += 1

print(f'A soma dos {cont} números pares foi de {s}')
