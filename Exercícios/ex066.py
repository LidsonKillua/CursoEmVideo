"""
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre elas (desconsiderando o flag).
"""

soma = qtd = 0
while True:
    val = int(input('Digite um valor (999 para parar): '))

    if val == 999:
        break

    qtd += 1
    soma += val

print(f'A soma dos {qtd} valores foi {soma}!')
