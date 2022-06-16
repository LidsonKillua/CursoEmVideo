"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
"""
alunos = list()
aluno = list()

while True:
    aluno.append(input('Nome: '))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))

    alunos.append(aluno[:])
    aluno.clear()

    if input('Quer continuar? [S/N] ')[0] not in 'Ss':
        break

print('-=' * 30)
print('N.  NOME       MÉDIA')
print('-' * 30)

for i in range(len(alunos)):
    media = (alunos[i][1] + alunos[i][2]) / 2
    print(f'{i:<3} {alunos[i][0]:<10} {media:5.1f}')

while True:
    print('-' * 50)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))

    if mostrar == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break

    print(f'Notas de {alunos[mostrar][0]} são [{alunos[mostrar][1]:.1f}, {alunos[mostrar][2]:.1f}]')
