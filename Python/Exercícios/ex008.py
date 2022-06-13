"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
"""

metros = float(input('Digite o valor em metros: '))
print('{:.2f} metro(s) são {:.2f} centímetro(s) e {:.2f} milímetro(s)'.format(metros, metros*100, metros*1000))
# Melhoria proposta:
print()
print()
print('{:.2f}km'.format(metros/1000))
print('{:.2f}hm'.format(metros/100))
print('{:.2f}dam'.format(metros/10))
print('{:.2f}m'.format(metros))
print('{:.2f}dm'.format(metros*10))
print('{:.2f}cm'.format(metros/100))
print('{:.2f}mm'.format(metros/1000))
