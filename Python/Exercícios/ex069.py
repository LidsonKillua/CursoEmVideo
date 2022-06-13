"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""

cadulto = chomem = cmulhercmenosdvinte = 0

while True:
    print('-' * 30)
    print(f'{"CADASTRE UMA PESSOA":^30}')
    print('-' * 30)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').strip().upper()[0]

    if idade > 18:
        cadulto += 1

    if sexo == 'M':
        chomem += 1

    elif sexo == 'F' and idade < 20:
        cmulhercmenosdvinte += 1

    print('-' * 30)
    opc = ' '
    while opc not in 'SN':
        opc = input('Quer Continuar? [S/N] ').strip().upper()[0]

    if opc == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cadulto}')
print(f'Ao todo temos {chomem} homens cadastrados')
print(f'E temos {cmulhercmenosdvinte} mulheres com menos de 20 anos')
