"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final,
mostre: A) Quantas pessoas foram cadastradas.
        B) Uma listagem com as pessoas mais pesadas.
        C) Uma listagem com as pessoas mais leves.
"""

pessoas = list()
pessoa = list()
peso = maxpeso = minpeso = 0

while True:
    pessoa.append(input('Nome: '))
    peso = float(input('Peso: '))
    pessoa.append(peso)

    if len(pessoas) == 0:
        maxpeso = minpeso = peso
    else:
        if peso > maxpeso:
            maxpeso = peso
        if peso < minpeso:
            minpeso = peso

    pessoas.append(pessoa)
    pessoa.clear()

    if input('Quer continuar? [S/N] ')[0] not in 'Ss':
        break

print('-=' * 40)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
strmax = strmin = ''

for pessoa in pessoas:
    if pessoa[1] == maxpeso:
        strmax += f'[{pessoa[0]}] '
    if pessoa[1] == minpeso:
        strmin += f'[{pessoa[0]}] '

print(f'O maior peso foi de {maxpeso:.1f}Kg. Peso de {strmax}')
print(f'O menor peso foi de {minpeso:.1f}Kg. Peso de {strmin}')
