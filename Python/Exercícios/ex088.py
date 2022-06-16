"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
nums = list()

print('-=' * 3, f'SORTEANDO {qtd} JOGOS', '-=' * 3)

for i in range(qtd):
    while True:
        novo = randint(1, 60)
        if novo not in nums:
            nums.append(novo)
        if len(nums) == 6:
            break

    sleep(1)
    print(f'Jogo {i + 1}: {sorted(nums)}')
    nums.clear()

print('-=' * 5 + '< BOA SORTE! >' + '-=' * 5)
