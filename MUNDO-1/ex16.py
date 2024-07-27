# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

import math
perg = float(input("Digite um número de estilo float: "))
num_int = math.floor(perg)

print("O valor do número {} em número inteiro é {}".format(perg, num_int))
