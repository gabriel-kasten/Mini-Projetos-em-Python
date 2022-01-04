import random

nome1 = input('Digite o nome de um aluno: ')
nome2 = input('Digite o nome de um aluno: ')
nome3 = input('Digete o nome de um aluno: ')
nome4 = input('Digite o nome de um aluno: ')

nomes = [nome1, nome2, nome3, nome4]

print('Dos 4 alunos, o escolhido foi {}!'.format(random.choice(nomes)))

# de 4 nomes escolhe um e mostra o nome