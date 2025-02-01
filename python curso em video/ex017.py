'''co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('Aqui temos 3 valores que representam um triangulo retangulo, sendo eles; \nO cateto oposto: {} \nO cateto adjacente: {} \nE a hipotenusa: {:.2f}'.format(co,  ca, h))'''

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
