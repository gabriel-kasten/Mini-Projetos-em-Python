from math import trunc

num = float(input('Digite um número com vírgula: '))
numReal = trunc(num)

print('O número real em {} é {}!'.format(num, numReal))