"""
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

exp = input('Digite a expressão: ')
parentesis = list()

for i in exp:
    if i in '()':
        parentesis.append(i)

a = f = e = 0
if len(parentesis) > 0:
    if parentesis.count('(') == parentesis.count(')'):
        for i in parentesis:
            if i == '(':
                a += 1
            elif i == ')':
                f += 1
                if f > a:
                    print('Sua expressão está errada!')
                    e = 1
                    break
        if e != 1:
            print('Sua expressão está válida!')
    else:
        print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')

""" Utilizando pilhas: (Solução Guanabara)
pilha = []
for s in exp:
    if s == '(':
        pilha.append(s)
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(s)
            break

if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
"""
