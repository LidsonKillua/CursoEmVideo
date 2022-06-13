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
if (b + c) > a > abs(b - c):
    if (a + c) > b > abs(a - c):
        if (a + b) > c > abs(a - b):
            tri = True

if tri:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')