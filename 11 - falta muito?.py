b = int(input('Qual a largura da parede? '))
h = int(input('Qual a altura da parede? '))

area = h * b
quantBaldes = area / 2

print('A area total foi de {}m² e serão necessários {}l para pintar essa parede!'.format(area, quantBaldes))
