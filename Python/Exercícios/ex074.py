"""
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

sort = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = sort[0]

print('Os valores sorteados foram', end=' ')
for i in sort:
    print(i, end=' ')

"""
    if i < menor:
        menor = i
    if i > maior:
        maior = i

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')"""

print(f'\nO maior valor sorteado foi {max(sort)}')
print(f'O menor valor sorteado foi {min(sort)}')
