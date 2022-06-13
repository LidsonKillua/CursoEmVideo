"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    print('-' * 30)
    val = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)

    if val < 0:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break

    for i in range(1, 11):
        print(f'{val} x {i:2} = {val * i}')
