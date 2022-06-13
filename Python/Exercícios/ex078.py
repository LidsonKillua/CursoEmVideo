"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

vals = []
for i in range(5):
    vals.append(int(input(f'Digite um valor para a posição {i}: ')))

print('=-'*50)
print(f'Você digitou os valores {vals}')
txtmaior = f'O maior valor digitado foi {max(vals)} nas posições '
txtmenor = f'O menor valor digitado foi {min(vals)} nas posições '

for i in range(len(vals)):
    if vals[i] == max(vals):
        txtmaior += f'{i}... '
    elif vals[i] == min(vals):
        txtmenor += f'{i}... '
"""
for i, v in enumerate(vals):
    if v == max(vals):
        txtmaior += f'{i}... '
    elif v == min(vals):
        txtmenor += f'{i}... '
"""

print(txtmaior)
print(txtmenor)
