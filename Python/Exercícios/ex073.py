"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do São Paulo.
Tabela Brasileirão 02/06/2022
"""


def main():
    tabela = ('Palmeiras', 'Atlético - MG', 'Corinthians', 'Coritiba', 'São Paulo', 'Athletico - PR', 'Botafogo',
              'Flamengo', 'Santos', 'América - MG', 'Fluminense', 'Internacional', 'Avaí', 'Bragantino', 'Ceará',
              'Goiás', 'Cuiabá', 'Atlético - GO', 'Juventude', 'Fortaleza')

    separador()
    print(f'Lista de times do Brasileirão: {tabela}')
    separador()
    print(f'Os 5 primeiros são: {tabela[0:5]}')
    separador()
    print(f'Os quatro últimos são: {tabela[-4:]}')
    separador()
    print(f'Times em Ordem Alfabética: {sorted(tabela)}')
    separador()
    print(f"O time do São Paulo está na {tabela.index('São Paulo') + 1}ª posição")
    separador()


def separador():
    print('=-=' * 40)


main()
