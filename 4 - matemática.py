n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2

print(
    'A soma é {}, o produto é {} e a divisão é {:.2f}. A divisão inteira é {} e a potência é {}!'
    .format(soma, mult, div, divInt, exp))