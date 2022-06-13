"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""

num = int(input('Digite um número para calcular seu fatorial: '))
c = 1
fatorial = num
texto = f'Calculando {num}! = {num} '

while c < num:
    fatorial = fatorial * (num - c)
    texto += f'x {num - c} '
    c += 1

texto += f' = {fatorial}'
print(texto)
