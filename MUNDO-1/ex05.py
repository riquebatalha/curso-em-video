# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor

perg = int(input("Informe um número: "))
a = perg - 1
s = perg + 1

print("Sucessor do número {} é {}".format(perg, s))
print("Antecessor do número {} é {}.".format(perg, a))