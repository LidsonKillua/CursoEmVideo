"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0

while True:
    print('=-' * 30)
    jognum = int(input('Diga um valor: '))

    jogesc = ' '
    while jogesc not in 'PI':
        jogesc = input('Par ou Ímpar? [P/I] ').strip().upper()[0]

    compnum = randint(0, 10)
    soma = jognum + compnum
    par = soma % 2 == 0

    print('-' * 30)
    print(f'Você jogou {jognum} e o computador {compnum}. Total de {soma} ', end='')

    if par:
        print('DEU PAR')
    else:
        print('DEU ÍMPAR')
    print('-' * 30)

    if jogesc == 'P' and par:
        print('Você VENCEU!')
        vitorias += 1
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU!')
        break

print('=-' * 30)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
