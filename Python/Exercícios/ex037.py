"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

bin() inteiro para binário
oct() inteiro para octal
hex() inteiro para hexadecimal
"""

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opt = int(input('Sua opção: '))

while opt != 1 and opt != 2 and opt != 3:
    opt = int(input('Sua opção: '))

if opt == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
    # [2:] por que os dois primeiros digitos dessas funções são apenas identificadores

elif opt == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opt == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

