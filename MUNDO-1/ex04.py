# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

perg = input("Digite algo: ")

print("O tipo primitido do que você escreveu é {}".format(type(perg)))
print("Só tem espaços: {}".format(perg.isspace()))
print("É um número? {}".format(perg.isnumeric()))
print("É alfabético? {}".format(perg.isalpha()))
print("É alfanumérico? {}".format(perg.isalnum()))
print("Está em minúscula? {}".format(perg.islower()))
print("Está em maiúscula? {}".format(perg.isupper()))
print("Está captalizada? {}".format(perg.istitle()))