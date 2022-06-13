"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

''' cola:
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''
tri = False
if a > abs(b - c) and a < (b + c):
    if b > abs(a - c) and b < (a + c):
        if c > abs(a - b) and c < (a + b):
            tri = True

if tri:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')