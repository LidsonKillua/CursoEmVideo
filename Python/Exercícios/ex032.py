"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

import time

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = time.localtime().tm_year

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
