# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de 
# dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

perg = float(input("Informe a quantidade de KM percorridos pelo carro alugado: "))
perg2 = int(input("Informe a quantiadde de dias no qual ele foi alugado: "))
total_pagar = (perg * 0.15) + (perg2 * 60) 

print("O número de KM's rodados pelo carro alugado foi de {}, e o número de dias alugado foi de {}, com isso, o total a se pagar é R${} ".format(perg, perg2, total_pagar))