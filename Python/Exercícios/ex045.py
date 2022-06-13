"""
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep

jogadapc = randint(0,2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogadaplayer = int(input('Qual é Sua Jogada? '))

if jogadaplayer != 0 and jogadaplayer != 1 and jogadaplayer != 2:
    print('Jogada inválida, tente novamente.')
else:
    sleep(0.5)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!')

    print('-=' * 11)

    if jogadapc == 0:
        print('Computador jogou Pedra')
    elif jogadapc == 1:
        print('Computador jogou Papel')
    else:
        print('Computador jogou Tesoura')

    if jogadaplayer == 0:
        print('Jogador jogou Pedra')
    elif jogadaplayer == 1:
        print('Jogador jogou Papel')
    else:
        print('Jogador jogou Tesoura')

    print('-=' * 11)

    if jogadaplayer == jogadapc:
        print('EMPATE')

    else:
        if jogadapc == 0:
            if jogadaplayer == 1:
                print('JOGADOR VENCE')
            if jogadaplayer == 2:
                print('COMPUTADOR VENCE')

        elif jogadapc == 1:
            if jogadaplayer == 2:
                print('JOGADOR VENCE')
            if jogadaplayer == 0:
                print('COMPUTADOR VENCE')

        elif jogadapc == 2:
            if jogadaplayer == 0:
                print('JOGADOR VENCE')
            if jogadaplayer == 1:
                print('COMPUTADOR VENCE')
