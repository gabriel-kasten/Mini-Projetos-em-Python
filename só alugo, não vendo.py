diasAlugados = int(input('Quantos dias alugados? '))
kmRodados = float(input('Quantos quilometros rodados? '))

pagar = (diasAlugados * 60) + (kmRodados * 0.15)

print('O total a pagar é de {:.2f}!'.format(pagar))
