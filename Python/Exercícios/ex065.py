"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
"""
cont = 'S'
qtd = soma = 0

while cont.upper() == 'S':
    n = int(input('Digite um número: '))
    qtd += 1
    soma += n

    if qtd == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    cont = input('Quer continuar? [S/N]: ').strip()[0]

media = soma / qtd

print(f'Você digitou {qtd} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
