"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

cdia = 60  # custo por dia
ckm = 0.15  # custo por Km rodado
qtddia = int(input('Quantos dias alugados? '))
qtdkm = float(input('Quantos Km rodados? '))

print('O total a pagar é de R${:.2f}'.format(qtddia * cdia + qtdkm * ckm))
