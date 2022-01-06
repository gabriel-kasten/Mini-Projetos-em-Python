from random import shuffle

input_aluno_1 = input('Primeiro nome: ')
input_aluno_2 = input('Segundo nome: ')
input_aluno_3 = input('Terceiro nome: ')
input_aluno_4 = input('Quarto nome: ')

ordem_alunos = [input_aluno_1, input_aluno_2, input_aluno_3, input_aluno_4] # cria uma "lista"
shuffle(ordem_alunos) # embaralha a lista!

print('A ordem de apresentações é: ')
print(ordem_alunos)
