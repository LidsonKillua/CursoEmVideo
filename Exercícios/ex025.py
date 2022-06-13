"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""
nome = str(input('Qual é o seu nome completo? ')).strip().upper()
# Primeira forma que eu fiz:
# i = nome.find('SILVA')
# print('Seu nome tem Silva? {}'.format('SILVA' in nome[i:]))
print('Seu nome tem Silva? {}'.format('SILVA' in nome))