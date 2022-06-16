"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

m = list()
sompar = somterccol = maxseglin = val = 0

for i in range(3):
    for j in range(3):
        val = int(input(f'Digite um valor para [{i}, {j}]: '))
        m.append(val)

        if val % 2 == 0:
            sompar += val

        if j == 2:
            somterccol += val

        if i == 1:
            if j == 0:
                maxseglin = val
            else:
                if val > maxseglin:
                    maxseglin = val

print('-='*40)
for i in range(9):
    if (i + 1) % 3 == 0:
        print(f'[{m[i]:^5}]')
    else:
        print(f'[{m[i]:^5}]', end='')
print('-='*40)

print(f'A soma dos valores pares é {sompar}')
print(f'A soma dos valores da terceira coluna é {somterccol}')
print(f'O maior valor da segunda linha é {maxseglin}.')
