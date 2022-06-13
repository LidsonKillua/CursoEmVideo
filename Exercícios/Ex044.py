"""
Exercício Python 44:
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal

– 3x ou mais no cartão: 20% de juros
"""
print(10*'=',' LOJAS LIDSON ', 10*'=')
# print('{:=^40}'.format(' LOJAS LIDSON '))

preco = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à Vista Dinheiro/Cheque
[ 2 ] à Vista Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão""")
opt = int(input('Qual é a opção? '))

if opt == 1:
    valorfinal = preco - (0.1 * preco)
elif opt == 2:
    valorfinal = preco - (0.05 * preco)
elif opt == 3:
    valorfinal = preco
    print(f'Sua compra será parcelada em 2x de R${valorfinal/2:.2f} SEM JUROS.')
elif opt == 4:
    valorfinal = preco + (0.2 * preco)
    qtdparcelas = int(input('Quantas parcelas? '))
    valorparcelas = valorfinal / qtdparcelas
    print(f'Sua compra será parcelada em {qtdparcelas}x de R${valorparcelas:.2f} COM JUROS.')
else:
    print('opção inválida')
    valorfinal = preco

print(f'Sua compra de R${preco:.2f} vai custar {valorfinal:.2f} no final.')
