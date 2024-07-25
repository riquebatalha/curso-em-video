# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


larg = float(input("Informe a largura da parede: "))
alt  = float(input("Informe a altura da parede: "))

area = (larg * alt)
litros_tinta = area / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m²".format(larg, alt, area))
print("Para pintar toda a sua parede, será necessário {}L".format(litros_tinta))