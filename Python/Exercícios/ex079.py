"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
"""

val = 0
vals = []
vals.append(int(input('Digite um valor: ')))
print('Valor adicionado com sucesso...')

while input('Quer continuar? [S/N] ')[0] in 'Ss':
    val = int(input('Digite um valor: '))

    if val not in vals:
        vals.append(val)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

print('-='*50)
print(f'Você digitou os valores {sorted(vals)}')
