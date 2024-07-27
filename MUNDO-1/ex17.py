# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


# Maneira sem uso de funções.
cateto_ad = float(input("Informe o valor do cateto adjacente: "))
cateto_op = float(input("Informe o valor do cateto oposto: "))
h = (cateto_ad ** 2 + cateto_op ** 2) ** (1/2) 

print("A soma do cateto adjacente {} e do cateto oposto {}, da o comprimento da hipotenusa de {:.2f}".format(cateto_ad, cateto_op, h))


# Maneira de fazer usando a biblioteca Math

import math
ca = float(input("Informe o valor do cateto adjacente: "))
co = float(input("Informe o valor do cateto oposto: "))
h = math.hypot(co, ca)

print("A soma do cateto adjacente {} e do cateto oposto {}, da o comprimento da hipotenusa de {:.2f}".format(cateto_ad, cateto_op, h))