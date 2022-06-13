"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""
p = str(input('Em que cidade você nasceu? ')).strip().upper().split()
print('SANTO' in p[0])
