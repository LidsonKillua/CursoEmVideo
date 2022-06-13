"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
men = n1
mai = n1
if n2 < men:  # min(n1, n2, n3)
    men = n2
if n3 < men:
    men = n3
if n2 > mai:  # max(n1, n2, n3)
    mai = n2
if n3 > mai:
    mai = n3
print('O menor valor digitado foi {}'.format(men))
print('O maior valor digitado foi {}'.format(mai))
