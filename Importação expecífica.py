from math import sqrt, floor
num = int(input('Digite um número para tirar a raiz: '))

raiz = sqrt(num)

print('A raiz de {} é {:.2f}'.format(num, floor(raiz)))