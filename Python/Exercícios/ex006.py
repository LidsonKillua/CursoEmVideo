"""
Crie um algorítmo que leia um número e mostre seu dobro, triplo e raiz quadrada
"""
n = int(input('Digite um número: '))
dobro = n*2
triplo = n*3
raiz = n**(1/2)
print('O número é {}, seu dobro: {},\ntriplo: {} e raiz quadrada: {:.2f}'.format(n, dobro, triplo, raiz))
