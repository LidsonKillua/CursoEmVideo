"""
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('=' * 40)
print(f'{"Gerador de PA":^40}')
print('=' * 40)

prim = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1

while c <= 10:
    print(prim, end=' -> ')
    prim += r
    c += 1

print('FIM')

"""
Método com for:

decimo = prim + (10 - 1) * r
for i in range(prim, decimo + r, r):
    print(i, end=' -> ')
print('Acabou')
"""
