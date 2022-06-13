"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

while True:
    erro = 0

    valor = int(input('Que valor você quer sacar? R$'))
    for nota in [50, 20, 10, 1]:
        if valor >= nota:
            qtdnota = valor // nota
            valor -= qtdnota * nota
            print(f'Total de {qtdnota} cédulas de R${nota}')
        else:
            erro += 1

    if erro == 4:
        print('Esse valor não pode ser sacado com as cédulas disponíveis')
    else:
        break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
