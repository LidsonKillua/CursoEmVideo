"""
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

vals = []
vals.append(int(input('Digite um valor: ')))

while input('Quer continuar? [S/N] ')[0] in 'Ss':
    vals.append(int(input('Digite um valor: ')))

print('-='*40)
print(f'Você digitou {len(vals)} elementos.')
print(f'Os valores em ordem decrescente são {vals.sort(reverse=True)}')

if 5 in vals:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
