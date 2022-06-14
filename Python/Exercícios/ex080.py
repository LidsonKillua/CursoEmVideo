"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

val = 0
vals = []

vals.append(int(input('Digite um valor: ')))
print('Adicionado ao final da lista...')

for v in range(4):
    val = int(input('Digite um valor: '))

    for i in range(len(vals)):
        if val <= vals[i]:
            vals.insert(i, val)
            print(f'Adicionado na posição {i} da lista...')
            break

        elif i == len(vals) - 1:
            vals.append(val)
            print('Adicionado ao final da lista...')

print('-='*50)
print(f'Os valores digitados em ordem foram {vals}')
