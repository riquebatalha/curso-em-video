# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

perg = int(input("Digite um número: "))

dobro = perg * 2
triplo = perg * 3
raiz = perg ** (1/2)

print("O dobro de {} é {}".format(perg, dobro))
print("O triplo de {} é  {}".format(perg, triplo))
print("Raiz quadrade de {} é {}".format(perg, raiz))