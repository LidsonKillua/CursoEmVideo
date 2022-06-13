"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""

print('-' * 30)
print(f'{"LOJA SUPER BARATÃO":^30}')
print('-' * 30)

total = vlrmbarato = qtdmaior1000 = c = 0
prodmbarato = ' '

while True:
    nome = input('Nome do produto: ')
    preco = int(input('Preço: R$'))
    total += preco

    if preco > 1000:
        qtdmaior1000 += 1

    if c == 0 or preco < vlrmbarato:
        prodmbarato = nome
        vlrmbarato = preco

    opt = ' '
    while opt not in 'SN':
        opt = input('Quer continuar? [S/N]').strip().upper()[0]

    if opt == 'N':
        break

    c += 1

print(f'{" FIM DO PROGRAMA ":-^30}')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtdmaior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodmbarato} que custa R${vlrmbarato:.2f}')
