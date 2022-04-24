'''
    EXERCÍCIO - ÁREA DO CÍRCULO

    ENTRADA = RAIO (FLOAT)
    ÁREA = PI*R^2
'''

from math import pi

r = float(input("Digite o valor do raio do círculo: "))
A = pi*r**2

print(f"\nA = {A:,.4f} u.m.\n")
