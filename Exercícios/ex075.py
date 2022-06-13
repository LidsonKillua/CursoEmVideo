"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
"""

nums = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))

print(f'Você digitou os valores {nums}')
print(f'O valor 9 apareceu {nums.count(9)} vezes')

if 3 in nums:
    print(f'O valor 3 pareceu na {nums.index(3) + 1}ª Posição')
else:
    print('O valor 3 não foi digitado')

c = 0
for i in nums:
    if i % 2 == 0:
        c += 1
print(f'Os valores pares digitados foram {c}')
