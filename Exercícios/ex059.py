"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))


def options():
    print("""        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa""")
    result = int(input('>>>>> Qual é a sua opção? '))
    return result


opt = options()
while opt != 5:
    if opt == 1:
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')

    elif opt == 2:
        print(f'O resultado de {n1} x {n2} é {n1 * n2}')

    elif opt == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior valor é {n1}')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior valor é {n2}')
        else:
            print('Os dois valores são iguais!')

    elif opt == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))

    else:
        print('Opção inválida. Tente novamente')

    print('=-=' * 10)
    sleep(2)
    opt = options()

print('Finalizando...')
print('=-=' * 10)
sleep(2)
print('Fim do programa. Volte Sempre!')
