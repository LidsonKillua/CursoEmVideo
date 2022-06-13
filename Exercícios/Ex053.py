"""
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços. Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
"""
f = input('Digite uma frase: ').strip().upper()

# lista = f.split()
# frase = ''.join(lista)  Utilizando isso eu não precisaria do for abaixo
frase = ''
for i in range(0, len(f)):
    if f[i] != ' ':
        frase += f[i]

inverso = ''
# inverso = frase[::-1]  Com esse fatiamento eu não precisaria do for abaixo
for i in range(len(frase)-1, -1, -1):
    inverso += frase[i]

print(f'O inverso de {frase} é {inverso}')

if frase == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
