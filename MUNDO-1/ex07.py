#  Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

not1 = float(input("Informe sua nota: "))
not2 = float(input("Informe sua outra nota: "))
med = (not1 + not2) / 2
print("A média entre as notas {} e {} é de {} ".format(not1, not2, med))