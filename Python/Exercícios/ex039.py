"""
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nascimento
alistamento = nascimento + 18

print(f'Quem nasceu em {nascimento} tem {idade} anos em {anoatual}.')

if idade < 18:
    diferenca = 18 - idade
    print(f'Ainda faltam {diferenca} anos para o alistamento')
    print(f'Seu alistamento será em {alistamento}!')

elif idade > 18:
    diferenca = idade - 18
    print(f'Você já deveria ter se alistado há {diferenca} anos.')
    print(f'Seu alistamento foi em {alistamento}.')
else:
    print('Você deve se alistar IMEDIATAMENTE!')
