"""
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

soma = 0
cont = 0
maior = 0
maisvelho = '<NOMEVAZIO>'
for i in range(1, 5):
    print(f'{f"{i} PESSOA":^20}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma += idade

    if sexo == 'M':
        if idade > maior:
            maior = idade
            maisvelho = nome
    else:
        if idade < 20:
            cont += 1

media = soma/4
print(f'A média de idade do grupo é de {media:} anos')
if maior > 0:
    print(f'O homem mais velho tem {maior} anos e se chama {maisvelho}.')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')
