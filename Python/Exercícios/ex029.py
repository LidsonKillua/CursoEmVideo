"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = float(input('Qual é a velocidade atual do carro? '))
valmult = 7
velmax = 80

if v > velmax:
    totmult = (v - velmax) * valmult
    print('MULTADO! Você excedeu o limite permitido que é de {}Km/h'.format(velmax))
    print('Você deve pagar uma multa de R${:.2f}!'.format(totmult))

print('Tenha um bom dia! Dirija com segurança! ')
