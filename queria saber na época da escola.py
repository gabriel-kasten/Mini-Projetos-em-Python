from math import sin, cos, tan

ang = int(input('Digite o ângulo: '))

seno = sin(ang)
coss = cos(ang)
tang = tan(ang)

print('Do ângulo {} é possível dizer que o \nseno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, seno, coss, tang))