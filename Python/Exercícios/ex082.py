"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas.
"""

val = 0

vals = []
par = []
impar = []

while True:
    val = int(input('Digite um número: '))
    vals.append(val)

    if val % 2 == 0:
        par.append(val)
    else:
        impar.append(val)

    if not input('Quer continuar? [S/N] ')[0] in 'Ss':
        break

print('-='*40)
print(f'A lista completa é {vals}')
print(f'A lista dos pares é {par}')
print(f'A lista dos ímpares é {impar}')
