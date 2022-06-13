"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
"""
print('=' * 40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('=' * 40)

prim = int(input('Primeiro termo: '))
r = int(input('Razão: '))

"""
termo = prim
for i in range(0, 10):
    print(termo, end=' -> ')
    termo += r
print('Acabou')
"""

decimo = prim + (10 - 1) * r
for i in range(prim, decimo + r, r):
    print(i, end=' -> ')
print('Acabou')
