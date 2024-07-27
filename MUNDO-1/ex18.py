import math

perg = float(input(("Digite o ângulo que você deseja: ")))
rad = math.radians(perg)

print("Seno de {} é {:.2f}".format(perg, math.sin(rad)))
print("Cosseno de {} é {:.2f}".format(perg, math.cos(rad)))
print("Tangente de {} é {:.2f}".format(perg, math.tan(rad)))
