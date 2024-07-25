# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# (0 °C × 9/5) + 32 
perg= float(input("Infome a tempartura em Celsius e ela será convertida para Fahrenheit: "))

convert = ((perg * 9) /5 ) + 32

print("A conversão de {} Graus Celsius é {:.2f} em Fahrenheit".format(perg, convert))

