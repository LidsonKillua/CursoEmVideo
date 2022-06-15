"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

vals = [[], []]

for i in range(7):
    val = int(input(f'Digite o {i+1}º valor: '))

    if val % 2 == 0:
        vals[0] += [val]  # vals[0].append(val)
    else:
        vals[1] += [val]  # vals[1].append(val)

print('-=' * 40)
print(f'Os valores pares digitados foram {sorted(vals[0])}')
print(f'Os valores ímpares digitados foram {sorted(vals[1])}')
