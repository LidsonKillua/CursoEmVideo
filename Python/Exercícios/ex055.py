"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
o menor peso lidos.
"""

maior = 0
menor = 0
# lista = []

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    # lista.append(peso)

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso


# maior = max(lista)
# menor = min(lista)

print(f'O maior peso lido foi de {maior:.1f}Kg')
print(f'O menor peso lido foi de {menor:.1f}Kg')
