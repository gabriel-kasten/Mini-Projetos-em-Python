salario = float(input('Qual o preço do produto?\n'))
porcentagemDesconto = int(input('Qual a porcentagem do desconto?\n'))

reajustePreco = salario - (salario * porcentagemDesconto / 100)

print('O valor atual é de {:.2f}! Muito bom!'.format(reajustePreco))
