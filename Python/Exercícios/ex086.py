"""
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

m = list()

for i in range(3):
    for j in range(3):
        m.append(int(input(f'Digite um valor para [{i}, {j}]: ')))

print('-='*40)

for i in range(9):
    if (i + 1) % 3 == 0:
        print(f'[{m[i]:^5}]')
    else:
        print(f'[{m[i]:^5}]', end='')

""" Guanabara:
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        m[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('-='*40)
for i in range(3):
    for j in range(3):
        print(f'[{m[i][j]:^5}]', end='')
    print()
"""
