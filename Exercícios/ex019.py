"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""
import random
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
alunos = [al1, al2, al3, al4]
print('O aluno escolhido foi {}'.format(alunos[random.randint(0, 3)]))

