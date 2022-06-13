"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input('Digite um número: '))
qtd = 0

for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[1;36m{i}', end=' ')
        qtd += 1

    else:
        print(f'\033[1;31m{i}', end=' ')

print('\033[0;0m')
print(f'O número {num} foi divisível {qtd} vezes')

if qtd == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
