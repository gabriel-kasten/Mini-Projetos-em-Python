nome = str(input('Digite seu nome: ')).split()
print('<<< Analizando seu nome >>>')

print('Seu nome em maiúsculas é {}'.format(nome[0].upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))