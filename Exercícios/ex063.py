"""
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
"""

n = int(input('Quantos termos você quer mostrar? '))
c = 1
f = 0  # inicio da sequência
ant1 = 0
ant2 = 1

print('~' * 30)
print(f, end=' -> ')
f = 1

while c < n:
    f = ant1 + ant2
    print(f, end=' -> ')

    ant2 = ant1
    ant1 = f
    c += 1

print('FIM')
print('~' * 30)

"""
Com lista:

n = int(input('Quantos termos você quer mostrar? '))
c = 0
f = [0]  # inicio da sequência

print('~' * 30)
# print(f[0], end=' -> ')

while c < n:
    if c > 0:
        if c == 1 or c == 2:
            f.append(1)
        else:
            f.append(f[c - 1] + f[c - 2])
    print(f[c], end=' -> ')
    c += 1

print('FIM')
print('~' * 30)
"""
