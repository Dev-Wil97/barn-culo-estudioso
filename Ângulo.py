# barn-culo-estudioso
Programas básicos de aprendizado :)

# Calculando o ângulo se SENO / COSSENO / TANGENTE

from math import radians, sin, cos, tan

ângulo= float(input('Digite o angulo que você deseja: '))

seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))

cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ângulo, tangente))
