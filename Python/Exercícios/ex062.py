"""
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

print('=' * 40)
print(f'{"Gerador de PA":^40}')
print('=' * 40)

prim = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 0
fim = 10

while c < fim:
    print(prim, end=' -> ')
    prim += r
    c += 1

    if c == fim:
        print('PAUSA')
        fim += int(input('Quantos termos você quer mostrar a mais? '))


print(f'Progressão finalizada com {c} termos mostrados.')
