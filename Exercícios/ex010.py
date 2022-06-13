"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

Considere US$1,00 = R$3,27
"""
din = float(input('Dinheiro em reais: '))
cot = 3.27
dol = din/cot
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}, com o dólar a {:.2f}'.format(din, dol, cot))
