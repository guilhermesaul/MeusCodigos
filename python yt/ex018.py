from math import radians, tan, cos, sin
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}\nO ângulo de {} tem o cosseno de {:.2f}\nO ângulo de {} tem a tangente de {:.2f}'.format(ang, seno, ang, cosseno, ang, tan))
