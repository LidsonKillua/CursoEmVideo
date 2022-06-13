"""
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
            'Mercado', 'Programador', 'Futuro')

print('-'*40, end='')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')

    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')
print(f'\n{"-"*40}')
