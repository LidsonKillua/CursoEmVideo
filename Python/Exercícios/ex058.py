"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

n = randint(0, 10)
ne = int(input('Qual é seu palpite? '))
tent = 1

while n != ne:
    if n > ne:
        print('Mais... Tente outra vez.')
    else:
        print('Menos... Tente outra vez.')

    ne = int(input('Qual é seu palpite? '))
    tent += 1

print(f'Acertou com {tent} tentativas, Parabéns!')