"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
i = int(input('Digite um número entre 0 e 20: '))
while not 0 <= i <= 20:
    i = int(input('Tente novamente, digite um número entre 0 e 20: '))

exten = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quatorze', 'Quize', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

print(f'Você digitou o número {exten[i]}')
