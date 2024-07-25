# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Informe seu salário: R$: "))

aumento = salario + (salario * 0.15)

print("Um funcionário que ganhava R${}, depois do aumento de 15%, irá receber R${:.2f}".format(salario, aumento))