"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(''.join(lista))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(lista[0], len(lista[0])))
