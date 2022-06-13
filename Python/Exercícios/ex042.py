"""
Exercício Python 42:
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""

s1 = int(input('Primeiro Seguimento: '))
s2 = int(input('Segundo seguimento: '))
s3 = int(input('Terceiro seguimento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    if s1 == s2 == s3:
        print('Os Segmentos acima podem formar um triângulo equilátero')
    elif (s1 == s2 != s3) or (s1 != s2 == s3) or (s1 == s3 != s2):
        print('Os segmentos acima podem formar um triângulo isosceles')
    elif s1 != s2 != s3 != s1:
        print('Os segmentos acima podem formar um triângulo escaleno')
else:
    print('Os Segmentos acima não podem formar um triângulo')
