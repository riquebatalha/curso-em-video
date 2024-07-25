# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

prec_produto = float(input("Informe o preço do seu produto: R$"))

desc =  prec_produto - (prec_produto * 0.05) 

print("O valor original do seu produto é de R${}, porém, com o desconto de 5%, ele vai ficar R${:.2f}".format(prec_produto, desc))

