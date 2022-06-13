"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o empréstimo será negado.
"""

# Var
vcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anosfin = int(input('Quantos anos de financiamento? '))
mesesfin = anosfin*12

# Inicio
prest = vcasa/mesesfin
trintaporc = salario * 0.3

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(vcasa, anosfin, prest))

if prest > trintaporc:
    print('Empréstimo NEGADO!')
elif prest <= trintaporc:
    print('Empréstimo pode ser CONCEDIDO!')
